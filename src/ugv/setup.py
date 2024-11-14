from setuptools import setup
import os
from glob import glob

package_name = 'ugv'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='your_email@example.com',
    description='UGV package with control node and URDF',
    license='Apache License 2.0',
    entry_points={
        'console_scripts': [
            'ugv_control = ugv.ugv_control:main',  # Link to Python control node
        ],
    },
    data_files=[
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*.urdf'))
    ],
)