import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Pyecharts-RedFox_pkg",
    version="1.0.1b",
    author="haitanghuadeng",
    author_email="author491609917@qq.com",
    description="Because RedFox is not really developed, but based on pyecharts",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://haitanghuadeng.github.io/Redfox/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license='MIT'
)
