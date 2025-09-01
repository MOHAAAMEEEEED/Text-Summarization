import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()





setuptools.setup(
    name="Text-Summarizer",
    version="0.0.0",
    author="Mohamed Walid",
    author_email="mo.waleedddd@gmail.com",
    description="A package for text summarization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MOHAAAMEEEEED/Text-Summarization",
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
