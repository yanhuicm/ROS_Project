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
import numpy as np
from rclpy.node import Node
from sensor_msgs.msg import Image, CompressedImage, PointCloud2
from std_msgs.msg import String
from cv_bridge import CvBridge, CvBridgeError
import cv2
from rclpy.qos import qos_profile_sensor_data
from time import sleep
import os, shutil
import time

from rclpy.callback_groups import ReentrantCallbackGroup,MutuallyExclusiveCallbackGroup
from rclpy.executors import MultiThreadedExecutor

bridge = CvBridge()            

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription1 = self.create_subscription(
            Image,
            'camera/infra1/image_rect_raw',
            self.listener_callback1,
            qos_profile_sensor_data,
            callback_group=MutuallyExclusiveCallbackGroup())
        self.subscription2 = self.create_subscription(
            Image,
            'camera/infra2/image_rect_raw',
            self.listener_callback2,
            qos_profile_sensor_data,
            callback_group=MutuallyExclusiveCallbackGroup())
        '''
        self.subscription3 = self.create_subscription(
            Image,
            '/camera/color/image_raw',
            self.listener_callback3,
            qos_profile_sensor_data,
            callback_group=MutuallyExclusiveCallbackGroup())
         '''

    def listener_callback1(self, msg):
        milli = int(round(time.time() * 1000)) # [-5:] is xx.xxx seconds
        print(f'Received infra1 image {milli}')
        '''
        try:
            cv2_img = bridge.imgmsg_to_cv2(msg, 'bgr8') # ensure correct format of img; orig is bgr8
        except CvBridgeError as e:
            print(e)
        else:
            cv2.imwrite(f'timed/images/{str(milli)[-5:]}_infra1.jpeg', cv2_img)
        '''

    def listener_callback2(self, msg):
        milli = int(round(time.time() * 1000))
        print(f'Received infra2 image {milli}')
        '''
        try:
            cv2_img = bridge.imgmsg_to_cv2(msg, 'bgr8') # ensure correct format of img; orig is bgr8
        except CvBridgeError as e:
            print(e)
        else:
            cv2.imwrite(f'timed/images/{str(milli)[-5:]}_infra2.jpeg', cv2_img)
        '''
    '''
    def listener_callback3(self, msg):
        milli = int(round(time.time() * 1000))
        print(f'Received color image {milli}')
        try:
            cv2_img = bridge.imgmsg_to_cv2(msg, 'bgr8') # ensure correct format of img; orig is bgr8
        except CvBridgeError as e:
            print(e)
        else:
            cv2.imwrite(f'timed/images/{str(milli)[-5:]}_color.jpeg', cv2_img)
    '''

def main(args=None):
    cwd = os.getcwd()
    if os.path.exists(cwd + '/timed/csv') == False:
        os.mkdir(cwd + '/timed/csv')
    if os.path.isdir(cwd + '/timed/images'):
        shutil.rmtree(cwd + '/timed/images')
    os.mkdir(cwd + '/timed/images')

    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    executor = MultiThreadedExecutor(num_threads=100)
    executor.add_node(minimal_subscriber)

    #import pdb;pdb.set_trace()

    executor.spin()

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
