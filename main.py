
import math
from random import random
from PIL import Image
import numpy as np
from Raio import Ray
from camera import Camera
from vetor import Vetor
from hittable1 import HitRecord
import sys
from material1 import metal, lambetiano,material
from Esferaray import Esfera


vetor1 = Vetor()
samples_perpixel=50
# imagem
aspecto = 16/9
largura = 400
altura = int(math.trunc(largura/aspecto))

imagem = Image.new(mode="RGB", size=(largura, altura), color=0)

SceneObject=[]

def getray(camera,s,t):
    dire = camera.lowerleftcorner + s * camera.horizontal + t * camera.vertical - camera.lookfrom
        
    raio = Ray(camera.lookfrom, dire)
    return raio


def reflect(dir,normal):
    return dir - 2.0 * vetor1.ProdutoEscalar(dir,normal) *normal


def background(dir):
    t = 0.5 * (dir[1] + 1.0)
    # print(t)
    return (1-t) * np.array([1.0, 1.0, 1.0]) + (t*np.array([0.5, 0.7, 1.0]))

def clamp(value,vmin=0.0,vmax=1.0):
    return min(max(value,vmin),vmax)

#dar cor ao objeto
def raycolor(raio:Ray, sceneobject,depth):
    hitRecord=HitRecord()
    ori=raio.origem
    direc=raio.raio
    
    if depth <=0:
        cor=np.array([0.0,0.0,0.0])
        return cor
    if hit(Ray(ori,direc),0.0001,sys.float_info.max,sceneobject,hitRecord):
        sholdscatter,attenuation,direction=hitRecord.material.scatter(raio,hitRecord)
        if sholdscatter:
            newray=Ray(hitRecord.p,direction)
            cor=np.array(attenuation) * raycolor(newray,sceneobject,depth-1)
            return cor
        else:
            return np.array([0.0,0.0,0.0])
    cor = background(direc)
    return cor

#percorrer lista de objetos verificando se ocorre intersecção
def hit(raio:Ray,t_min,t_max,SceneObject,hitRecord:HitRecord):
    hitanything=False
    temprecord=HitRecord()
    closetsofar=t_max

    for object in SceneObject:
        if object.hit(raio,t_min,closetsofar,temprecord):
            hitanything=True
            closetsofar=temprecord.t

            hitRecord.p=temprecord.p
            hitRecord.t=temprecord.t
            hitRecord.normal=temprecord.normal
            hitRecord.frontface=temprecord.frontface
            hitRecord.material=temprecord.material    
    return hitanything


#criar esferas    
materialfloor=lambetiano(np.array([0.8,0.8,0.0]))
materialcenter=lambetiano(np.array([0.7,0.5,0.5]))
materialleft=metal(np.array([0.8,0.8,0.8]),0.9)
materialright=metal(np.array([0.8,1.0,0.2]),0.4)
esfera1 = Esfera(np.array([0.0, 0.0, -1.0]),0.5,materialcenter)
esfera2 = Esfera(np.array([0.0, -100-0.5, -1.0]),100,materialfloor)
esfera3 = Esfera(np.array([-1.0, 0.0, -1.0]),0.5,materialleft)
esfera4 = Esfera(np.array([1.0, 0.0, -1.0]),0.5,materialright)
SceneObject.append(esfera1)
SceneObject.append(esfera2)
SceneObject.append(esfera3)
SceneObject.append(esfera4)

#criar camera

lookfrom=np.array([-2.0,2.0,1.0])
lookat=np.array([0.0,0.0,-1.0])
up=np.array([0.0,1.0,0.0])
camera=Camera(90,aspecto,lookfrom,lookat,up)


#lançar raios na cena
for j in range(1, largura):
    for i in range(1, altura):
        cor=np.array([0.0,0.0,0.0])
        for n in range (1,samples_perpixel):
            u = (j-1 + random())/(largura-1)
            v = 1.0 - (i-1 + random())/(altura-1)
            raio=getray(camera,u,v)
            cor =cor + raycolor(raio, SceneObject,depth=50)
            
           
        scala=1.0 /samples_perpixel
        cor[0] =math.sqrt(scala*cor[0]) 
        cor[1] =math.sqrt(scala*cor[1]) 
        cor[2] =math.sqrt(scala*cor[2]) 
            
        cor1 = int(255.999*clamp(cor[0]))
        cor2 = int(255.999*clamp(cor[1]))
        cor3 = int(255.999*clamp(cor[2]))
        imagem.putpixel((j, i), (cor1, cor2, cor3))    


imagem.save("imagem1.jpg")