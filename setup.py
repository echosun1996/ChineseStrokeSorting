import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Chinese_Stroke_Sorting-echosun",
    version="0.0.1",
    author="echosun",
    author_email="echosun1996@126.com",
    description="Chinese Name Sort by Stroke Order",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/echosun1996/ChineseStrokeSorting",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)