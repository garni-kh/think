from setuptools import setup

setup(
    name='con',
    version='0.01',
    py_modules=['con'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        con=con:cli
    ''',
)
