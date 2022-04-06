




import math
import numpy as np

from vetor import Vetor

class Camera(Vetor):
    def __init__(self,vfov,aspecto,lookfrom,lookat,up):
        theta=math.radians(vfov)
        self.aspecto = aspecto
        self.h=math.tan(theta/2)
        self.viewportheigth = 2.0 * self.h
        self.viewportwidth = self.viewportheigth* self.aspecto
        self.lookfrom=lookfrom
        self.lookat=lookat
        self.up=up

        w=Vetor.VetorUnitario(self,self.lookfrom-self.lookat)
        u=Vetor.VetorUnitario(self,np.cross(self.up,w))
        v=np.cross(w,u)

        self.horizontal =self.viewportwidth * u
        self.vertical = self.viewportheigth * v

        self.lowerleftcorner = self.lookfrom-(self.horizontal/2) - (self.vertical/2) - w
    