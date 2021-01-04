import rclpy
from rclpy.node import Node

from std_msgs.msg import String

from rclpy.callback_groups import ReentrantCallbackGroup
from rclpy.executors import MultiThreadedExecutor

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription0 = self.create_subscription(
            String,
            'topic',
            self.listener_callback0,
            10,
            callback_group=ReentrantCallbackGroup())
        self.subscription1 = self.create_subscription(
            String,
            'topic',
            self.listener_callback1,
            10,
            callback_group=ReentrantCallbackGroup())

    def listener_callback0(self, msg):
        self.get_logger().info('0 I heard: "%s"' % msg.data)

    def listener_callback1(self, msg):
        self.get_logger().info('1 I heard: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()
    executor = MultiThreadedExecutor(num_threads=50)
    executor.add_node(minimal_subscriber)

    executor.spin_once()

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

