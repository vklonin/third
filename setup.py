from setuptools import setup, find_packages

setup(
    name='TestAutomationFramework',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'selene==2.0.0rc2',
        'pytest==7.4.0',
        'allure-pytest==2.13.2'
    ]
)
