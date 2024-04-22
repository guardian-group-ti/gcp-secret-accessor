import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open('requirements.txt', 'r', encoding="utf-8") as fp:
    contents = fp.read()
    requirements = list(map(str.strip, contents.split('\n')))

setuptools.setup(
    name='gcp-secret-accessor',
    version='0.0.4',
    author='Nirvan Sharma',
    author_email='nirvan.sharma@myguardiangroup.com',
    description='Public GCP Secret Accessor',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/guardian-group-ti/gcp-secret-accessor',
    project_urls={
        "Bug Tracker": "https://github.com/guardian-group-ti/gcp-secret-accessor/issues"
    },
    license='MIT',
    packages=['gcp_secret_accessor'],
    install_requires=requirements
)
