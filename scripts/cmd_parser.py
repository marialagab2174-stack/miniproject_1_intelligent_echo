#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from miniproject_1_intelligent_echo.srv import GetHistory
import re
import os

class CmdParser(Node):
    def __init__(self):
        super().__init__('cmd_parser')
        self.sub = self.create_subscription(String, 'cmd_text', self.cmd_callback, 10)
        self.pub = self.create_publisher(Twist, 'robot_response', 10)
        self.srv = self.create_service(GetHistory, 'get_history', self.get_history_callback)
        
        self.history = []
        self.log_file = "robot_commands.log"
        self.get_logger().info("✅ Robot Écho Intelligent (MAX) initialisé.")

    def cmd_callback(self, msg):
        raw_text = msg.data.lower().strip()
        twist = Twist()
        valid = False

        # Utilisation de REGEX pour un parsing professionnel
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
                if cmd == 'avance': twist.linear.x = float(match.group(1))
                elif cmd == 'recule': twist.linear.x = -float(match.group(1))
                elif cmd == 'tourne_gauche': twist.angular.z = float(match.group(1))
                elif cmd == 'tourne_droite': twist.angular.z = -float(match.group(1))
                elif cmd == 'stop': twist.linear.x = 0.0; twist.angular.z = 0.0
                break

        if valid:
            self.pub.publish(twist)
            self.add_to_history(raw_text)
            self.get_logger().info(f"🚀 Commande exécutée : {raw_text}")
        else:
            self.get_logger().warn(f"⚠️ Commande ignorée (Format invalide) : {raw_text}")

    def add_to_history(self, cmd):
        self.history.append(cmd)
        if len(self.history) > 10: self.history.pop(0)
        # Log persistant
        with open(self.log_file, "a") as f:
            f.write(f"[{self.get_clock().now().to_msg().sec}] {cmd}\n")

    def get_history_callback(self, request, response):
        response.history = self.history
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
