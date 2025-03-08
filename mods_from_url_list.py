import os
import sys

if "__main__" == __name__:
    if 2 != len(sys.argv):
        print("Usage: python mods_from_url_list.py <url_list_file>")
        sys.exit(1)
    url_list_file = sys.argv[1]
    with open(url_list_file, "r") as f:
        for line in f:
            url = line.strip()
            print(f"Downloading project from: {url}")
            os.system(f"packwiz mr add -y {url}")
        f.close()
    print("Done! :3")
    sys.exit(0)
