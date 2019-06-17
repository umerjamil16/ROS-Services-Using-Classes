#! /usr/bin/env python

import rospy
from my_python_class.srv import CustomSrvMsg, CustomSrvMsgResponse # you import the service message python classes generated from Empty.srv.
from bb8_move_circle_class import MoveBB8

def my_callback(request):
    rospy.loginfo("The Service move_bb8_in_circle has been called")
    movebb8_object = MoveBB8()

    i = 0
    while i <= request.duration:
        movebb8_object.move_bb8()
        rospy.loginfo("Finished service move_bb8_in_circle")
        rospy.loginfo("MoveCircle Callback has been called")
        rospy.loginfo("STARTED service move_bb8_in_circle_custom")
        i = i+1

    rospy.loginfo("Finished service move_bb8_in_circle_custom")

    response = CustomSrvMsgResponse()
    response.success = True
    return response

rospy.init_node('service_move_bb8_in_circle_server')
my_service = rospy.Service('/move_bb8_in_circle', CustomSrvMsg , my_callback)
rospy.loginfo("Service /move_bb8_in_circle Ready")
rospy.spin() # mantain the service open.