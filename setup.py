from setuptools import setup


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='PubMedExtraxtion',
    version='1.0',
    url='https://github.com/aparnathinks/PubMedExtraction',
    author='Aparna Subramanian',
    author_email='aparnas1@umbc.edu',
    description='Extract pubmed articles by PMID into json, pubmed or xml files'
)

