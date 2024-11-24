import requests
from pathlib import Path
import os
RAW_PRE = "https://raw.githubusercontent.com/"


class Mod:
    name = None
    owner = None

    def __init__(self, mod_url):
        res = mod_url.split("/")
        self.name = res[-1]
        self.owner = res[-2]

        self.path = Path("mods_locale/" + self.name).resolve()
        self.path_en = self.path / "locale/en"
        
        if not os.path.exists(self.path_en):
            init_mod(self)

    def download_locale_en(self, store=True):
        # download the English version
        req = requests.get(
            f"{RAW_PRE}/{self.owner}/{self.name}/refs/heads/main/locale/en/locale.cfg", timeout=10)
        if req.status_code != 200:
            raise ConnectionError('Request failed. CHeck provided URL')
        config_str = req.content.decode(req.encoding)

        if store is True:
            with open(self.path_en / "locale.cfg", "w", encoding=req.encoding) as f:
                f.write(config_str)
        return config_str



def init_mod(mod, overwrite=False):
    if os.path.exists(mod.path) and not overwrite:
        raise FileExistsError("Mod folder already exists in repository. Use --f to overwrite.")
    print(f"Mod {mod.name} by {mod.owner} not intialised. Intialising...")
    os.makedirs(mod.path_en, exist_ok=overwrite)
    mod.download_locale_en()
    print(f"Locale File downloaded for {mod.name} by {mod.owner}. Ready to translate!")
    return mod


if __name__ == "__main__":
    mod = Mod("https://github.com/Wip-Sama/Smart_Inserters")
