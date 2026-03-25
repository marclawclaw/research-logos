#!/usr/bin/env python3
"""
Logos Module Crawler
Searches GitHub for repos (outside logos-co and logos-blockchain orgs)
that contain signals of Logos module usage.
"""

import subprocess
import json
import time
import sys
from datetime import datetime, timezone

EXCLUDED_ORGS = {"logos-co", "logos-blockchain"}

SEARCH_SIGNALS = [
    ("LogosAPIClient", "code"),
    ("LogosResult", "code"),
    ("LogosModeConfig", "code"),
    ("logos-cpp-sdk", "code"),
    ("mkLogosModule", "code"),
    ("Q_INTERFACES(PluginInterface) Logos", "code"),
]

def gh_api(path, params=None):
    """Call GitHub API via gh CLI."""
    url = f"https://api.github.com{path}"
    if params:
        qs = "&".join(f"{k}={v}" for k, v in params.items())
        url = f"{url}?{qs}"
    result = subprocess.run(
        ["gh", "api", "--header", "Accept: application/vnd.github+json", url],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print(f"  API error: {result.stderr.strip()}", file=sys.stderr)
        return None
    return json.loads(result.stdout)

def search_code(query, page=1):
    """Search GitHub code."""
    result = subprocess.run(
        ["gh", "api",
         "--header", "Accept: application/vnd.github+json",
         f"https://api.github.com/search/code?q={query}&per_page=100&page={page}"],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print(f"  Search error: {result.stderr.strip()}", file=sys.stderr)
        return None
    return json.loads(result.stdout)

def get_repo_info(full_name):
    """Get repo metadata."""
    data = gh_api(f"/repos/{full_name}")
    if not data:
        return None
    return {
        "full_name": data.get("full_name"),
        "description": data.get("description"),
        "language": data.get("language"),
        "pushed_at": data.get("pushed_at"),
        "stargazers_count": data.get("stargazers_count"),
        "html_url": data.get("html_url"),
        "owner": data.get("owner", {}).get("login"),
    }

def main():
    found_repos = {}  # full_name -> {repo_info, signals}
    log_entries = []

    run_time = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    print(f"Starting Logos module crawl at {run_time}")

    for signal, search_type in SEARCH_SIGNALS:
        print(f"\nSearching for: {signal}")
        log_entries.append(f"### Signal: `{signal}`")
        signal_hits = 0

        for page in range(1, 6):  # max 5 pages = 500 results
            print(f"  Page {page}...")
            # URL-encode the query
            query = signal.replace(" ", "+").replace("(", "%28").replace(")", "%29")
            data = search_code(query, page)

            if not data:
                break

            items = data.get("items", [])
            if not items:
                break

            for item in items:
                repo = item.get("repository", {})
                full_name = repo.get("full_name", "")
                owner = repo.get("owner", {}).get("login", "")

                # Filter excluded orgs
                if owner.lower() in EXCLUDED_ORGS:
                    continue

                signal_hits += 1

                if full_name not in found_repos:
                    found_repos[full_name] = {
                        "full_name": full_name,
                        "signals": []
                    }
                if signal not in found_repos[full_name]["signals"]:
                    found_repos[full_name]["signals"].append(signal)

            # Check if we've hit the last page
            total = data.get("total_count", 0)
            if page * 100 >= total:
                break

            # Rate limit: search API allows 10 req/min authenticated
            time.sleep(7)

        log_entries.append(f"- Hits (excl. logos orgs): {signal_hits}")
        print(f"  → {signal_hits} hits outside logos orgs")

        # Sleep between signals to avoid rate limiting
        time.sleep(10)

    # Enrich with repo metadata
    print(f"\nEnriching {len(found_repos)} repos with metadata...")
    enriched = []
    for i, (full_name, data) in enumerate(found_repos.items()):
        print(f"  [{i+1}/{len(found_repos)}] {full_name}")
        info = get_repo_info(full_name)
        if info:
            info["signals"] = data["signals"]
            enriched.append(info)
        else:
            enriched.append({
                "full_name": full_name,
                "signals": data["signals"],
                "error": "could not fetch metadata"
            })
        time.sleep(1)

    # Save results
    output = {
        "crawled_at": run_time,
        "total_repos": len(enriched),
        "repos": enriched
    }

    out_path = "/home/marclaw/src/marclawclaw/research-logos/crawler/found-modules.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved {len(enriched)} repos to {out_path}")

    # Write run log
    log_path = "/home/marclaw/src/marclawclaw/research-logos/crawler/run-log.md"
    with open(log_path, "a") as f:
        f.write(f"\n## [{run_time}] Logos Module Crawl — ok\n")
        f.write(f"- Repos found: {len(enriched)}\n")
        f.write(f"- Signals searched: {len(SEARCH_SIGNALS)}\n")
        for entry in log_entries:
            f.write(f"{entry}\n")
        f.write("\n")

    print("Done.")

if __name__ == "__main__":
    main()
