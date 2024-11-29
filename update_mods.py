from compare_tools import Mod, check_url
import git


def update_mods():
    repo = git.Repo(".")
    with open("mod_list.txt", "r") as f:
        urls = f.read().splitlines()

        for url in urls:
            urls = check_url.check_url(url)
            mod = Mod.Mod(url)
            mod.download_locale_en()

        repo.index.add("mods_locale/*")
        repo.index.commit("update mod En locale")


if __name__ == "__main__":
    update_mods()
