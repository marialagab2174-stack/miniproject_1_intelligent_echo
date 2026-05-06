from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='miniproject_1_intelligent_echo',
            executable='cmd_parser.py',
            output='screen'
        ),
        # Node Logger simulé pour enregistrer les sorties
        Node(
            package='miniproject_1_intelligent_echo',
            executable='intelligent_echo.py',
            name='echo_logger',
            remappings=[('input_topic', 'cmd_text')]
        )
    ])
