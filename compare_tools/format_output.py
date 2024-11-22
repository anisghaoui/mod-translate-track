import argparse
from Mod import Mod
from compare_configs import compare_configs
from configparser import ConfigParser

TEXT_DISPLAYED = {
    "added_keys": "These keys were added since last update",
    "removed_keys": "These keys were removed since last update",
    "modified_keys": "These keys were updated since last update",
    "unmodified_keys": "These keys were not changed"
}


def format_output(config_json, mod):
    config_out = ConfigParser()
    config_ret = ConfigParser()

    added_sections = config_json["added_sections"]
    removed_sections = config_json["removed_sections"]
    modified_sections = config_json["modified_sections"]

    # Write the file section by section starting with the common ones
    path = "output/" + mod.name + "/locale.cfg"
    with open(path, "w+") as f:
        # added_sections
        for sections in "added_sections", "removed_sections":
            if len(added_sections) or len(removed_sections):
                f.write(f"# {sections}\n")
                for section_name in added_sections.keys():
                    config_out.add_section(section_name)
                    config_ret.add_section(section_name)

                    for key, value in section.items():
                        config_out.set(section_name, key, value)
                        config_ret.set(section_name, key, value)
                config_out.write(f)
                config_out = ConfigParser()
                f.write("#######################################\n")

        # modified_sections
        for section_name in modified_sections.keys():
            config_out.add_section(section_name)
            config_ret.add_section(section_name)

            section = modified_sections[section_name]
            for sub_key, value in section.items():
                # key_kind is either: added_keys, removed_keys, modified_keys, unmodified_keys
                if len(value) != 0:
                    config_out.set(section_name,  "# " + sub_key,
                                   TEXT_DISPLAYED[sub_key])
                    config_ret.set(section_name,  "# " + sub_key,
                                   TEXT_DISPLAYED[sub_key])

                    for kk, vv in value.items():
                        if sub_key == "modified_keys":
                            # it is written as "from", "to" keys
                            vv = vv["to"]
                        config_out.set(section_name, kk, vv)
                        config_ret.set(section_name, kk, vv)

            config_out.write(f)
            config_out = ConfigParser()

    return config_ret


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('mod_url')
    args = parser.parse_args()

    mod = Mod(args.mod_url)
    path_previous = mod.path_en / "locale.cfg"
    path_new = mod.path / "locale/fr/locale.cfg"
    # path_new = mod.download_locale_en()

    diff = compare_configs(path_previous, path_new)
    format_output(diff, mod)
