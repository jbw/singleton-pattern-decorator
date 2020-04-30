import setuptools


with open("README.md", "r") as fh:
    LONG_DESC = fh.read()

setuptools.setup(
    name="singleton_pattern_decorator",
    version=1.0,
    author="Jason Watson",
    author_email="jbw@jbw.cc",
    description="Singleton decorator",
    url="https://github.com/jbw/singleton-pattern-decorator",
    long_description=LONG_DESC,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "License :: Public Domain",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
)
