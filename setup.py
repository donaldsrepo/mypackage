from setuptools import setup

setup(name='mypackagedstierman',
version='0.0.1',
url="https://github.com/donald/mypackagedstierman",
author="Donald Stierman",
author_email="stiermandon@gmail.com",
description='Testing installation of Package',
long_description_content_type="text/markdown",
classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
],
packages=['mypackage'],
zip_safe=False,
python_requires='>=3.6')
