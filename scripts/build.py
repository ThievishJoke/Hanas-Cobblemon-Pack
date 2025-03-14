import os
import shutil
from pathlib import Path

# Path to packwiz's default resource pack directory, since
# we're unable to configure it.
pw_resource_pack_dir = Path("resourcepacks")
pw_data_pack_dir = Path("datapacks")
openloader_pack_dir = Path("config/openloader/packs")

def copy_resource_packs():
    print("Copying resource packs...\n")
    for file in pw_resource_pack_dir.iterdir():
        print(f"Copying `{file.name}` to `{openloader_pack_dir}`")
        shutil.copy(file, openloader_pack_dir / file.name)
    print("Done copying resource packs.")

def copy_data_packs():
    print("Copying data packs...\n")
    for file in pw_data_pack_dir.iterdir():
        print(f"Copying `{file.name}` to `{openloader_pack_dir}`")
        shutil.copy(file, openloader_pack_dir / file.name)
    print("Done copying data packs.")


def build():
    openloader_pack_dir.mkdir(parents=True, exist_ok=True)

    copy_resource_packs()
    copy_data_packs()

    print("Refreshing packwiz and exporting modpack...")

    os.system("packwiz refresh")
    os.system("packwiz mr export")

    print("Cleaning up...")

    shutil.rmtree(openloader_pack_dir)

    os.system("packwiz refresh")

    print("Done! :3")
        

if __name__ == '__main__':
    build()
