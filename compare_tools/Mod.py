import requests
from pathlib import Path

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


if __name__ == "__main__":
    mod = Mod("https://github.com/Wip-Sama/Smart_Inserters")
    mod.download_locale_en()
