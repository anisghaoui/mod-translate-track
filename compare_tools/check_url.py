import re


class InvalidURLException(Exception):
    pass


def check_url(url: str):
    pattern = "https://github.com/*"
    if not re.match(pattern, url):
        raise InvalidURLException(f"rejected url: {url}")


def dump_faulty_urls(urls):
    for url in urls:
        print(f"Faulty url detected: {url}. Rejecting track.")
