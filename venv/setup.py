from setuptools import find_packages,setup
from typing import List
HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function gives the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        [req.replace("\n","") for req in requirements]

setup(
    name='mlproject',
    version='0.0.1',
    author='Dennis',
    author_email='dennisheraaldv@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)