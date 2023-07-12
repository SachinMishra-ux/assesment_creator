import setuptools

try:
   import pypandoc
   long_description = pypandoc.convert_file('README.md', 'rst')
except(IOError, ImportError):
   long_description = open('README.md').read()

__version__ = "0.0.3"

REPO_NAME = "assesment_creator"
AUTHOR_USER_NAME = "SachinMishra-ux"
SRC_REPO = "assesment_creator"
AUTHOR_EMAIL = "sachin19566@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="assesment creator python package",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)