from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
import os

def generate_launch_description():
    # Full path to the URDF/Xacro file
    ugv_model = os.path.join(
        os.getenv('HOME'), 'ros2_ws/src/ugv/urdf/ugv.urdf')

    return LaunchDescription([
        # Launch Gazebo with ROS plugins
        ExecuteProcess(
            cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_factory.so'],
            output='screen'
        ),

        # Spawn UGV in Gazebo
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=['-entity', 'ugv', '-file', ugv_model],
            output='screen'
        )
    ])
