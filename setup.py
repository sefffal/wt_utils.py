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
    packages='wt_utils',
    include_package_data=True,
    py_modules=['wt_utils']
    # ...
)
