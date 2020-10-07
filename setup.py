import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="chinese-stroke-sorting",
    version="0.3.1",
    author="echosun",
    author_email="echosun1996@126.com",
    description="Chinese Name Sort by Stroke Order",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/echosun1996/ChineseStrokeSorting",
    packages=setuptools.find_packages(),
    package_data={'chinese_stroke_sorting': ['bh.txt']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Topic :: Text Processing"
    ],
    python_requires='>=3.5',
)