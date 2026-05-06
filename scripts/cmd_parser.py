#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from miniproject_1_intelligent_echo.srv import GetHistory, GetEchoStats
import re
import time
import os

class CmdParser(Node):
    def __init__(self):
        super().__init__('cmd_parser')
        # Publisher/Subscriber
        self.sub = self.create_subscription(String, 'cmd_text', self.cmd_callback, 10)
        self.pub = self.create_publisher(Twist, 'robot_response', 10)
        
        # Services
        self.srv_history = self.create_service(GetHistory, 'get_history', self.get_history_callback)
        self.srv_stats = self.create_service(GetEchoStats, 'get_echo_stats', self.get_stats_callback)
        
        # Data & Metrics
        self.history = []
        self.count = 0
        self.start_time = time.time()
        self.last_msg = ""
        self.log_file = "robot_commands.log"
        
        self.get_logger().info("✅ Robot Écho Intelligent (MAX) prêt sur Dell Latitude.")

    def cmd_callback(self, msg):
        raw_text = msg.data.lower().strip()
        twist = Twist()
        valid = False
        self.count += 1

        # REGEX Professionnel pour éviter les erreurs de frappe
        patterns = {
            'avance': r'avance\s+(\d+\.?\d*)',
            'recule': r'recule\s+(\d+\.?\d*)',
            'tourne_gauche': r'tourne_gauche\s+(\d+\.?\d*)',
            'tourne_droite': r'tourne_droite\s+(\d+\.?\d*)',
            'stop': r'stop'
        }

        for cmd, pattern in patterns.items():
            match = re.match(pattern, raw_text)
            if match:
                valid = True
                val = float(match.group(1)) if cmd != 'stop' else 0.0
                if cmd == 'avance': twist.linear.x = val
                elif cmd == 'recule': twist.linear.x = -val
                elif cmd == 'tourne_gauche': twist.angular.z = val
                elif cmd == 'tourne_droite': twist.angular.z = -val
                elif cmd == 'stop': twist.linear.x = 0.0; twist.angular.z = 0.0
                break

        if valid:
            self.pub.publish(twist)
            self.history.append(raw_text)
            if len(self.history) > 10: self.history.pop(0)
            self.last_msg = raw_text
            # Log Persistant
            with open(self.log_file, "a") as f:
                f.write(f"[{self.get_clock().now().to_msg().sec}] {raw_text}\n")
            self.get_logger().info(f"🚀 Exécution : {raw_text}")
        else:
            self.get_logger().warn(f"⚠️ Format invalide ignoré : {raw_text}")

    def get_history_callback(self, request, response):
        response.history = self.history
        return response

    def get_stats_callback(self, request, response):
        response.total_messages = self.count
        response.average_latency = (time.time() - self.start_time) / (self.count if self.count > 0 else 1)
        response.last_message_processed = self.last_msg
        return response

def main():
    rclpy.init()
    node = CmdParser()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()
