from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [requirement.replace("\n","") for requirement in requirements if requirement != '-e .\n']
    return requirements

setup(
    name = "Loan Status Prediction",
    version = '0.0.1',
    author = "Ann Mary Shaju",
    author_email = "shajuannmary01@gmail.com",
    packages = find_packages(),
    install_requirements = get_requirements("requirements.txt")

)
