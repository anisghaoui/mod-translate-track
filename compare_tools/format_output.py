import argparse
from Mod import Mod
from compare_configs import compare_configs

from configparser import ConfigParser

TEXT_DISPLAYED = {
    "added_keys": "################## These keys were added since last update ##################",
    "removed_keys": "These keys were removed since last update",
    "modified_keys": "These keys were updated since last update",
    "unmodified_keys": "################## These keys were unchanged ##################",
}


def format_output(config_json, mod):
    config_out = ConfigParser()

    # add_sections = config["added_sections"]
    # removed_sections = config["removed_sections"]
    common_sections = config_json["modified_sections"]

    # Write the file section by section starting with the common ones
    path = "output/" + mod.name + "/locale.cfg"
    with open(path, "w+") as f:
        for section_name in common_sections.keys():
            config_out.add_section(section_name)
            section = common_sections[section_name]
            f.write("modified_sections" + "\n")
            for sub_key, value in section.items():
                # key_kind is either: added_keys, removed_keys, modified_keys, unmodified_keys
                if len(value) != 0:
                    config_out.set(section_name,  "# " + sub_key,
                                   TEXT_DISPLAYED[sub_key])

                    for kk, vv in value.items():
                        if sub_key == "modified_keys":
                            # it is written as "from", "to" keys
                            vv = vv["to"]
                        config_out.set(section_name, kk, vv)

            config_out.write(f)
            config_out = ConfigParser()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('mod_url')
    args = parser.parse_args()

    mod = Mod(args.mod_url)
    path_previous = mod.path_en / "locale.cfg"
    path_new = mod.path_en / "locale copy.cfg"
    # path_new = mod.download_locale_en()

    diff = compare_configs(path_previous, path_new)
    format_output(diff, mod)
