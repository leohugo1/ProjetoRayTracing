
import math
import random
from PIL import Image
import numpy as np
from Raio import Ray
from camera import Camera
from vetor import Vetor
from hittable1 import HitRecord
import sys
from material1 import Dieletric, diffuse_light, metal, lambetiano,material
from Esferaray import Esfera, moving_sphere, retangulo_xy, retangulo_xz, retangulo_yz


vetor1 = Vetor()
samples_perpixel=100
# imagem
aspecto = 16/9
largura = 400
altura = int(math.trunc(largura/aspecto))

imagem = Image.new(mode="RGB", size=(largura, altura), color=0)

SceneObject=[]

def random_indisc():
    
    return np.array([random.random(),random.random(),0.0])

def getray(camera:Camera,s,t):
    orizon=camera.horizontal
    vert=camera.vertical
    rd=camera.lensradius * random_indisc()
    
    origin=camera.lookfrom + (camera.u * rd[0]) + (camera.v * rd[1])
   
    dire = camera.lowerleftcorner + (s * orizon) + (t * vert) - origin
    time=random.uniform(camera.time0,camera.time1) 
  
    return Ray(origin, dire,time)
    


def reflect(dir,normal):
    return dir - 2.0 * vetor1.ProdutoEscalar(dir,normal) *normal


def background(dir):
    t = 0.5 * (dir[1] + 1.0)
    # print(t)
    return (1-t) * np.array([0.0, 0.0, 0.0]) + (t*np.array([0.0, 0.0, 0.0]))

def clamp(value,vmin=0.0,vmax=1.0):
    return min(max(value,vmin),vmax)

#dar cor ao objeto
def raycolor(raio:Ray, sceneobject,depth):
    hitRecord=HitRecord()
    origin=raio.origem
    direc=raio.raio
    time=raio.time
    if depth <=0:
        cor=np.array([0.0,0.0,0.0])
        return cor
    if hit(Ray(origin,direc,time),0.0001,sys.float_info.max,sceneobject,hitRecord):
        sholdscatter,attenuation,direction=hitRecord.material.scatter(raio,hitRecord)
        if sholdscatter:
            newray=Ray(hitRecord.p,direction,time)
            cor=np.array(attenuation) * raycolor(newray,sceneobject,depth-1)
            return cor
        else:
            return attenuation
    cor = background(raio.raio)
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
red=lambetiano(np.array([0.65,0.5,0.5]))
white=lambetiano(np.array([0.73,0.73,0.73]))
green=lambetiano(np.array([0.12,0.45,0.15]))
materialleft=metal(np.array([0.8,0.6,0.2]),0.0)
materialright=metal(np.array([0.8,0.6,0.2]),0.0)
difuso=diffuse_light(np.array([15,15,15]))
glass=Dieletric(1.33)
#esfera0=moving_sphere(np.array([1.0,0.0,-1.0]),np.array([1.3,0.0,-1.0]),0.0,1.0,0.5,materialcenter)
esfera1 = retangulo_yz(0,555, 0,555,555,green)
esfera2 = retangulo_yz(0,555,0,555,0,red)
esfera3 = retangulo_xz(213,343, 227,332,554,difuso)
esfera5=retangulo_xz(0, 555, 0, 555, 0, white)
esfera4 = retangulo_xz(0, 555, 0, 555, 555, white)
esfera6=retangulo_xy(0, 555, 0, 555, 555, white)
SceneObject.append(esfera1)
SceneObject.append(esfera2)
SceneObject.append(esfera3)
SceneObject.append(esfera4)
SceneObject.append(esfera5)
SceneObject.append(esfera6)
#criar camera

lookfrom=np.array([278, 278, -800])
lookat=np.array([278, 278, 0])
up=np.array([0,1,0])

camera=Camera(40.0,aspecto,lookfrom,lookat,up,vetor1.norma(lookfrom-lookat),0.1,0.0,0.8)


#lançar raios na cena
for j in range(1, largura):
    for i in range(1, altura):
        cor=np.array([0.0,0.0,0.0])
        for n in range (1,samples_perpixel):
            u = (j-1 + random.random())/(largura-1)
            v = 1.0 - (i-1 + random.random())/(altura-1)
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


imagem.save("imagem7.jpg")
