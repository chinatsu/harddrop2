from setuptools import setup

setup(
    name='harddrop',
    packages=['harddrop'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-bootstrap',
        'flask-nav',
        'sqlalchemy',
        'flask-sqlalchemy',
        'flask-login',
        'wtforms',
        'passlib',
        'mysql-connector'
    ],
)
