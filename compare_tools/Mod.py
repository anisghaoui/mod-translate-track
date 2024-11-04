import requests
from pathlib import Path

RAW_PRE = "https://raw.githubusercontent.com/"


class Mod:
    def __init__(self, mod_url):
        res = mod_url.split("/")
        self.mod_name = res[-1]
        self.mod_owner = res[-2]

        self.path = Path("mods_locale/" + self.mod_name).resolve()
        self.path_en = self.path / "locale/en"

    def download_locale_en(self):
        # download the English version
        req = requests.get(
            f"{RAW_PRE}/{self.mod_owner}/{self.mod_name}/refs/heads/main/locale/en/locale.cfg")
        if req.status_code != 200:
            raise ConnectionError('Request failed. CHeck provided URL')
        config_str = req.content.decode(req.encoding)

        with open(self.path_en / "locale.cfg", "w", encoding=req.encoding) as f:
            f.write(config_str)


if __name__ == "__main__":
    mod = Mod("https://github.com/Wip-Sama/Smart_Inserters")
    mod.download_locale_en()
