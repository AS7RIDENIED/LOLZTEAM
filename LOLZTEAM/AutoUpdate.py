from importlib.metadata import version
import httpx
import os

current_version = version("LOLZTEAM")
response = httpx.get("https://pypi.org/pypi/LOLZTEAM/json")
newest_version = response.json()["info"]["version"]
if current_version != newest_version:
    venv_folder = None
    for root, dirs, files in os.walk(os.curdir):
        if all(folder in dirs for folder in ["Lib", "Scripts", "Include"]):
            if "pyvenv.cfg" in files:
                venv_folder = root
                print(f"Found venv - {venv_folder}")
                break
    print(f"Updating LOLZTEAM from {current_version} to {newest_version}")
    import subprocess
    import sys
    from importlib import reload
    if venv_folder:
        subprocess.call(
            f"{venv_folder}\\Scripts\\pip install LOLZTEAM --upgrade",
            shell=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.STDOUT,
        )
    else:
        subprocess.call(
            "pip install LOLZTEAM --upgrade",
            shell=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.STDOUT,
        )
        reload(sys.modules["LOLZTEAM"])
        print(f"LOLZTEAM updated to {newest_version}")
