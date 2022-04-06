import math
import random
import numpy as np



class Vetor:
    def normaSquared(self,vetor):
        return np.sum(vetor[0]*vetor[0]+vetor[1]*vetor[1]+vetor[2]*vetor[2])
    
    def norma(self,vetor):
        return math.sqrt(self.normaSquared(vetor))

    def ProdutoEscalar(self,vet1,vet2):
        return np.dot(vet1,vet2)

    def VetorUnitario(self,vetor):
        return vetor / self.norma(vetor)

    def random_unitvetor():
        f=1/0.1
        costheta=random.uniform(0.0,2*math.pi)
        cosph=random.uniform(0.0,math.pi)

        return np.array([math.cos(costheta)*math.sin(cosph),math.sin(costheta)*math.sin(cosph),math.cos(cosph)])
    
    def random_insphere():

        costheta=random.uniform(0.0,2*math.pi)
        cosph=random.uniform(0.0,math.pi)
        r=random.random()
        return r * np.array([math.cos(costheta)*math.sin(cosph),math.sin(costheta)*math.sin(cosph),math.cos(cosph)])