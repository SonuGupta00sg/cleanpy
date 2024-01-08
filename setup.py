from setuptools import setup, find_packages

setup(
    name='cleanpy',
    version='0.1',
    packages=find_packages(),
    description='A simple data cleaning and preprocessing library',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Sonu Gupta',
    license='MIT',
    install_requires=[
        'pandas',
        'scikit-learn',
        'numpy',
        'scipy'
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest']
)