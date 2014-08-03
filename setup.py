from distutils.core import setup

setup(
    name='dnspython-lookup',
    version='0.1.11',
    author='Joubin Jabbari',
    author_email='joubin.j@gmail.com',
    packages=['dnspython'],
    url='https://pypi.python.org/pypi/dnspython-lookup/',
    license='LICENSE.txt',
      entry_points={
          'console_scripts':
              ['release = dnspython:main',
               ]},
    description='Check dns entries across the world',
    long_description=open('README.txt').read(),
    install_requires=[],
)
