import setuptools

with open("README.md","r",encoding="utf-8")as f:
    long_description = f.read()
    
    
__version__="0.0.0"

REPO_NAME="anshi78"
AUTHOR_USER_NAME="TextSummarization"
SRC_REPO="textSummarization"
AUTHOR_EMAIL="rastogianshika05@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app"),
long_description=long_description,
long_description_content="text/markdown",
url=f"https://github.com/anshi78/TextSummarization",
project_urls={
    "Bug Tracker":f"https://github.com/anshi78/TextSummarization/issues",
},
package_dir={"":"src"},
packages=setuptools.find_packages(where="src")
    