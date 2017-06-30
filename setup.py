from setuptools import setup
from csv2md.__init__ import __version__

setup(
    name = 'csv2md',
    version = __version__,
    description = 'Python port of CsvToMarkdownTable for nodejs by donatj',
    url = 'https://github.com/olegsson/tilebeard',
    author = 'olegsson',
    author_email = 'luka.olegsson@gmail.com',
    license = 'MIT',
    packages = ['csv2md'],
    zip_safe = True,
)
