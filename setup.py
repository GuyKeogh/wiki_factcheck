from setuptools import setup, find_packages

setup(
    name="wiki_verify",
    version="1.0",
    description="""Uses natural-language processing to help fact-check information in English-language Wikipedia
                   articles by comparing information in the article against the text of its citations.""",
    author="Guy Keogh",
    url="https://github.com/GuyKeogh/wiki_verify",
    packages=find_packages(where='src', exclude=['test']),
    install_requires=["nltk", "requests", "beautifulsoup4", "wikitextparser"],
)
