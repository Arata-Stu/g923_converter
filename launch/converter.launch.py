from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='g923_converter',
            executable='gear_change_node',
            name='gear_change_node'
        ),
        Node(
            package='g923_converter',
            executable='handle_converter_node',
            name='handle_converter_node'
        ),
        Node(
            package='g923_ros2_driver',
            executable='g923_driver_node',
            name='g923_driver_node',
            arguments=['/dev/input/event6']
        ),
    ])
