#!/usr/bin/env python3
import rclpy
#nodes uses OOP 

from rclpy.node import Node
#this class is going to inherit from the node class of rclpy 

class MyNode(Node): #we are defininga class Mynode which inherits from the node that is from rclpy node
   
    #next thing is creating a constructor
    def __init__(self):
        super().__init__("first_node")#Put actual node name in Parathesis
        self.get_logger().info("Hello from ROS2")

def main(args=None): #Main Function
    rclpy.init (args=args) #initialize Ros Communication
    node = MyNode()
    rclpy.spin(node) #spin functionality it means that the node is kept running infinitely until ctrl c is pressed
    rclpy.shutdown() #last thing to shutdown the communication

if __name__ == '__main__':
    main()


