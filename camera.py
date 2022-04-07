




import math
import numpy as np

from vetor import Vetor

class Camera(Vetor):
    def __init__(self,vfov,aspecto,lookfrom,lookat,up,dist_focal,abertura):
        theta=math.radians(vfov)
        self.abertura=abertura
        self.dist_focal=dist_focal
        self.aspecto = aspecto
        self.lookfrom=lookfrom
        self.lookat=lookat
        self.up=up
        self.h=math.tan(theta/2)
        self.viewportheigth = 2.0 * self.h
        self.viewportwidth =self.aspecto* self.viewportheigth 
        

        self.w=Vetor.VetorUnitario(self,self.lookfrom - self.lookat)
        self.u=Vetor.VetorUnitario(self,np.cross(self.up,self.w))
        self.v=np.cross(self.w,self.u)



        self.horizontal = self.dist_focal * self.viewportwidth * self.u  
        self.vertical =  self.dist_focal * self.viewportheigth * self.v 
        

        self.lowerleftcorner = self.lookfrom - self.horizontal/2 - self.vertical/2 - self.dist_focal * self.w 
        print("lowercorner",self.lowerleftcorner)
        self.lensradius=self.abertura/2
    