#!/usr/bin/env python
#-*- coding: utf-8 -*-
import rospy
import time
from std_msgs.msg import String

def cb(message):

    if message.data == "好きな食べ物は？":
        print "（＾_＾）＜　激辛ラーメン！"
    if message.data == "嫌いな食べ物は？":
        print "（・_・；）＜　・・・しいたけ"
    if message.data == "好きなスポーツは？":
        print "（＾A＾）＜　バスケットボール！"
    if message.data == "好きな大学の講義は？":
        print "（＾o＾）＜　ロボットシステム学！"
        time.sleep(3)
        print "ｍ（＿＿）ｍ＜　先生ありがとうございました！"




if __name__ == '__main__': 
    print "（＾_＾）＜質問してね！"
    rospy.init_node('twice')
    sub = rospy.Subscriber('count_up', String, cb) 
    rospy.spin()
