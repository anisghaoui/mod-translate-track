import re
from compare_tools import Mod

def dump_faulty_urls(urls):
    for url in urls:
        print(f"Faulty url detected: {url}. Rejecting track.")

def check_urls(urls: list):
    pattern = "https://github.com/*"
    sanes = [url for url in urls if re.match(pattern, url)] 
    dump_faulty_urls(set(urls) - set(sanes))
    return sanes
            

def main():
    with open("mod_list.txt", "r") as f:
        urls = f.read().splitlines() 
        urls = check_urls(urls)
        
        for url in urls:
            mod = Mod.Mod(url)


if __name__ == "__main__":
    main()