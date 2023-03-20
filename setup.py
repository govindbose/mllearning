from setuptools import find_packages, setup
from typing import List

def get_requirement(filename: str)->List[str]:
    """
        This function will return the list of requirements
    """
    requirements = []
    with open(filename) as file_obj:
        requirements = file_obj.readlines()
        requirements = [reg.replace("\n", "") for reg in requirements]
    
    return requirements
setup (
    name='mlproject',
    version='0.0.1',
    author='govind',
    author_email='govind@dqlabs.ai',
    packages=find_packages(),
    install_requires=get_requirement('requirements.txt')
)