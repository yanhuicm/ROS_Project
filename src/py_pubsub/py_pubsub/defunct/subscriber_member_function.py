import rclpy
from rclpy.node import Node

from std_msgs.msg import String

from rclpy.callback_groups import ReentrantCallbackGroup
from rclpy.executors import MultiThreadedExecutor

callbackgroup = ReentrantCallbackGroup()


class MinimalSubscriber0(Node):

    def __init__(self):
        super().__init__('minimal_subscriber0')
        self.subscription = self.create_subscription(
            String,
            'topic',
            self.listener_callback,
            10,
            callback_group=callbackgroup)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)

class MinimalSubscriber1(Node):

    def __init__(self):
        super().__init__('minimal_subscriber1')
        self.subscription = self.create_subscription(
            String,
            'topic',
            self.listener_callback,
            10,
            callback_group=callbackgroup)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber0 = MinimalSubscriber0()
    minimal_subscriber1 = MinimalSubscriber1()
    executor = MultiThreadedExecutor(num_threads=4)
    executor.add_node(minimal_subscriber0)
    executor.add_node(minimal_subscriber1)

    executor.spin()

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber0.destroy_node()
    minimal_subscriber1.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

