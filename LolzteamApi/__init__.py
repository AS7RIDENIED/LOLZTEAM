"""
LolzteamApi it's library that contains all the methods of the Lolzteam API (Market/Forum/Antipublic)

You can find full documentation here -> https://github.com/AS7RIDENIED/Lolzteam_Python_Api
"""
def auto_update():
    from importlib.metadata import version
    import requests
    current_version = version('LolzteamApi')
    response = requests.get("https://pypi.org/pypi/lolzteamapi/json")
    newest_version = response.json()["info"]["version"]
    if current_version != newest_version:
        print(f"Updating LolzteamApi from {current_version} to {newest_version}")
        import subprocess
        import sys
        from importlib import reload
        subprocess.call("pip install LolzteamApi --upgrade", shell=True, stdout=subprocess.DEVNULL,
                        stderr=subprocess.STDOUT)
        reload(sys.modules["LolzteamApi"])
        print(f"LolzteamApi updated to {newest_version}")

try:
    auto_update()
except Exception as e:
    pass
finally:
    from .LolzteamApi import LolzteamApi
    from .AntipublicApi import AntipublicApi
    from .DelaySynchronizer import  DelaySynchronizer
    from . import Types
