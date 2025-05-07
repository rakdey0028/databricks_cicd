from setuptools import setup, find_packages

setup(
    name="framework_wheel",
    version="0.1",
    package_dir={"": "src"},
    packages=["cleaning"],
    include_package_data=True,
    install_requires=[
        'pyspark>=3.5.0',
    ],
)
