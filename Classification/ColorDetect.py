import cv2 
import numpy as np 
import matplotlib.pyplot as plt
def colorDetection(path):
    frame=cv2.imread(path)
    colors={
        "red":[(0,105,105),(5,255,255),0.0,(170,105,105),(180,255,255),False],
        "brown":[(5,105,20),(15,255,150),0.0,False],
        "orange":[(5,105,155),(23,255,255),0.0,False],
        "blue":[(90,105,105),(120,255,255),0.0,False],
        "green":[(40,105,105),(80,255,255),0.0,False],
        "yellow":[(24,105,105),(35,255,255),0.0,False],
        "purple":[(130,105,105),(155,255,255),0.0,False],
        "pink":[(155,105,105),(170,255,255),0.0,False],
        "black":[(0,0,0),(180,255,50),0.0,False],
        "white": [(0,0,205),(180,50,255),0.0,False],
        "gray":[(0,0,50),(180,50,200),0.0,False]
    }
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    original=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    size = frame.shape[0] * frame.shape[1]
    fig_no=0

    for key in colors:
        if key=='red':
            mask1=cv2.inRange(hsv, colors[key][0], colors[key][1])
            mask2=cv2.inRange(hsv, colors[key][3], colors[key][4])
            mask=mask1+mask2
            res=cv2.bitwise_and(original,original,mask=mask)
            colors[key][2]=(float(cv2.countNonZero(mask))/float(size))*100.0
        else:
            mask=cv2.inRange(hsv, colors[key][0], colors[key][1])
            res=cv2.bitwise_and(original,original,mask=mask)
            colors[key][2]=(float(cv2.countNonZero(mask))/float(size))*100.0
        if(colors[key][2]>5):
            colors[key][-1]=True
        print(key+ " percentage: "+str(colors[key][2])+"%")
    print("Colors that exists are:",end=" ")
    for key in colors:
        if(colors[key][-1]):
            print(key,end=",")
    print("\n")

    for key in colors:
        percentages=[]
        if(key!="black" and key!="white" and key!="gray" and key!="brown" and colors[key][-1]):
            count=0
            print("Shades Percentages of color",key)
            for i in range(101):
                if(i%50==0):
                    for j in range(101):
                        if(j%50==0):
                            if key=='red':
                                mask1=cv2.inRange(hsv, (colors[key][0][0],i+105,j+105),(colors[key][1][0],i+155,j+155))
                                mask2=cv2.inRange(hsv, (colors[key][3][0],i+105,j+105),(colors[key][4][0],i+155,j+155))
                                mask=mask1+mask2
                                res=cv2.bitwise_and(original,original,mask=mask)
                                percentages.append((float(cv2.countNonZero(mask))/float(size))*100.0)
                                print(key,str(count)+ " percentage: "+str((float(cv2.countNonZero(mask))/float(size))*100.0)+"%")
                                count+=1
                            else:
                                mask=cv2.inRange(hsv, (colors[key][0][0],i+105,j+105),(colors[key][1][0],i+155,j+155))
                                res=cv2.bitwise_and(original,original,mask=mask)
                                percentages.append((float(cv2.countNonZero(mask))/float(size))*100.0)
                                print(key,str(count)+ " percentage: "+str((float(cv2.countNonZero(mask))/float(size))*100.0)+"%")
                                count+=1
            maxPercentage=percentages.index(max(percentages))
            print("MAX PERCENTAGE SHADE",maxPercentage)
            print("\n")