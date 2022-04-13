



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

class retangulo_xy(Vetor):
    def __init__(self,x0,x1,y0,y1,k,material):
        self.x0=x0
        self.x1=x1
        self.y0=y0
        self.y1=y1
        self.k=k
        self.material=material
    def hit(self,ray:Ray,t_min,t_max,hitRecord:HitRecord):
        t=(self.k - ray.origem[2])/ray.raio[2]
        if t<t_min or t>t_max:
            return False
        x=ray.origem[0] + t*ray.raio[0]
        y=ray.origem[1] + t*ray.raio[1]

        if x<self.x0 or x>self.x1 or y<self.y0 or y>self.y1:
            return False
        #hitRecord.u=(x-self.x0)/(self.x1 - self.x0)
        #hitRecord.v=(y-self.y0)/(self.y1- self.y0)
        hitRecord.t=t
        outward_normal=np.array([0.0,0.0,1.0])
        hitRecord.p=ray.inteseccao(t)
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

class retangulo_xz(Vetor):
    def __init__(self,x0,x1,z0,z1,k,material):
        self.x0=x0
        self.x1=x1
        self.z0=z0
        self.z1=z1
        self.k=k
        self.material=material
    def hit(self,ray:Ray,t_min,t_max,hitRecord:HitRecord):
        t=(self.k - ray.origem[1])/ray.raio[1]
        if t<t_min or t>t_max:
            return False
        x=ray.origem[0] + t*ray.raio[0]
        z=ray.origem[2] + t*ray.raio[2]

        if x<self.x0 or x>self.x1 or z<self.z0 or z>self.z1:
            return False
        #hitRecord.u=(x-self.x0)/(self.x1 - self.x0)
        #hitRecord.v=(y-self.y0)/(self.y1- self.y0)
        hitRecord.t=t
        outward_normal=np.array([0.0,1.0,0.0])
        hitRecord.p=ray.inteseccao(t)
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

class retangulo_yz(Vetor):
    def __init__(self,y0,y1,z0,z1,k,material):
        self.z0=z0
        self.z1=z1
        self.y0=y0
        self.y1=y1
        self.k=k
        self.material=material
    def hit(self,ray:Ray,t_min,t_max,hitRecord:HitRecord):
        t=(self.k - ray.origem[0])/ray.raio[0]
        if t<t_min or t>t_max:
            return False
        y=ray.origem[1] + t*ray.raio[1]
        z=ray.origem[2] + t*ray.raio[2]

        if y<self.y0 or y>self.y1 or z<self.z0 or z>self.z1:
            return False
        #hitRecord.u=(x-self.x0)/(self.x1 - self.x0)
        #hitRecord.v=(y-self.y0)/(self.y1- self.y0)
        hitRecord.t=t
        outward_normal=np.array([1.0,0.0,0.0])
        hitRecord.p=ray.inteseccao(t)
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