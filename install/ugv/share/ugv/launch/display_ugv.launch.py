from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, FindPackageShare
import os

def generate_launch_description():
    # Define the path to the Xacro file
    xacro_file = os.path.join(
        FindPackageShare('ugv'), 'urdf', 'ugv.xacro'  # Update with your actual package name and Xacro file name
    )

    # Define the path to the RViz configuration file
    rviz_config_file = os.path.join(
        FindPackageShare('ugv'), 'rviz', 'display.rviz'  # Update with your actual package name and RViz config file name
    )

    return LaunchDescription([
        # Load the robot description from the Xacro file
        DeclareLaunchArgument(
            'robot_description',
            default_value=xacro_file,
            description='Path to robot xacro file'
        ),

        # Start the Xacro node to process the Xacro file
        Node(
            package='xacro',
            executable='xacro',
            name='xacro',
            output='screen',
            parameters=[{
                'robot_description': LaunchConfiguration('robot_description')
            }]
        ),

        # Start RViz with the specified configuration
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz',
            output='screen',
            arguments=['-d', rviz_config_file]
        ),
    ])
