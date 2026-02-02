from setuptools import setup, find_packages

Hypen="-e ."
def get_requirements(file_path):
    requirements=[]
    with open('requirements.txt') as file:
        requirements=file.readlines()
        requirements=[req.replace("/n"," ") for req in requirements]
    
    if Hypen in requirements:
        requirements.remove(Hypen)
    return requirements


setup(
    name="MLPJ",
    version="0.0.1",
    author="Ajay Mudliyar",
    author_email="ajaymudliyar66@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    
)