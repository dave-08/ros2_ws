from launch import LaunchDescription
from launch.substitutions import Command
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    package_name = 'ugv'  # Replace with your package name
    xacro_file = os.path.join(
        get_package_share_directory(package_name),
        'urdf',
        'ugv.xacro'
    )

    # Convert the xacro file to URDF on the fly
    robot_description = Command(['xacro ', xacro_file])

    return LaunchDescription([
        # Launch Ignition Gazebo
        ExecuteProcess(
            cmd=['ign', 'gazebo', '-r', 'empty.sdf'],  # You can change 'empty.sdf' to a custom world
            output='screen'
        ),

        # Start the bridge to forward /cmd_vel from ROS2 to Ignition
        Node(
            package='ros_ign_bridge',
            executable='parameter_bridge',
            arguments=[
                '/cmd_vel@geometry_msgs/msg/Twist@ignition.msgs.Twist'
            ],
            output='screen'
        ),

        # Spawn UGV Model in Ignition Gazebo
        Node(
            package='ros_ign_gazebo',
            executable='create',
            arguments=['-name', 'ugv', '-file', robot_description],
            output='screen'
        ),
    ])
