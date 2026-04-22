import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'scout_description'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # These two lines copy your launch and urdf folders to the install space
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
        (os.path.join('share', package_name, 'urdf'), glob(os.path.join('urdf', '*.urdf'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ROBE-313',
    maintainer_email='robotics@wvu.edu',
    description='Scout Rover Description Package',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
