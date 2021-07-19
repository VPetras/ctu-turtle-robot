#!/usr/bin/env python2
from sensor_msgs.msg import LaserScan
import matplotlib.pyplot as plt
import numpy as np
import rospy


class ScanCollector():

    def __init__(self):
        # Initialize Subscriber node for topic name "/scan"
        rospy.init_node('listener')
        self.subscriber = rospy.Subscriber('scan', LaserScan, self.scan_callback)
        # Initialize filter and plot parameters
        self.plot_min_angle = np.radians(-30)
        self.plot_max_angle = np.radians(30)

        self.plot_length = 500
        self.start_time = 0
        # TODO: initialize the necessary variables to store data:

    def plot_ranges(self, x, y):
        plt.plot(x, y)
        plt.xlabel('time [s]')
        plt.ylabel('distance [m]')
        plt.title('LaserScan Data')
        plt.show()

    def scan_callback(self, msg):

        # 1) TODO: Parse input message, extract all needed data:
        # Example:
        # angle_min = msg.angle_min
        # angle_max = msg.angle_max

        # 2) TODO: Filter out erroneous data from scan

        # TODO: Discard unwanted angles
        # TODO: Ignore wrong ranges

        # 3) TODO: store filtered data and message timestamp.

        # ...

        # 4) TODO: plot ranges if the number of stored values had reached the number specified in the plot_length
        # self.plot_ranges(timestamps, data)

        return


if __name__ == '__main__':
    sc = ScanCollector()
    rospy.spin()