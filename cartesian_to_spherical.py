# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 18:58:59 2021

@author: User
"""
import numpy as np
import math

def cartesian_to_spherical(normal, point):
    spherical = np.zeros((normal.shape), dtype=np.float32)
    point = np.sqrt(np.sum(np.square(point), axis=1, keepdims=1))
    for i in range(normal.shape[0]):
        if normal[i][0]>0 and normal[i][1]>=0:
            spherical[i][0] = point[i][0]
            spherical[i][1] = math.acos(normal[i][2])/math.pi*180
            spherical[i][2] = abs(math.atan(normal[i][1]/(normal[i][0] + 1e-5))/math.pi*180)
        elif normal[i][0]<=0 and normal[i][1]>0:
            spherical[i][0] = point[i][0]
            spherical[i][1] = math.acos(normal[i][2])/math.pi*180
            spherical[i][2] = 180 - abs(math.atan(normal[i][1]/(normal[i][0] - 1e-5))/math.pi*180)
        elif normal[i][0]<0 and normal[i][1]<=0:
            spherical[i][0] = point[i][0]
            spherical[i][1] = math.acos(normal[i][2])/math.pi*180
            spherical[i][2] = 180 + abs(math.atan(normal[i][1]/(normal[i][0] - 1e-5))/math.pi*180)
        elif normal[i][0]>=0 and normal[i][1]<0:
            spherical[i][0] = point[i][0]
            spherical[i][1] = math.acos(normal[i][2])/math.pi*180
            spherical[i][2] = 360 - abs(math.atan(normal[i][1]/(normal[i][0] + 1e-5))/math.pi*180)
        else:
            spherical[i][0] = point[i][0]
            spherical[i][1] = 0.0
            spherical[i][2] = 0.0
    return spherical
