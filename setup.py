import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="selenium-react-select",
    version="0.0.3",
    author="Karin Shaim",
    author_email="karins1010@gmail.com",
    description="package for react select : version 1 and 2",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/karins28/selenium-react-select",
    install_requires=['selenium'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
