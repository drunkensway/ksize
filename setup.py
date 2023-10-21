from setuptools import setup

setup(
    name='ksize',
    version='0.1.3',
    packages=['ksize'],
    install_requires=[
        # List your dependencies here
    ],
    entry_points={
        'console_scripts': [
            'kafka_install=ksize.kafka_install:kafka_install'
        ]
    }
)
