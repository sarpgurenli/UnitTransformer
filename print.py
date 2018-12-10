# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 12:02:34 2018

@author: sarpg
"""
import defs
while True:
    print("WELCOME TO VOLUME-AREA CALCULATOR & CONVERTER")
    director = int(input("For volume-area calculator press 1 and enter, for converter press 2 and enter please !(EXIT(3))"))
    if director == 2:
        print("WELCOME TO CONVERTER!")
        print("atm-bar(1)\nknot-m/s(2)\nknot-km/h(3)\nrad-degree(4)\nsea_miles-statute_miles(land miles)(5)\njoule-calorie(6)")
        sel1=int(input("enter converter number:"))
        if sel1 == 1:
            atm = int(input("atm:"))
            bar = int(input("bar:"))
            print("{}Atm = {}bar".format(atm,defs.converter.atm_bar(atm)))
            print("{}bar = {}Atm".format(bar,defs.converter.bar_atm(bar)))
#            print("{}bar = {}Atm".format(bar,defs.converter(bar).bar_atm()))
        elif sel1 == 2:
            knot = int(input("knot:"))
            ms = int(input("ms:"))
            print("{}knot={}m/s".format(knot,defs.converter.knot_ms(knot)))
            print("{}m/s={}knot".format(ms,defs.converter.ms_knot(ms)))
        elif sel1 == 3:
            knot = int(input("knot:"))
            kmh = int(input("kmh:"))
#            print("{}knot={}km/h".format(knot,defs.converter(knot).knot_kmh()))
#            print("{}km/h={}knot".format(kmh,defs.converter(kmh).kmh_knot()))
            print("{}knot={}km/h".format(knot,defs.converter.knot_kmh(knot)))
            print("{}km/h={}knot".format(kmh,defs.converter.kmh_knot(kmh)))
        elif sel1 == 4:
            rad = int(input("rad:"))
            deg = int(input("deg:"))
            print("{}rad={}degree".format(rad,defs.converter.rad_degree(rad)))
            print("{}degree={}rad".format(deg,defs.converter.degree_rad(deg)))
        elif sel1 == 5:
            smile = int(input("smile:"))
            lmile = int(input("lmile:"))
            print("{}nautical miles={}miles".format(smile,defs.converter.seamiles_statuemiles(smile)))
            print("{}miles={}nautical miles".format(lmile,defs.converter.statuemiles_seamiles(lmile)))
        elif sel1 == 6:
            joule = int(input("joule:"))
            calorie = int(input("calorie:"))
            print("{}joule={}calorie".format(joule,defs.converter.joule_calorie(joule)))
            print("{}calorie={}joule".format(calorie,defs.converter.calorie_joule(calorie)))
        else:
            print("EROR !")
    elif director == 1:
        print("WELCOME TO Volume Area Calculator!")
        print("circle area(1)\nsquare area(2)\nrectangular area(3)\nvolume of cube(4)\nvolume of rectangular prism(5)\nvolume of the  sphere(6)")
        sel1=int(input("enter calculation module number:"))
        if sel1 == 1:
            radius = int(input("Radius:"))
            print("Circle Area = {}".format(defs.volume_area.circle_area(radius)))
        elif sel1 == 2:
            dim_edge1 = int(input("length of edge:"))
            print("Square Area = {}".format(defs.volume_area.square_area(dim_edge1)))
        elif sel1 == 3:
            dim_edge1 = int(input("length of long edge:"))
            dim_edge2 = int(input("length of short edge:"))
            print("Rectangular Area = {}".format(defs.volume_area.rectangular_area(dim_edge1,dim_edge2)))
        elif sel1 == 4:
            dim_edge1 = int(input("length of edge:"))
            print("Volume of cube = {}".format(defs.volume_area.vol_cube(dim_edge1)))
        elif sel1 == 5:
            h = int(input("heigth of prism"))
            dim_edge1 = int(input("length of long edge:"))
            dim_edge2 = int(input("length of short edge:"))
            print("Volume of rectangular prism = {}".format(defs.volume_area.vol_rec_prism(h,dim_edge1,dim_edge2)))
        elif sel1 == 6:
            radius = int(input("Radius:"))
            print("volume of the  sphere = {}".format(defs.volume_area.vol_sphere(radius)))
        else:
            print("EROR !")
    elif director == 3:
        break
    else:
        print("EROR !")