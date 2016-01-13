from setuptools import setup

setup(
    name='livescrape',
    version='0.9.0',
    url='https://github.com/ondergetekende/python-livescrape',
    description='A toolkit to build pythonic web scraper libraries',
    author='Koert van der Veer',
    author_email='koert@ondergetekende.nl',
    py_modules=["livescrape"],
    install_requires=["lxml", "requests", "cssselect", "six"],
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
)
