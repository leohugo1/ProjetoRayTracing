from vetor import Vetor
import numpy as np

class Ray(Vetor) :
    def __init__(self,origem,raio,time):
        self.origem=origem
        self.raio=Vetor.VetorUnitario(self,raio)
        self.time=time

    def inteseccao(self,t):
        return self.origem + t*self.raio