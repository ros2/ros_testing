from setuptools import find_packages
from setuptools import setup

setup(
    name='ros2test',
    version='0.8.1',
    packages=find_packages(exclude=['test']),
    install_requires=['ros2cli'],
    zip_safe=True,
    author='Michel Hidalgo',
    author_email='michel@ekumenlabs.com',
    maintainer='Michel Hidalgo',
    maintainer_email='michel@ekumenlabs.com',
    url='https://github.com/ros2/rostest/tree/master/ros2test',
    download_url='https://github.com/ros2/rostest/releases',
    keywords=[],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
    ],
    description='The test command for ROS 2 launch tests.',
    long_description="""\
This package provides the test command for ROS 2 launch tests.""",
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'ros2cli.command': [
            'launch = ros2test.command.test:TestCommand',
        ],
    }
)
