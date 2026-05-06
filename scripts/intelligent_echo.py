#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from miniproject_1_intelligent_echo.srv import GetEchoStats
import time

class IntelligentEcho(Node):
    def __init__(self):
        super().__init__('intelligent_echo')
        
        # Paramètres
        self.declare_parameter('echo_mode', 'UPPERCASE') # Modes: UPPERCASE, REVERSE, CYBER
        
        # Pub/Sub
        self.subscription = self.create_subscription(String, 'input_topic', self.listener_callback, 10)
        self.publisher_ = self.create_publisher(String, 'output_topic', 10)
        
        # Service
        self.srv = self.create_service(GetEchoStats, 'get_echo_stats', self.get_stats_callback)
        
        # Stats internes
        self.count = 0
        self.start_time = time.time()
        self.last_msg = ""

    def listener_callback(self, msg):
        mode = self.get_parameter('echo_mode').get_parameter_value().string_value
        content = msg.data
        
        # Transformation intelligente
        if mode == 'UPPERCASE':
            processed = content.upper()
        elif mode == 'REVERSE':
            processed = content[::-1]
        elif mode == 'CYBER':
            processed = f"[PROCESSED_BY_MARIA]: {content.replace('e', '3').replace('a', '4')}"
        else:
            processed = content

        self.count += 1
        self.last_msg = processed
        
        # Envoi
        echo_msg = String()
        echo_msg.data = processed
        self.publisher_.publish(echo_msg)
        self.get_logger().info(f'[{mode}] Echoing: {processed}')

    def get_stats_callback(self, request, response):
        response.total_messages = self.count
        response.average_latency = (time.time() - self.start_time) / (self.count if self.count > 0 else 1)
        response.last_message_processed = self.last_msg
        return response

def main():
    rclpy.init()
    node = IntelligentEcho()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
