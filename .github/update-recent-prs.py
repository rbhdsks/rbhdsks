"""Refresh the profile README with the latest public pull requests."""

import json
import os
from datetime import datetime
from pathlib import Path
import re
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from zoneinfo import ZoneInfo

START = "<!-- recent-pull-requests:start -->"
END = "<!-- recent-pull-requests:end -->"
SEARCH = "https://api.github.com/search/issues?" + urlencode({
    "q": "is:pr is:public author:rbhdsks",
    "sort": "created",
    "order": "desc",
    "per_page": 8,
})


def recent_pull_requests():
    headers = {"Accept": "application/vnd.github+json"}
    if token := os.environ.get("GITHUB_TOKEN"):
        headers["Authorization"] = f"Bearer {token}"
    with urlopen(Request(SEARCH, headers=headers), timeout=20) as response:
        results = json.load(response)
    if results["incomplete_results"]:
        raise RuntimeError("GitHub returned incomplete pull request results")
    return results["items"]


def markdown(items):
    lines = []
    for item in items:
        url = item["html_url"]
        repo = item["repository_url"].split("/repos/", 1)[1]
        title = re.sub(r'([\\`*_{}\[\]()<>#+.!|])', r'\\\1', " ".join(item["title"].split()))
        status = "Merged" if item["pull_request"].get("merged_at") else item["state"].capitalize()
        created = datetime.fromisoformat(item["created_at"].replace("Z", "+00:00"))
        date = created.astimezone(ZoneInfo("Asia/Kolkata")).strftime("%d %b %Y")
        lines.append(f"- [{title}]({url}) on [`{repo}`](https://github.com/{repo}) · {status} · {date}")
    return "\n".join(lines) or "No public pull requests found."


def main():
    readme = Path(__file__).resolve().parents[1] / "README.md"
    original = readme.read_text(encoding="utf-8")
    if original.count(START) != 1 or original.count(END) != 1 or original.index(START) > original.index(END):
        raise RuntimeError("Expected one ordered pair of pull request markers")
    before, _, remainder = original.partition(START)
    _, _, after = remainder.partition(END)
    updated = f"{before}{START}\n{markdown(recent_pull_requests())}\n{END}{after}"
    if original != updated:
        readme.write_text(updated, encoding="utf-8")


if __name__ == "__main__":
    main()
