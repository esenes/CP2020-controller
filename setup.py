from setuptools import setup, find_packages

# long description
with open("README.md", 'r', encoding='utf-8') as fh:
    long_description = fh.read()

# requirements
REQUIREMENTS = ['prologix_gpib_ethernet']

# more details
CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.6',
]

setup(name='CP2020-controller',
    version='1.0.0',
    description='A python wrapper for using Flann Microwave CP2020 controllers with Prologix GPIB to ethernet adapters',
    url='https://github.com/esenes/CP2020-controller',
    author='Eugenio Senes',
    author_email='a@b.ch',
    license='MIT',
    packages=find_packages(),
    classifiers=CLASSIFIERS,
    install_requires=REQUIREMENTS,
    dependency_links=['git+git://github.com/nelsond/prologix-gpib-ethernet.git'],
    keywords='GPIB flann attenuator phase-shifter wrapper',
)
