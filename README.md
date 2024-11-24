# Tracking Factorio Mod Translation

Many modders love writing code and barely adding anything but English localisation to it. This repository helping me keep up with translation of mods.

## How it works 
- A mod must be public on https://mods.factorio.com/
- A mod must be on Github.com
- Fork this repository
- Add the Github url to mod_list.txt
- Translate your mod by creating a new folder and file under `mods_locale/<mod_name>/<LANGUAGE>`
- Run the program once to ensure it is working via:
  - `python3 mod_translate_track.py github.com/author/modname pl` for exemple
- Commit and push
- Watch Github Actions trigger the pipeline
- Artefacts will hold `locale.cfg` file in the target translation language for each mod
- The LAGUANGE variable is hidden in the security > secrets > repository vars.

## Expected Output
```
[smart-inserters]
# modified_keys = These keys were updated since last update
welcome = [Smart Inserters] SOme test

[flying-text-smart-inserters]
# unmodified_keys = These keys were not changed
```
For any enhancement, please open a PR or an issue.
Be aware of mod licence.
