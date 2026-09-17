'''
This file helps in commiting the work done, basically to be more descriptive and simple: it reads the current snapshot pointer from version.txt, determines the next
snapshot version , creates the new manifest file with the help of manifest.py and then update the version.txt and point to the newest manifest.
'''
from pathlib import Path

VERSION_PATH = Path("data/snapshots/version.txt")

def get_current_snapshot():
    with open(VERSION_PATH,"r") as file:
        current_version = file.read().strip()
    return current_version

def commit_snapshot(new_manifest_path):
    with open(VERSION_PATH,"w") as file:
        file.write(new_manifest_path)
    return new_manifest_path


