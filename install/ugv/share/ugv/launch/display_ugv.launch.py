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

    urdf_file = os.path.join(package_dir, 'urdf', 'ugv.urdf')

        # Read the URDF file contents
    with open(urdf_file, 'r') as urdf:
        robot_description = urdf.read()


    return LaunchDescription([

        # RViz Node for visualization
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz',
            output='screen',
            arguments=['-d', os.path.join(package_dir, 'rviz','ugv_config.rviz')]
        ),

                 # Joint State Publisher
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher_gui',
            output='screen'
        ),

        # Robot State Publisher Node
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': robot_description}] # :open(urdf_file).open() ;; Command(['xacro ', xacro_file])
        )

    ])
