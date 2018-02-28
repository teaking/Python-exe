# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 13:33:07 2018

@author: blindness
"""
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-step", required=False, default = 32, help="overlapping by reducing step size, the crop image is 32 x 32.\n Default value == 32")
ap.add_argument("-v", required = False, help = "vertical overlap == True")
args = vars(ap.parse_args())
a = args["step"]
print(type(a))
print (args)