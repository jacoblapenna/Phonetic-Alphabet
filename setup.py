from setuptools import find_packages
from setuptools import setup

setup(
    name="phonetic_alphabet_app",
    version="1.0.0",
    url="",
    license="BSD",
    maintainer="Jacob Lapenna",
    maintainer_email="me@jacoblapenna.com",
    description="An app to help study the phonetic alphabet.",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["flask"],
)
