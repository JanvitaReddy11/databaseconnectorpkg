from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

__version__ = "0.0.4"
REPO_NAME = "databaseconnectorpkg"
PKG_NAME = "Mongodb Connector"
AUTHOR_USER_NAME = "JanvitaReddy11"
AUTHOR_EMAIL = "janvita11@tamu.edu"

setup(
    name=PKG_NAME,  # Name of package
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for connecting with database",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"": "src"},
    packages=find_packages(where="src")
)
