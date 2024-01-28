from importlib.metadata import version
import requests

current_version = version("LOLZTEAM")
response = requests.get("https://pypi.org/pypi/LOLZTEAM/json")
newest_version = response.json()["info"]["version"]
if current_version != newest_version:
    print(f"Updating LOLZTEAM from {current_version} to {newest_version}")

    import subprocess
    import sys
    from importlib import reload

    subprocess.call(
        "pip install LOLZTEAM --upgrade",
        shell=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.STDOUT,
    )
    reload(sys.modules["LOLZTEAM"])
    print(f"LOLZTEAM updated to {newest_version}")
