from compare_tools import Mod, compare_configs, format_output, check_url
import argparse


def main(url: str, language: str):
    check_url.check_url(url)
    print(f"checking mod at: {url}")
    mod = Mod.Mod(url)
    diff = compare_configs.compare_configs(
        mod.path_en/"locale.cfg", mod)
    format_output.format_output(diff, mod, language)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('mod_url')
    parser.add_argument('language')
    parser.add_argument('--f', "--overwrite",
                        action="store_true", default=False)
    args = parser.parse_args()

    main(args.mod_url, args.language)
