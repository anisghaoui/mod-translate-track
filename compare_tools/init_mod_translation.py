import os
import argparse

from Mod import Mod


def init_mod(mod_repo_url, overwrite=False):
    mod = Mod(mod_repo_url)
    if os.path.exists(mod.path) and not overwrite:
        raise FileExistsError("Mod folder already exists in repository. Use --f to overwrite.")

    os.makedirs(mod.path_en, exist_ok=overwrite)
    os.makedirs(mod.path_en, exist_ok=overwrite)
    mod.download_locale_en()

    print(
        f"Locale File downloaded for {mod.name} by {mod.owner}. Ready to translate!")

    return mod

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('mod_url')
    parser.add_argument('--f', "--overwrite",
                        action="store_true", default=False)
    args = parser.parse_args()
    init_mod(args.mod_url, args.f)
