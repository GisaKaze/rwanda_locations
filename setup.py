from setuptools import setup, find_packages

setup(
    name='rwanda_locations',
    version='1.0',
    packages=find_packages(),
    install_requires=[],
    description='A package for working with Rwandan location metadata, including provinces, districts, sectors, cells, and villages.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Fredson Gisa Kaze',
    author_email='fredson.coder@gmail.com',
    url='https://github.com/gisakaze/rwanda_locations',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)