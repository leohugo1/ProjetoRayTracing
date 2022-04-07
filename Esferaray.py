



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
            outward_normal=Vetor.VetorUnitario(self,hitRecord.p - self.centro)/self.raio
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