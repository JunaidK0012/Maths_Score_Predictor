from setuptools import find_packages,setup
from typing import List

#this function will return the list of requirements
HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:  
    requirements= []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements




setup(
    name='ML_project',
    version='0.0.1',
    author='Junaid',
    author_email='khanj3991@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)