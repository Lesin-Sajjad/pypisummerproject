from setuptools import setup, find_packages
import codecs
import os

 #here = os.path.abspath(os.path.dirname(__file__))

 #with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
 #   long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Basic Mathematical operations.'

# Setting up
setup(
    name="mathematical_operations",
    version=VERSION,
    author="Lesin (Student at iiit banglore)",
    author_email="<lesin280204@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'basic math', 'iiit banglore'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)