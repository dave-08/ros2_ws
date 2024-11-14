from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Launch the UGV Control Node
        Node(
            package='ugv',           # Make sure this is your package name
            executable='test_script',  # This should be the exact name of the script (without .py)
            output='screen',
        ),
    ])
