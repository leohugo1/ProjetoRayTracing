
import numpy as np


class Hittable:
    def __init__(self,ray,t_min,t_max,hit_Record):
        pass    


class HitRecord:
    def __init__(self,t=0.0,p=np.array([0.0,0.0,0.0]),normal=np.array([0.0,0.0,0.0]),frontface=False,material=np.array([0.0,0.0,0.0])):
        self.t=t
        self.p=p
        self.normal=normal
        self.frontface=frontface
        self.material=material
        #self.u
        #self.v