import re
from compare_tools import Mod, compare_configs, format_output
import argparse


class InvalidURLException(Exception):
    pass


def check_url(url: str):
    pattern = "https://github.com/*"
    if not re.match(pattern, url):
        raise InvalidURLException(f"rejected url: {url}")


def main(url: str, language: str):
    check_url(url)
    print(f"checking mod at: {url}")
    mod = Mod.Mod(url)
    diff = compare_configs.compare_configs(
        mod.path_en/"locale.cfg", mod.path / "locale" / language / "locale.cfg")
    # TODO: I am using local EN vs Language. I need to use remote EN vs locale EN AND output it in LANGUAGE
    format_output.format_output(diff, mod)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('mod_url')
    parser.add_argument('language')
    parser.add_argument('--f', "--overwrite",
                        action="store_true", default=False)
    args = parser.parse_args()

    main(args.mod_url, args.language)
