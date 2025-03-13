import os
import sys
import json
import re


# Adds projects from a Modrinth index file with packwiz
def main():
    if 2 != len(sys.argv):
        print("Usage: python mods_from_index.py <url_list_file>")
        sys.exit(1)
    index_file = sys.argv[1]
    with open(index_file, "r") as f:
        index = json.load(f)
        projects = index["files"]
        url_pattern = r"https://cdn\.modrinth\.com/data/(?P<projectId>[A-Za-z0-9]{8})/versions/(?P<versionId>[A-Za-z0-9]{8})/"
        for project in projects:
            download_url = project["downloads"][0]
            match = re.match(url_pattern, download_url)
            if match:
                project_id = match.group("projectId")
                version_id = match.group("versionId")
                print(f"Adding project from https://modrinth.com/project/{project_id}/{version_id}")
                os.system(f"packwiz mr add -y --project-id {project_id} --version-id {version_id}")
        f.close()

if "__main__" == __name__:
    main()
