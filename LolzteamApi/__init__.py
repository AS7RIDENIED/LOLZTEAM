def auto_update():
    from importlib.metadata import version
    import requests
    from bs4 import BeautifulSoup
    current_version = version('LolzteamApi')
    response = requests.get("https://pypi.org/project/LolzteamApi/")
    newest_version = BeautifulSoup(response.text, 'html.parser').select(
        selector="#content > div.banner > div > div.package-header__left > h1")[0].text.replace("LolzteamApi",
                                                                                                "").replace(" ",
                                                                                                            "").replace(
        "\n", "")
    if current_version != newest_version:
        print(f"Updating LolzteamApi from {current_version} to {newest_version}")
        import subprocess
        import sys
        import importlib
        subprocess.call("pip install LolzteamApi --upgrade", shell=True, stdout=subprocess.DEVNULL,
                        stderr=subprocess.STDOUT)
        importlib.reload(sys.modules["LolzteamApi"])
        print(f"LolzteamApi updated to {newest_version}")

try:
    auto_update()
except:
    pass
from .LolzteamApi import LolzteamApi, Types
