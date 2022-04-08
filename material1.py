
from abc import ABC,abstractmethod
import math
import random
from Raio import Ray
from hittable1 import HitRecord
from vetor import Vetor
import numpy as np

class material(ABC):
    @abstractmethod
    def scatter(self,ray:Ray,hitrecord:HitRecord):
        pass

class metal(material):
    def __init__(self,material,fuzz):
        self.material=material
        if fuzz<1:self.fuzz=fuzz
        else:
            self.fuzz=1
        pass
    def scatter(self,ray:Ray,hitrecord:HitRecord):
        dir=ray.raio - 2.0 * Vetor.ProdutoEscalar(self,ray.raio,hitrecord.normal) *hitrecord.normal + Vetor.random_insphere() * self.fuzz

        if Vetor.ProdutoEscalar(self,dir,hitrecord.normal) >0 :
            sholdscatter = True
        else:
            sholdscatter=False
        return sholdscatter,self.material,dir

class lambetiano(material):
    def __init__(self,material):
        self.material=material
        pass
    def scatter(self,ray:Ray,hitrecord:HitRecord):
        scatterdir=hitrecord.normal + Vetor.random_unitvetor() 
        

        if all(map(lambda x:math.isclose(a=x,b=0,rel_tol=1e-8,abs_tol=0.1),scatterdir)):
            scatterdir=hitrecord.normal
        

        return True,self.material,scatterdir

class Dieletric(material):
    def __init__(self,refracao):
        self.refracao=refracao
    def refratar(self,dir,normal,refractionatio):
        costheta=min(Vetor.ProdutoEscalar(self,-dir,normal),1.0)
        perp=refractionatio*(dir + costheta * normal)
        parallel= - math.sqrt(abs(1.0 - Vetor.normaSquared(self,perp))) * normal
        return perp + parallel

    def reflectance(self,coseno,refidx):
        r0=(1-refidx) / (1+ refidx)
        r0= r0*r0
        return r0 + (1-r0)*math.pow((1-coseno),5)

    def scatter(self, ray: Ray, hitrecord: HitRecord):
        ir=self.refracao
        if(hitrecord.frontface): 
            refrectionratio=1.0/ir
        else:
            refrectionratio= ir

        costheta= min(np.dot(-ray.raio,hitrecord.normal),1.0)
        sintheta=math.sqrt(1.0 - int(costheta*costheta))

        cannotrefrect=refrectionratio * sintheta
        if cannotrefrect >1.0 or self.reflectance(costheta,refrectionratio)> random.random():
            scatterdir=ray.raio - 2.0 * Vetor.ProdutoEscalar(self,ray.raio,hitrecord.normal) *hitrecord.normal + Vetor.random_insphere()
        else:
            scatterdir=self.refratar(ray.raio,hitrecord.normal,refrectionratio)


        return True,np.array([1.0,1.0,1.0]),scatterdir