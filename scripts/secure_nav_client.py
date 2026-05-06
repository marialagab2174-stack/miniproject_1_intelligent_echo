#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from nav2_msgs.action import NavigateToPose

class SecureNavClient(Node):
    def __init__(self):
        super().__init__('secure_nav_client')
        self._action_client = ActionClient(self, NavigateToPose, 'navigate_to_pose')

    def go_to(self, x, y):
        goal_msg = NavigateToPose.Goal()
        goal_msg.pose.pose.position.x = x
        goal_msg.pose.pose.position.y = y
        
        self.get_logger().info('Attente du serveur de navigation...')
        self._action_client.wait_for_server()
        
        # ENVOI NON-BLOQUANT
        self._send_goal_future = self._action_client.send_goal_async(goal_msg)
        self._send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().error('Goal rejeté !')
            return
        self.get_logger().info('Goal accepté, navigation asynchrone en cours...')
