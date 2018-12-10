# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 10:34:11 2018

@author: sarpg
"""
#import numpy as np
#class converter:
#    def __init__(self,atm=0,bar=0,knot=0,ms=0,kmh=0,rad=0,deg=0,smile=0,lmile=0,joule=0,calorie=0):
#        self.atm = atm
#        self.bar = bar
#        self.knot = knot
#        self.ms = ms
#        self.kmh = kmh
#        self.rad = rad
#        self.deg = deg
#        self.smile = smile
#        self.lmile = lmile
#        self.joule = joule
#        self.calorie = calorie
#    def atm_bar(self):
#        """1 atm = 1.01325 """
#        return self.atm*1.0132
#    def knot_ms(self):
#        """1 knot = 0.514444444 meters / second"""
#        return self.knot*0.5144
#    def knot_kmh(self):
#        """1 knot = 1.85200 kilometers per hour"""
#        return self.knot*1.8520
#    def rad_degree(self):
#        return self.rad*(np.pi/180)
#    def seamiles_statuemiles(self):
#        """1 nautical mile = 1.15077945 miles"""
#        return self.smile*1.1507
#    def joule_calorie(self):
#        """1 joule = 0.239005736 calories"""
#        return self.joule*0.2390
#    def bar_atm(self):
#        """1 bar = 0.986923267 atm"""
#        return self.bar*0.9869
#    def ms_knot(self):
#        """1 (meter / second) = 1.94384449 knot"""
#        return self.ms*1.9438
#    def kmh_knot(self):
#        """1 kilometer per hour = 0.539956803 knot"""
#        return self.kmh*0.5399
#    def degree_rad(self):
#        return self.deg*(180/np.pi)
#    def statuemiles_seamiles(self):
#        """1 mile = 0.868976242 nautical mile"""
#        return self.lmile*0.8689
#    def calorie_joule(self):
#        """1 calorie = 4.18400 joules"""
#        return self.calorie*4.1840
#class volume_area:
#    def __init__(self,radius,dim_edge1,dim_edge2,h):
#        self.radius = radius
#        self.dim_edge1 = dim_edge1
#        self.dim_edge2 = dim_edge2
#        self.h = h
#    def circle_area(self):
#        return np.pi*self.radius**2
#    def square_area(self):
#        return self.dim_edge1**2
#    def rectangular_area(self):
#        return self.dim_edge1*self.dim_edge2
#    def vol_cube(self):
#        return self.dim_edge1**3
#    def vol_rec_prism(self):
#        return self.h*self.dim_edge1*self.dim_edge2
#    def vol_sphere(self):
#        return (4/3)*np.pi*self.radius**3
import numpy as np
class converter:
    def atm_bar(atm):
        """1 atm = 1.01325 """
        return atm*1.0132
    def knot_ms(knot):
        """1 knot = 0.514444444 meters / second"""
        return knot*0.5144
    def knot_kmh(knot):
        """1 knot = 1.85200 kilometers per hour"""
        return knot*1.8520
    def rad_degree(rad):
        return rad*(np.pi/180)
    def seamiles_statuemiles(smile):
        """1 nautical mile = 1.15077945 miles"""
        return smile*1.1507
    def joule_calorie(joule):
        """1 joule = 0.239005736 calories"""
        return joule*0.2390
    def bar_atm(bar):
        """1 bar = 0.986923267 atm"""
        return bar*0.9869
    def ms_knot(ms):
        """1 (meter / second) = 1.94384449 knot"""
        return ms*1.9438
    def kmh_knot(kmh):
        """1 kilometer per hour = 0.539956803 knot"""
        return kmh*0.5399
    def degree_rad(deg):
        return deg*(180/np.pi)
    def statuemiles_seamiles(lmile):
        """1 mile = 0.868976242 nautical mile"""
        return lmile*0.8689
    def calorie_joule(calorie):
        """1 calorie = 4.18400 joules"""
        return calorie*4.1840
class volume_area:
    def circle_area(radius):
        return np.pi*radius**2
    def square_area(dim_edge1):
        return dim_edge1**2
    def rectangular_area(dim_edge1,dim_edge2):
        return dim_edge1*dim_edge2
    def vol_cube(dim_edge1):
        return dim_edge1**3
    def vol_rec_prism(h,dim_edge1,dim_edge2):
        return h*dim_edge1*dim_edge2
    def vol_sphere(radius):
        return (4/3)*np.pi*radius**3