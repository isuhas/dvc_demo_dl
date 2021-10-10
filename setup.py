from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.1",
    author="Suhas",
    description="A small package for dvc dl pipeline demo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/isuhas/dvc_demo_dl",
    author_email="suhaspote8@gmail.com",
    packages=["src"],
    python_requires=">=3.7",
    install_requires=[
        'dvc',
        'tensorflow==2.5.0',
        'matplotlib==3.4.3',
        'pandas==1.1.5',
        'numpy==1.19.5',
        'PyYAML==5.4.1',
        'tqdm==4.62.3',
        'boto3==1.18.58'
    ]
)