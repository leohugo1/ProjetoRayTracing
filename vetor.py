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
        
        return np.array([random.random(),random.random(),random.random()])
    
    def random_insphere():
        
        r=random.random()
        return r* np.array([random.random(),random.random(),random.random()])