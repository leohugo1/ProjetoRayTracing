



import math
import numpy as np
from hittable1 import HitRecord, Hittable
from vetor import Vetor
from Raio import Ray

class Esfera(Vetor):
    def __init__(self,centro,raio,material):
        self.centro=centro
        self.raio=raio
        self.material=material
    def hit(self,ray:Ray,t_min,t_max,hitRecord:HitRecord):
        a=Vetor.normaSquared(self,ray.raio)
        oc=ray.origem-np.array(self.centro)
        b=Vetor.ProdutoEscalar(self,ray.raio,oc)
        c=Vetor.normaSquared(self,oc) - self.raio**2
        disc=b*b -  a *c
        if disc<0:
            return False
        else:
            raiz=math.sqrt(disc)
            t=(-b - raiz)/a 
            if t< t_min or t>t_max:
                t=(-b + raiz)/a
                if  t< t_min or t>t_max:
                    return False
            hitRecord.t=t
            hitRecord.p=ray.inteseccao(hitRecord.t)
            outward_normal=(hitRecord.p - self.centro)/self.raio
            if Vetor.ProdutoEscalar(self,ray.raio,np.array(outward_normal)) < 0:
                hitRecord.frontface=True
            else:
                hitRecord.frontface=False
            if hitRecord.frontface:
                hitRecord.normal=outward_normal
                hitRecord.material=self.material
                return True 
            else:
                hitRecord.normal= -outward_normal
                hitRecord.material=self.material
                return True



class moving_sphere(Vetor):
    def __init__(self,cen0,cen1,time0,time1,r,material):
        self.cen0=cen0
        self.cen1=cen1
        self.time0=time0
        self.time1=time1
        self.r=r
        self.material=material
    def center(self,time):
        return np.array(self.cen0 + ((time-self.time0)/(self.time1-self.time0)) * (self.cen1 - self.cen0))
    def hit(self,ray:Ray,t_min,t_max,hitRecord:HitRecord):
            oc=ray.origem - self.center(ray.time)
            a=Vetor.normaSquared(self,ray.raio)
            b=Vetor.ProdutoEscalar(self,ray.raio,oc)
            c=Vetor.normaSquared(self,oc) - self.r**2

            disc=b*b -  a *c
            if disc<0:
                return False
            else:
                raiz=math.sqrt(disc)
                t=(-b - raiz)/a 
                if t< t_min or t>t_max:
                    t=(-b + raiz)/a
                    if  t< t_min or t>t_max:
                        return False
            hitRecord.t=t
            hitRecord.p=ray.inteseccao(hitRecord.t)
            outward_normal=(hitRecord.p - self.center(ray.time))/self.r
            if Vetor.ProdutoEscalar(self,ray.raio,np.array(outward_normal)) < 0:
                hitRecord.frontface=True
            else:
                hitRecord.frontface=False
            if hitRecord.frontface:
                hitRecord.normal=outward_normal
                hitRecord.material=self.material
                return True 
            else:
                hitRecord.normal= -outward_normal
                hitRecord.material=self.material
                return True
