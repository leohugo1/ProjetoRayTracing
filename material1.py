
from abc import ABC,abstractmethod
import math
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