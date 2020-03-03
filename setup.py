from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name='unichars',
    version='1.0',
    author='Jacob Komissar',
    description='Identify unicode characters',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/jirassimok/unichars',

    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],

    py_modules=['unichars'],

    python_requires='>=3.6',  # f-strings
)
