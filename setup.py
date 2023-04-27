from setuptools import setup, find_packages


setup(
    name='flet_multi_page',
    version='1.2',
    author='SKbarbon',
    description='A tool of creating new pages with flet library.',
    long_description="until now, flet v0.6 does not support multi pages.\n With this tool, you can start new pages on the same script without the need of creating new `app` class.\n visit the github repo for more: [github](https://github.com/SKbarbon/flet_multi_page)",
    url='https://github.com/SKbarbon/flet_multi_page',
    install_requires=["flet"],
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows"
    ],
)