#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from miniproject_1_intelligent_echo.srv import GetHistory

class CmdParser(Node):
    def __init__(self):
        super().__init__('cmd_parser')
        self.sub = self.create_subscription(String, 'cmd_text', self.cmd_callback, 10)
        self.pub = self.create_publisher(Twist, 'robot_response', 10)
        self.srv = self.create_service(GetHistory, 'get_history', self.get_history_callback)
        
        self.history = []
        self.get_logger().info("Robot Écho Intelligent : Parser prêt.")

    def cmd_callback(self, msg):
        cmd_raw = msg.data.lower().strip()
        parts = cmd_raw.split()
        twist = Twist()
        
        try:
            if 'avance' in parts:
                twist.linear.x = float(parts[1])
            elif 'recule' in parts:
                twist.linear.x = -float(parts[1])
            elif 'tourne_gauche' in parts:
                twist.angular.z = float(parts[1])
            elif 'tourne_droite' in parts:
                twist.angular.z = -float(parts[1])
            elif 'stop' in parts:
                twist.linear.x = 0.0
                twist.angular.z = 0.0
            
            self.pub.publish(twist)
            self.history.append(cmd_raw)
            if len(self.history) > 10: self.history.pop(0)
            self.get_logger().info(f"Exécution : {cmd_raw}")
            
        except (IndexError, ValueError):
            self.get_logger().error(f"Commande invalide : {cmd_raw}")

    def get_history_callback(self, request, response):
        response.history = self.history
        return response

def main():
    rclpy.init()
    node = CmdParser()
    rclpy.spin(node)
