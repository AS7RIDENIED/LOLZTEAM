import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = ["requests", "beautifulsoup4"]

setuptools.setup(
    name="LolzteamApi",
    version="1.0.14",
    author="AS7RID",
    author_email="as7ridwork@gmail.com",
    description="A library that contains all the methods of the Lolzteam API (Market/Forum)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AS7RIDENIED/Lolzteam_Python_Api",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=["Programming Language :: Python :: 3.11"],
    python_requires='>=3.6'
)
