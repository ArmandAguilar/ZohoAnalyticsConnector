from setuptools import setup
from sphinx.setup_command import BuildDoc
from os import path
cmdclass = {'build_sphinx': BuildDoc}

name = 'ZohoAnalyticsConnector'
keywords = 'zoho analytics connector'
version = '0.1.0'

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name=name,
    keywords=keywords,
    version=version,
    packages=['connector_analytics'],
    python_requires='>=3.6',
    install_requires=['requests'],
    setup_requires=['pytest-runner', 'wheel'],
    tests_require=["pytest"],
    classifiers=[
        'Development Status :: 1 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Zoho/Business',
    ],
    url='https://github.com/ArmandAguilar/ZohoAnalyticsConnector',
    license='MIT',
    author='Armando Aguilar L.',
    author_email='a.aguilar@gategeek.com',
    description='Zoho Analytics connector',
    long_description=long_description,
    cmdclass=cmdclass,
    command_options={
        'build_sphinx': {
            'project': ('setup.py', name),
            'version': ('setup.py', version),
            'release': ('setup.py', version),
            'source_dir': ('setup.py', 'docs')}},

)
