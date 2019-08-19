from setuptools import find_packages
from setuptools import setup
from io import open

# read the contents of the README file
with open('README.md', encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='pixel-cnn',
    description='Pixel-cnn++',
    version='1.0.0',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Tim Salimans, Andrej Karpathy, Xi Chen, Diederik P. Kingma, and Yaroslav Bulatov',
    url='https://github.com/openai/pixel-cnn',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'six',
        'imageio',
        'numpy',
        'tensorflow',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    keywords='machine learning'
)
