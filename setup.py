try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

__version__ = '1.0.0'
exec(open('t411api/version.py').read())

setup(
        name='t411api',
        version=__version__,
        description='Lightweight API for T411 (french torrent website)',
        long_description='Documentation is available `here <https://github.com/Xide/t411api/blob/master/README.md>`_',
        url='https://github.com/Xide/t411api',
        author='Germain Gau',
        author_email='germain.gau@gmail.com',
        license='THE BEER-WARE LICENSE',
        packages=['t411api'],
        zip_safe=False,
        test_suite='tests',
        install_requires=[
            'requests>=2.6'
        ],
        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.2",
            "Programming Language :: Python :: 3.3",
            "Programming Language :: Python :: 3.4",
            "Programming Language :: Python :: 3.5",
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Programming Language :: Python',
            'Operating System :: Unix'
        ]
)
