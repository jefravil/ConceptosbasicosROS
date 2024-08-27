#! /usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

speed = .2
turn = 1
last_msg = None

def callback (msg):
    global last_msg
    last_msg =msg


def cambiomov(linearX=0.0,angularZ=0.0):
            twist = Twist()
            twist.linear.x = linearX*speed
            twist.linear.y = 0
            twist.linear.z = 0
            twist.angular.x = 0
            twist.angular.y = 0
            twist.angular.z = angularZ*turn
            pub.publish(twist)

if __name__ == "__main__":
    try:
        rospy.init_node('topics_quiz_node')
        pub= rospy.Publisher('/cmd_vel', Twist,queue_size=1)
        sub= rospy.Subscriber('/kobuki/laser/scan', LaserScan, callback)
        rate = rospy.Rate(20)
        while not rospy.is_shutdown():
            if last_msg != None:
                rangesArray= last_msg.ranges
                cantArray= len(rangesArray)
                d_angle_min= rangesArray[0]
                d_angle_max= rangesArray[-1]
                d_angle_mid= rangesArray[int(round((cantArray-1)/2))]
                print(d_angle_min,'\n')
                print(d_angle_mid,'\n')
                print(d_angle_max,'\n')

                if d_angle_min<=1:
                    cambiomov(1,0.7)
                elif d_angle_max<=1:
                    cambiomov(1,0.7)
                elif d_angle_mid<=1:
                    if d_angle_mid<=0.3:
                        print('retrocediendo')
                        while d_angle_mid<=0.5:
                            cambiomov(-1,0)
                            print(d_angle_min,'\n')
                            print(d_angle_mid,'\n')
                            print(d_angle_max,'\n')
                            rangesArray= last_msg.ranges
                            d_angle_mid= rangesArray[int(round((cantArray-1)/2))]
                            rate.sleep() 
                            
                    else:
                        cambiomov(1,0.7)
                else:
                    cambiomov(1,0)
            rate.sleep() 
        cambiomov(0,0)
                
    
    except rospy.ROSInterruptException:
        pass

    finally:
        cambiomov(0,0)
