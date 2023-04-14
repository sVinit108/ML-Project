from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)-> List[str]:
    '''
    Returns the list of all requirements
    '''
    with open(file_path) as file:
        requirements=file.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='vinit',
    author_email='sharmavinit.1008@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)