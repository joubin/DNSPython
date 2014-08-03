from distutils.core import setup

setup(
    name='dnspython-lookup',
    version='0.1.15',
    author='Joubin Jabbari',
    author_email='joubin.j@gmail.com',
    packages=['dnspython'],
    url='https://pypi.python.org/pypi/dnspython-lookup/',
    license='LICENSE.txt',
      entry_points={
          'console_scripts':
              ['dnspython-lookup = dnspython:main',
               ]},
    description='Check dns entries across the world. In short, if you move your server from one IP to another, you can check to see when most of the dns servers in the world have update their results.',
    long_description=open('README.txt').read(),
    install_requires=[],
)
