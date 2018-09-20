import rospy, time, math, random
from random import randint

from std_msgs.msg import Int32, Float32, String
from time import sleep

def cameraDriven():
    camData = randint(0,5000)
    return camData

if __name__ == '__main__':
    rospy.init_node('usb_cam')
    imgPub = rospy.Publisher('camera/image_raw',Int32,queue_size=10)
    rate = rospy.Rate(5)

    while not rospy.is_shutdown():
        camData = cameraDriven()
        #this is where our function defined above will go, along with
        #any additional functionality
        if camData <= 2500:
            rospy.loginfo("The number generated is lower than 2500: %s", camData)
            imgPub.publish(camData)
        else:
            rospy.loginfo("The number generated is lower than 2500: %s", camData)
            imgPub.publish(camData)

rate.sleepy()
