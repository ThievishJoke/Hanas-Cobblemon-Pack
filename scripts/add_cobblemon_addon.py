# for cobblemon addons that are both data packs and resource packs

import os
import sys


if len(sys.argv) != 2:
    print("Usage: python add_cobblemon_addon.py <target_project>")
    sys.exit(1)
target_project = sys.argv[1]

os.system(f"packwiz mr add {target_project} --meta-folder datapacks")
os.system(f"packwiz mr add {target_project} --meta-folder resourcepacks")

