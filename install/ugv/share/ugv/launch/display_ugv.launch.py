import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command, PathJoinSubstitution

def generate_launch_description():
    # Get the package directory
    package_dir = get_package_share_directory('ugv')

    # Set the path to the Xacro file
    xacro_file = os.path.join(package_dir, 'urdf', 'ugv.xacro')

    return LaunchDescription([
        # Robot State Publisher Node
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{
                'robot_description': Command([
                    'xacro ', xacro_file
                ])
            }]
        ),

        # RViz Node for visualization
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz',
            output='screen',
            arguments=['-d', os.path.join(package_dir, 'rviz')]
        )
    ])
