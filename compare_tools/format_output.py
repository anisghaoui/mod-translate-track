import argparse
from Mod import Mod
from compare_configs import compare_configs

from configparser import ConfigParser


def format_output(config_json, mod):
    config_out = ConfigParser()

    # add_sections = config["added_sections"]
    # removed_sections = config["removed_sections"]
    common_sections = config_json["common_sections"]

    # Write the file section by section starting with the common ones
    path = "output/" + mod.name + "/locale.cfg"
    with open(path, "w+") as f:
        for section_name in common_sections.keys():
            config_out.add_section(section_name)
            section = common_sections[section_name]
            for k, v in section.items():
                print(k)
                print(v)
                if len(v) != 0:
                    for kk, vv in v.items():
                        config_out.set(section_name, kk, vv)

    with open('output.cfg', 'w') as cf:
        config_out.write(cf)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('mod_url')
    args = parser.parse_args()

    mod = Mod(args.mod_url)
    path_previous = mod.path_en / "locale.cfg"
    # path_new = mod.download_locale_en()

    diff = compare_configs(path_previous, path_previous)

    format_output(diff, mod)
