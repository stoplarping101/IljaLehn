"""Submit URLs to a Cloudflare Worker that performs the crawling."""

import json
import os
import sys
from urllib.request import Request, urlopen


def main() -> None:
    endpoint = os.environ.get("CF_WORKER_URL")
    if not endpoint:
        raise SystemExit("Set CF_WORKER_URL to your deployed Worker endpoint.")

    urls = sys.argv[1:]
    if not urls:
        raise SystemExit("Usage: python crawl.py https://example.com [URL ...]")

    request = Request(
        endpoint,
        data=json.dumps({"urls": urls}).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urlopen(request, timeout=60) as response:
        print(response.read().decode("utf-8"))


if __name__ == "__main__":
    main()
