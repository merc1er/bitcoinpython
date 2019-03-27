from setuptools import find_packages, setup

with open('bitcoinpython/__init__.py', 'r') as f:
    for line in f:
        if line.startswith('__version__'):
            version = line.strip().split('= ')[1].strip("'")
            break

setup(
    name='bitcoinpython',
    version=version,
    description='Bitcoin Cash for Python',
    long_description=open('README.md', 'r').read(),
    author='Corentin Mercier',
    author_email='corentin@mercier.link',
    maintainer='Corentin Mercier',
    maintainer_email='corentin@mercier.link',
    url='https://github.com/buymercier/bitcoinpython',
    download_url='https://github.com/buymercier/bitcoinpython/tarball/{}'.format(version),
    license='MIT',

    keywords=[
        'bitcoin',
        'bitcoincash',
        'cryptocurrency',
        'payments',
        'tools',
        'wallet',
    ],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],

    install_requires=['coincurve>=4.3.0', 'requests', 'cashaddress==1.0.4'],
    extras_require={
        'cli': ('appdirs', 'click', 'privy', 'tinydb'),
        'cache': ('lmdb', ),
    },
    tests_require=['pytest'],

    packages=find_packages(),
    entry_points={
        'console_scripts': (
            'bitcoinpython = bitcoinpython.cli:bitcoinpython',
        ),
    },
)
