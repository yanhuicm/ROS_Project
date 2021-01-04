from setuptools import setup

package_name = 'py_pubsub'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='yan',
    maintainer_email='yan@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                'talker = py_pubsub.publisher_member_function:main',
                'listener = py_pubsub.subscriber_member_function:main',
                'color = py_pubsub.subscriber_member_function_color:main',
                'depth = py_pubsub.subscriber_member_function_depth:main',
                'infra1 = py_pubsub.subscriber_member_function_infra1:main',
                'infra2 = py_pubsub.subscriber_member_function_infra2:main',
                'point = py_pubsub.subscriber_member_function_point:main',
                'timed = py_pubsub.subscriber_member_function_timed:main',
                'timed1 = py_pubsub.subscriber_member_function_timed1:main',
                'twice = py_pubsub.subscriber_member_function_twice:main',
                'onesensor = py_pubsub.subscriber_member_function_onesensor:main',
                'csvtojpeg = py_pubsub.csvtojpeg:main',
                'subscriber_mutually = py_pubsub.subscriber_mutually:main',
                'subscriber_reentrant = py_pubsub.subscriber_reentrant:main',
        ],
    },
)
