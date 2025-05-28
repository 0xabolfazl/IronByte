from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ironbyte",
    version="1.0.0",
    author="0xAbolfazl",
    author_email="0xAbolfazl@example.com",
    description="Python code obfuscation tool for protecting intellectual property",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/0xabolfazl/ironbyte",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Security",
    ],
    python_requires=">=3.6",
    keywords="obfuscation security code-protection",
)