import io

from setuptools import find_packages, setup

with io.open('README.rst', 'rt', encoding='utf8') as f:
    readme = f.read()

setup(
    name='parsons',
    version='0.1.0',
    url='http://parsons.problemsolving.io',
    license='MIT',
    maintainer='Shlomi Hod',
    maintainer_email='shlomi.hod@uni-potsdam.de',
    description='The basic blog app built in the Flask tutorial.',
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'flask_sqlalchemy',
        'python-dotenv',
        'psycopg2',
    ],
    #    extras_require={
    #        'test': [
    #            'pytest',
    #            'coverage',
    #        ],
    #   },
)
