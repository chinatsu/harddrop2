from setuptools import setup

setup(
    name='harddrop',
    packages=['harddrop'],
    include_package_data=True,
    install_requires=[
        'flask',
        'sqlalchemy',
        'flask-sqlalchemy',
        'flask-login',
        'mysql-connector'
    ],
)
