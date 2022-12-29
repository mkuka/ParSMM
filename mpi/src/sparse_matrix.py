# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 18:31:18 2022
@author: Kuka
"""
import random
from scipy import stats
from numpy.random import default_rng

class S_matrix:
    def __init__(self, r,c,density):
       self.size = (r,c)
       self.density=density

#generate random matrix
    def random_matrix(self):
        number_non_zero=(int(self.density)/100)
        rng = default_rng()
        rvs = stats.poisson(25, loc=10).rvs
        sparse_matrix = random(self.size[0],self.size[1], density=number_non_zero, random_state=rng, data_rvs=rvs).toarray()
        return sparse_matrix

# vector multiplication
    def matix_vec_mul_original(self,M,v):
        res=[0]*M.shape[0]
        # print(res)
        # res = [[0 for x in range(M)] for y in range(M)]
        print(v.shape)
        print(M.shape)
        if v.shape[0]==M.shape[1]:
            for i in range(len(M)):
                # print(i)
                ans=0
                for j in range(len(M[0])):
                    # print(v[i])
                    # print(M[i][j])
                    ans+=v[j]*M[i][j]
                    # print(ans)
                res[i]=ans
            # print(res)
        return res
