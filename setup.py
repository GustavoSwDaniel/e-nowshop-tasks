from setuptools import setup, find_packages
import pathlib

HERE = pathlib.Path(__file__).parent

# The text of the README file

README = (HERE / "README.md").read_text()

VERSION = '0.0.2'
DESCRIPTION = 'e-nowshop-tasks'
LONG_DESCRIPTION = 'Package to manage tasks of e-nowshop'
#
# Setting up
setup( 
    name="enowshop-tasks",
    version=VERSION,
    author="GustavoSwDaniel",
    author_email="<gustavodanieldetoledo@gmail.com.com>",
    description=DESCRIPTION,
    long_description=README,
    license="MIT",
    url='https://github.com/GustavoSwDaniel/e-nowshop-tasks',
    install_requires=['celery[redis]'],
    keywords=['python'],
    packages=['async_tasks', 'async_tasks.tasks'],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
