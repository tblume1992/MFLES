# -*- coding: utf-8 -*-
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="MFLES",
    version="0.2.2",
    author="Tyler Blume",
    url="https://github.com/tblume1992/MFLES",
    long_description=long_description,
    # packages=['MFLES'],
    # package_dir={'MFLES':'src'},
    long_description_content_type="text/markdown",
    description = "Gradient boosted time series forecasting.",
    keywords = ['forecasting', 'time series', 'seasonality', 'trend'],
      install_requires=[           
                        'numpy',
                        'pandas',
                        'tqdm',
                        'numba',
                        'matplotlib'
                        ],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)


