from setuptools import setup, find_packages
import os


# Utility function to read the README file.
# Used for the long_description. It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='djnext',
    version='0.0.1',
    description='Django-NextJS Isomorphic UI dev with Decorator pattern',
    author='James Pic',
    author_email='jamespic@gmail.com',
    url='https://git.yourlabs.org/oss/djnext',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    long_description=read('README.rst'),
    license='MIT',
    keywords='django nextjs',
    install_requires=[
        'django-appwatch',
        'requests',
        'watchdog',
    ],
    tests_require=['tox'],
    extras_require=dict(
        dev=[
          'django>=2.0',
          'django12factor',
          'dj-static',
          'crudlfap',
        ],
    ),
    entry_points={
        'console_scripts': [
            'djnext = djnext_example.manage:main',
        ],
    },
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
