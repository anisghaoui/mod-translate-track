

def format_output(config, mod):

    add_sections = config["added_sections"]
    removed_sections = config["removed_sections"]
    common_sections = config["common_sections"]

    # Write the file section by section starting with the common ones
