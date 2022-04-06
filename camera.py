




import math
import numpy as np

from vetor import Vetor

class Camera(Vetor):
    def __init__(self,vfov,aspecto,lookfrom,lookat,up,focus_dist,aperture=0.0):
        theta=math.radians(vfov)
        self.aperture=aperture
        self.focus_dist=focus_dist
        self.aspecto = aspecto
        self.h=math.tan(theta/2)
        self.viewportheigth = 2.0 * self.h
        self.viewportwidth = self.viewportheigth* self.aspecto
        self.lookfrom=lookfrom
        self.lookat=lookat
        self.up=up
        

        self.w=Vetor.VetorUnitario(self,self.lookfrom-self.lookat)
        self.u=Vetor.VetorUnitario(self,np.cross(self.up,self.w))
        self.v=np.cross(self.w,self.u)



        self.horizontal =self.viewportwidth * self.u * self.focus_dist
        self.vertical = self.viewportheigth * self.v * self.focus_dist
        
        self.lensradius=self.aperture/2

        self.lowerleftcorner = self.lookfrom-(self.horizontal/2) - (self.vertical/2) - self.w * self.focus_dist
    