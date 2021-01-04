# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
from rclpy.qos import qos_profile_sensor_data

bridge = CvBridge()

class MinimalSubscriber0(Node):

    def __init__(self):
        super().__init__('minimal_subscriber0')
        self.subscription = self.create_subscription(
            Image,
            '/camera/color/image_raw',
            self.listener_callback,
            qos_profile_sensor_data)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        print('Received color image')
        try:
            # Convert your ROS Image message to OpenCV2
            cv2_img = bridge.imgmsg_to_cv2(msg, 'bgr8') # ensure correct format of img; orig is bgr8
        except CvBridgeError as e:
            print(e)
        else:
            #Save your OpenCV2 image as a jpeg
            cv2.imwrite('color.jpeg', cv2_img)
            cv2.imshow('image', cv2_img)
            cv2.waitKey(1)

class MinimalSubscriber1(Node):

    def __init__(self):
        super().__init__('minimal_subscriber1')
        self.subscription = self.create_subscription(
            Image,
            'camera/infra1/image_rect_raw',
            self.listener_callback,
            qos_profile_sensor_data)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        print('Received infra1 image')
        try:
            # Convert your ROS Image message to OpenCV2
            cv2_img = bridge.imgmsg_to_cv2(msg) # ensure correct format of img; orig is bgr8
        except CvBridgeError as e:
            print(e)
        else:
            #Save your OpenCV2 image as a jpeg
            cv2.imwrite('infra1.jpeg', cv2_img)
            cv2.imshow('image', cv2_img)
            cv2.waitKey(1)

class MinimalSubscriber2(Node):

    def __init__(self):
        super().__init__('minimal_subscriber2')
        self.subscription = self.create_subscription(
            Image,
            'camera/infra2/image_rect_raw',
            self.listener_callback,
            qos_profile_sensor_data)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        print('Received infra2 image')
        try:
            # Convert your ROS Image message to OpenCV2
            cv2_img = bridge.imgmsg_to_cv2(msg) # ensure correct format of img; orig is bgr8
        except CvBridgeError as e:
            print(e)
        else:
            #Save your OpenCV2 image as a jpeg
            cv2.imwrite('infra2.jpeg', cv2_img)
            cv2.imshow('image', cv2_img)
            cv2.waitKey(1)

class MinimalSubscriber3(Node):

    def __init__(self):
        super().__init__('minimal_subscriber3')
        self.subscription = self.create_subscription(
            Image,
            '/camera/aligned_depth_to_color/image_raw',
            self.listener_callback,
            qos_profile_sensor_data)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        print('Received depth image')
        try:
            # Convert your ROS Image message to OpenCV2
            cv2_img = bridge.imgmsg_to_cv2(msg) # ensure correct format of img; orig is bgr8
        except CvBridgeError as e:
            print(e)
        else:
            #Save your OpenCV2 image as a jpeg
            cv2.imwrite('depth.jpeg', cv2_img)
            cv2.imshow('image', cv2_img)
            cv2.waitKey(1)

def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber0 = MinimalSubscriber0()
    minimal_subscriber1 = MinimalSubscriber1()
    minimal_subscriber2 = MinimalSubscriber2()
    minimal_subscriber3 = MinimalSubscriber3()
    #import pdb;pdb.set_trace()

    rclpy.spin_once(minimal_subscriber0)
    rclpy.spin_once(minimal_subscriber1)
    rclpy.spin_once(minimal_subscriber2)
    rclpy.spin_once(minimal_subscriber3)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber0.destroy_node()
    minimal_subscriber1.destroy_node()
    minimal_subscriber2.destroy_node()
    minimal_subscriber3.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
