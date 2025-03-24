from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="communityone",
    version="1.1.1",
    author="CommunityOne",
    author_email="support@communityone.io",
    description="Official Python SDK for CommunityOne API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CommunityOne-io/communityone-sdk",
    project_urls={
        "Homepage": "https://communityone.io",
        "Documentation": "https://api.communityone.io/v1/documentation",
        "Bug Tracker": "https://github.com/CommunityOne-io/communityone-sdk/issues",
    },
    packages=find_packages(),
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.25.0",
        "aiohttp>=3.8.0",
    ],
)
