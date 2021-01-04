import rclpy
from rclpy.node import Node
import time

from std_msgs.msg import String

from rclpy.callback_groups import MutuallyExclusiveCallbackGroup,ReentrantCallbackGroup
from rclpy.executors import MultiThreadedExecutor

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        timer_period = 1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback, callback_group=MutuallyExclusiveCallbackGroup())
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello World: %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        #self.callback_group = MutuallyExclusiveCallbackGroup()
        self.subscription0 = self.create_subscription(
            String,
            'topic',
            self.listener_callback0,
            10,
            callback_group=MutuallyExclusiveCallbackGroup())
        self.subscription1 = self.create_subscription(
            String,
            'topic',
            self.listener_callback1,
            10,
            callback_group=MutuallyExclusiveCallbackGroup())

    def listener_callback0(self, msg):
        self.get_logger().info(f'0 I heard: {msg.data} {time.time()}')

    def listener_callback1(self, msg):
        self.get_logger().info(f'1 I heard: {msg.data} {time.time()}')

def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()
    minimal_publisher = MinimalPublisher()
    executor = MultiThreadedExecutor(num_threads=50)
    executor.add_node(minimal_subscriber)
    executor.add_node(minimal_publisher)

    executor.spin()

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

