from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """
    This function will return the list of requirements

    """
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
    
    # Removing any extra spaces and new line characters
    requirements = [req.strip() for req in requirements if req.strip()]
    
    # If '-e .' is present, remove it
    if '-e .' in requirements:
        requirements.remove('-e .')
    
    return requirements

setup(
    name='ML-PROJECT-1',
    version='0.1.0',
    author='SURYAVHI DAS',
    author_email='dassuryavhi704@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
      
    
)