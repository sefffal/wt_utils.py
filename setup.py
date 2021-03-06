from setuptools import setup

setup(
    name="wt_utils",
    version="0.1",
    description='Utilities for using python 3 in Jupyter notebooks',
    install_requires=[
        "ipywidgets",
    ],
    keywords='jupyter ipython notebook animation',
    author='Will Thompson',
    author_email='12wt9@queensu.ca',
    include_package_data=True,
    packages=['wt_utils']
    # ...
)
