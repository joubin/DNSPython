from distutils.core import setup

import setuptools


setup(
    name='dnspython',
    version='0.7.30',
    author='Joubin Jabbari',
    author_email='joubin.j@gmail.com',
    url="https://github.com/joubin/DNSPython",
    license='LICENSE.txt',
      entry_points={
          'console_scripts':
              ['dnspython= dnspython.main:main']},
    description='Check dns entries across the world. In short, if you move your server from one IP to another, you can check to see when most of the dns servers in the world have update their results.',
    long_description="Test",
    long_description_content_type="text/markdown",
    packages=['dnspython'],
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
