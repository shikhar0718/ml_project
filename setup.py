## used to update our own project in python pipy , it will be created as a package and we can deploy it in pipy

from setuptools import find_packages,setup
from typing import List

HYPHEN='-e.'
def get_requirement(file_path:str)->List[str]:
    # this function will return the list of requirements

    requirements=[]
    with open (file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPHEN in requirements:
            requirements.remove(HYPHEN)
    
    return requirements

setup(

    name='mlproject',
    version='0.0.1',
    author = 'shikhar',
    email ='shikhar0718@gmail.com',
    packages=find_packages(),
    # install_requires=['pamdas','numpy','seaborn']

    install_requires=get_requirement('requirements.txt')


)