import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command

def generate_launch_description():
    # Define the path to the Xacro file
    xacro_file = os.path.join(
        get_package_share_directory('ugv'),
        'urdf',
        'ugv.xacro')

    # Command to convert the Xacro file to URDF
    robot_description = {'robot_description': Command(['xacro ', xacro_file])}

    # Launch the robot_state_publisher node
    rsp_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[robot_description]
    )

    # Launch RViz to visualize the robot
    rviz_config_file = os.path.join(get_package_share_directory('ugv'), 'rviz', 'display.rviz')

    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', rviz_config_file],
        parameters=[robot_description]
    )

    return LaunchDescription([rsp_node, rviz_node])
