from setuptools import setup,find_packages
with open("README.md","r",encoding="utf-8") as file:
    tool_description=file.read()
setup(
    name="phonyARP",
    version='0.0.1',
    author="pk_the_hacker",
    author_email="",
    description=tool_description,
    packages=find_packages(),
    install_requires=[
        'art==6.4',
        'colorama==0.4.6',
        'scapy>=2.6.1',
        'requests>=2.32.3'
    ],
    entry_points={
        "console_scripts":[
            "phonyARP=phonyARP.phonyarp:main"
        ],
    }
)
