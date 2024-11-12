import argparse
from Mod import Mod
import configparser


def parse_config(path_or_string):
    cfg = configparser.ConfigParser()
    cfg.read(path_or_string)
    return {section: dict(cfg.items(section))
            for section in cfg.sections()}


def compare_configs(cfg_previous: str, cfg_new: str):
    cfg_previous = parse_config(cfg_previous)
    cfg_new = parse_config(cfg_new)

    # Find sections or keys that have changed, were added, or removed
    added_sections = cfg_new.keys() - cfg_previous.keys()
    removed_sections = cfg_previous.keys() - cfg_new.keys()
    common_sections = cfg_previous.keys() & cfg_new.keys()

    # Store differences
    diff_result = {
        "added_sections": {section: cfg_new[section] for section in added_sections},
        "removed_sections": {section: cfg_previous[section] for section in removed_sections},
        "modified_sections": {}
    }

    # Compare keys within common sections
    for section in common_sections:
        added_keys = cfg_new[section].keys() - cfg_previous[section].keys()
        removed_keys = cfg_previous[section].keys() - cfg_new[section].keys()
        modified_keys = {
            key for key in cfg_previous[section].keys() & cfg_new[section].keys()
            if cfg_previous[section][key] != cfg_new[section][key]
        }
        unmodified_keys = {
            key for key in cfg_previous[section].keys() & cfg_new[section].keys()
            if cfg_previous[section][key] == cfg_new[section][key]
        }
        # If any exists, create a dict
        if added_keys or removed_keys or modified_keys or unmodified_keys:
            diff_result["modified_sections"][section] = {
                "added_keys": {key: cfg_new[section][key] for key in added_keys},
                "removed_keys": {key: cfg_previous[section][key] for key in removed_keys},
                "modified_keys": {
                    key: {"from": cfg_previous[section][key],
                          "to": cfg_new[section][key]}
                    for key in modified_keys
                },
                "unmodified_keys": {key: cfg_previous[section][key] for key in unmodified_keys},
            }

    return diff_result


def compare_configs(cfg_previous: str, cfg_new: str):
    cfg_previous = parse_config(cfg_previous)
    cfg_new = parse_config(cfg_new)

    # Find sections or keys that have changed, were added, or removed
    added_sections = cfg_new.keys() - cfg_previous.keys()
    removed_sections = cfg_previous.keys() - cfg_new.keys()
    common_sections = cfg_previous.keys() & cfg_new.keys()

    # Store differences
    diff_result = {
        "added_sections": {section: cfg_new[section] for section in added_sections},
        "removed_sections": {section: cfg_previous[section] for section in removed_sections},
        "common_sections": {}
    }

    # Compare keys within common sections
    for section in common_sections:
        added_keys = cfg_new[section].keys() - cfg_previous[section].keys()
        removed_keys = cfg_previous[section].keys() - cfg_new[section].keys()
        modified_keys = {
            key for key in cfg_previous[section].keys() & cfg_new[section].keys()
            if cfg_previous[section][key] != cfg_new[section][key]
        }
        unmodifed_keys = {
            key for key in cfg_previous[section].keys() & cfg_new[section].keys()
            if cfg_previous[section][key] == cfg_new[section][key]
        }

        # If any exists, create a dict
        if added_keys or removed_keys or modified_keys or unmodifed_keys:
            diff_result["common_sections"][section] = {
                "added_keys": {key: cfg_new[section][key] for key in added_keys},
                "removed_keys": {key: cfg_previous[section][key] for key in removed_keys},
                "modified_keys": {
                    key: {"from": cfg_previous[section][key],
                          "to": cfg_new[section][key]}
                    for key in modified_keys
                },
                "unmodifed_keys": {key: cfg_previous[section][key] for key in unmodifed_keys},
            }

    return diff_result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('mod_url')
    args = parser.parse_args()

    mod = Mod(args.mod_url)
    path_previous = mod.path_en / "locale.cfg"
    # path_new = mod.download_locale_en()
    diff = compare_configs(path_previous, path_previous)
    from pprint import pprint
    pprint(diff)
