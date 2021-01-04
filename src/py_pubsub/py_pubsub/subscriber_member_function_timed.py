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
import os

from rclpy.callback_groups import ReentrantCallbackGroup,MutuallyExclusiveCallbackGroup
from rclpy.executors import MultiThreadedExecutor

bridge = CvBridge()
callbackgroup0 = ReentrantCallbackGroup()
callbackgroup1 = ReentrantCallbackGroup()
callbackgroup2 = ReentrantCallbackGroup()
callbackgroup3 = ReentrantCallbackGroup()
callbackgroup4 = ReentrantCallbackGroup()

class Listener(Node):

    def __init__(self):
        super().__init__('listener')
        self.subscription = self.create_subscription(
            String,
            'topic',
            self.listener_callback,
            qos_profile_sensor_data)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)

class MinimalSubscriber0(Node):

    def __init__(self):
        super().__init__('minimal_subscriber0')
        self.subscription = self.create_subscription(
            Image,
            '/camera/color/image_raw',
            self.listener_callback,
            qos_profile_sensor_data,
            callback_group=callbackgroup0)
        self.subscription  # prevent unused variable warning
        self.i = 0

    def listener_callback(self, msg):
        print('Received color image')
        self.i += 1
        try:
            # Convert your ROS Image message to OpenCV2
            #np_arr = np.fromstring(msg.data, np.uint8)
            #cv2_img = cv2.imdecode(np_arr, cv2.CV_LOAD_IMAGE_COLOR)
            cv2_img = bridge.imgmsg_to_cv2(msg, 'bgr8') # ensure correct format of img; orig is bgr8
        except CvBridgeError as e:
            print(e)
        else:
            #Save your OpenCV2 image as a jpeg
            #cv2.imshow("color", cv2_img)
            cv2.imwrite(f'timed/images/{self.i}_color.jpeg', cv2_img)
            #cv2.waitKey(1) # used for imshow (window stays open if 1)
            #np.savetxt(f'timed/{self.i}_color.csv', cv2_img, delimiter=',')
            

class MinimalSubscriber1(Node):

    def __init__(self):
        super().__init__('minimal_subscriber1')
        self.subscription = self.create_subscription(
            Image,
            'camera/infra1/image_rect_raw',
            self.listener_callback,
            qos_profile_sensor_data,
            callback_group=callbackgroup1)
        self.i = 0

    def listener_callback(self, msg):
        print('Received infra1 image')
        self.i += 1
        try:
            # Convert your ROS Image message to OpenCV2
            cv2_img = bridge.imgmsg_to_cv2(msg) # ensure correct format of img; orig is bgr8
        except CvBridgeError as e:
            print(e)
        else:
            #Save your OpenCV2 image as a jpeg
            #cv2.imshow("infra1", cv2_img)
            cv2.imwrite(f'timed/images/{self.i}_infra1.jpeg', cv2_img)
            #cv2.waitKey(1)
            #np.savetxt(f'timed/{self.i}_infra1.csv', cv2_img, delimiter=',')

class MinimalSubscriber2(Node):

    def __init__(self):
        super().__init__('minimal_subscriber2')
        self.subscription = self.create_subscription(
            Image,
            'camera/infra2/image_rect_raw',
            self.listener_callback,
            qos_profile_sensor_data,
            callback_group=callbackgroup2)
        self.i = 0

    def listener_callback(self, msg):
        print('Received infra2 image')
        self.i += 1
        try:
            # Convert your ROS Image message to OpenCV2
            cv2_img = bridge.imgmsg_to_cv2(msg) # ensure correct format of img; orig is bgr8
        except CvBridgeError as e:
            print(e)
        else:
            #Save your OpenCV2 image as a jpeg
            #cv2.imshow("infra2", cv2_img)
            cv2.imwrite(f'timed/images/{self.i}_infra2.jpeg', cv2_img)
            #cv2.waitKey(1)
            #np.savetxt(f'timed/{self.i}_infra2.csv', cv2_img, delimiter=',')

class MinimalSubscriber3(Node):

    def __init__(self):
        super().__init__('minimal_subscriber3')
        self.subscription = self.create_subscription(
            Image,
            '/camera/depth/image_rect_raw',
            self.listener_callback,
            qos_profile_sensor_data,
            callback_group=callbackgroup3)
        self.i = 0

    def listener_callback(self, msg):
        print('Received depth image')
        self.i += 1
        try:
            # Convert your ROS Image message to OpenCV2
            cv2_img = bridge.imgmsg_to_cv2(msg) # ensure correct format of img; orig is bgr8
        except CvBridgeError as e:
            print(e)
        else:
            #Save your OpenCV2 image as a jpeg
            #cv2.imshow("depth", cv2_img)
            cv2.imwrite(f'timed/{self.i}_depth.jpeg', cv2_img)
            #cv2.waitKey(1)

'''
class MinimalSubscriber4(Node):

    def __init__(self):
        super().__init__('minimal_subscriber4')
        self.subscription = self.create_subscription(
            PointCloud2,
            '/camera/aligned_depth_to_color/color/points',
            self.listener_callback,
            qos_profile_sensor_data,
            callback_group=callbackgroup4)

    def listener_callback(self, msg):
        points_list = []
        for data in pc2.read_points(ros_cloud, skip_nans=True):
            points_list.append([data[0], data[1], data[2], data[3]])

        pcl_data = pcl.PointCloud_PointXYZRGB()
        pcl_data.from_list(points_list)
        print("Received pointcloud data")
        print(pcl_data)
'''

def main(args=None):
    cwd = os.getcwd()
    if os.path.exists(cwd + '/timed/csv') == False:
        os.mkdir(cwd + '/timed/csv')

    rclpy.init(args=args)

    minimal_subscriber0 = MinimalSubscriber0() # color
    minimal_subscriber1 = MinimalSubscriber1() # infra1
    minimal_subscriber2 = MinimalSubscriber2() # infra2
    #minimal_subscriber3 = MinimalSubscriber3() # depth
    #minimal_subscriber4 = MinimalSubscriber4() # pointcloud

    executor = MultiThreadedExecutor(num_threads=100)
    executor.add_node(minimal_subscriber0)
    executor.add_node(minimal_subscriber1)
    executor.add_node(minimal_subscriber2)
    #executor.add_node(minimal_subscriber3)
    #executor.add_node(minimal_subscriber4)

    #import pdb;pdb.set_trace()

    executor.spin()

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber0.destroy_node()
    minimal_subscriber1.destroy_node()
    minimal_subscriber2.destroy_node()
    #minimal_subscriber3.destroy_node()
    #minimal_subscriber4.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
