from Mod import Mod
import configparser


def parse_config(mod: Mod):
    cfg = configparser.ConfigParser()
    cfg.read(mod.path_en / "locale.cfg")
    sections = cfg.sections()
    print(sections)


if __name__ == "__main__":
    mod = Mod("https://github.com/Wip-Sama/Smart_Inserters")
    parse_config(mod)
