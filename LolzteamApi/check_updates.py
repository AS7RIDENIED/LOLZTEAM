from importlib.metadata import version
from bs4 import BeautifulSoup
import requests


def check_for_new_version():
    current_version = version('LolzteamApi')
    response = requests.get("https://pypi.org/project/LolzteamApi/")
    newest_version = BeautifulSoup(response.text, 'html.parser').select(
        selector="#content > div.banner > div > div.package-header__left > h1")[0].text.replace("LolzteamApi",
                                                                                                "").replace(" ",
                                                                                                            "").replace(
        "\n", "")
    if current_version != newest_version:
        print(f"Your version of LolzteamApi is outdated.")
        print(f"It has problems that have been solved in the new version")
        print(f"Your version:   {current_version}")
        print(f"Newest version: {newest_version}")
        print()
        print(f"You can update your package using the command below")
        print(f"pip install LolzteamApi --upgrade")
        print()
