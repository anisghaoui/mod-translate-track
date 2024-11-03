import requests
import os
import sys
import argparse

RAW_PRE = "https://raw.githubusercontent.com/"

def init_mod(mod_repo_url, overwrite=False):
    res = mod_repo_url.split("/")
    mod_name = res[-1]
    owner= res[-2]

    # check if mod locale folder exists:
    mod_path = "mods_locale/" + mod_name
    if os.path.exists(mod_path) and not overwrite:
        raise FileExistsError("Mod folder already exists in repository. Use --f to overwrite.")
    
    os.makedirs(mod_path + "/locale/en",exist_ok=overwrite)
    os.makedirs(mod_path +"/locale/fr",exist_ok=overwrite)
    
    # download the English version
    req = requests.get(f"{RAW_PRE}/{owner}/{mod_name}/refs/heads/main/locale/en/locale.cfg")
    if req.status_code != 200:
        raise ConnectionError('Request failed. CHeck provided URL')
    config_str= req.content.decode(req.encoding)
    
    with open(mod_path+"/locale/en/locale.cfg", "w",encoding = req.encoding) as f:
        f.write(config_str)
    
    print(f"Locale File downloaded for {mod_name} by {owner}. Ready to translate!")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('mod_url')
    parser.add_argument('--f', "--overwrite", action="store_true", default=False)
    args = parser.parse_args()
    init_mod(args.mod_url,args.f)
