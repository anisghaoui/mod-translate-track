import re
from compare_tools import Mod, compare_configs, format_output

def dump_faulty_urls(urls):
    for url in urls:
        print(f"Faulty url detected: {url}. Rejecting track.")

def check_urls(urls: list):
    pattern = "https://github.com/*"
    sanes = [url for url in urls if re.match(pattern, url)] 
    dump_faulty_urls(set(urls) - set(sanes))
    return sanes
            

def main(language:str):
    with open("mod_list.txt", "r") as f:
        urls = f.read().splitlines() 
        urls = check_urls(urls)
        
        for url in urls:
            print(f"checking mod at: {url}")
            mod = Mod.Mod(url)
            print(mod.path_en/"locale.cfg")
            diff = compare_configs.compare_configs(mod.path_en/"locale.cfg", mod.path / "locale" / language/"locale.cfg")
            format_output.format_output(diff,mod)

if __name__ == "__main__":
    language = "fr"
    main(language)