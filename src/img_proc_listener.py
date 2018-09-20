import rospy
import cv2
from cv_bridge import CvBridge, CvBridgeError
from std_msgs.msg import String, Int32
from sensor_msgs.msg import Image
from random import randint

# def imagecb(data):
#     # Convert Image message to CV image with blue-green-red color order (bgr8)
#     try:
#         img_original = bridge.imgmsg_to_cv2(data, "bgr8")
#     except CvBridgeError, e:
#         print("==[CAMERA MANAGER]==", e)

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

# def listener():
#
#     rospy.init_node('listener', anonymous=True)
#
#     rospy.Subscriber("camera/image_raw", String, callback, bridge)
#
#     imagecb(data)
#
#     # spin() simply keeps python from exiting until this node is stopped
#     rospy.spin()

if __name__ == '__main__':
    rospy.init_node('cam_data_subscriber',anonymous=True)
    sub=rospy.Subscriber('camera/image_raw', Int32, callback)
    rospy.spin()
