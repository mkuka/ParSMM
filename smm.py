# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 11:26:01 2022

@author: Kuka
"""

from mpi4py import MPI
import numpy as np
import time
from sparse_matrix import S_matrix


t0 = time.time()
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
nprocs = comm.Get_size()



        
       
r=1000
c=1000

# Matrix=np.array([[27.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
#         [ 0.,  0.,  0.,  0.,  0., 41.,  0.,  0., 40.,  0.],
#         [28.,  0., 34.,  0.,  0., 35.,  0.,  0.,  0.,  0.],
#         [ 0., 34.,  0.,  0., 33.,  0.,  0.,  0.,  0.,  0.],
#         [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
#         [ 0.,  0.,  0., 36.,  0.,  0.,  0.,  0.,  0.,  0.],
#         [ 0.,  0., 41.,  0., 28.,  0.,  0.,  0.,  0.,  0.],
#         [31.,  0., 37.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
#         [0.,  0.,  0., 31.,  0., 34., 30., 31.,  0.,  0.],
#         [ 0.,  0.,  0.,  0.,  0.,  0., 27., 28., 38.,  0.]])

# Matrix=np.array([[27.,  0.,  0.,  0.],
#             [0.,  0.,  0.,  0.],
#         [ 0.,  0.,  0.,  0.], 
#         [0., 41.,  0.,  0.], 
#         [28.,  0., 34.,  0.]])

vec = np.arange(c)
vec=comm.bcast(vec,root=0)

sp=S_matrix(r,c,30)
M=sp.random_matrix()

Matrix=M
num_steps = M[0].size

# print(num_steps)

# step size
#dx = 1.0 / nsteps

if rank == 0:
    
    
    ans, rem = divmod(num_steps, nprocs)
    # counts = [ans + 1 if pro < rem else ans for pro in range(nprocs)]
    # determine the size of each sub-task
    ans, rem = divmod(num_steps, nprocs)
    tasks_each_pro = [ans + 1 if pro < rem else ans for pro in range(nprocs)]
    print(tasks_each_pro)
    # determine the starting and ending indices of each sub-task
    starts = [sum(tasks_each_pro[:pro]) for pro in range(nprocs)]
    ends = [sum(tasks_each_pro[:pro+1]) for pro in range(nprocs)]
    # print(counts)
    # print(starts, ends)
    # save the starting and ending indices in data  
    Matrix = [Matrix[starts[pro]:ends[pro]] for pro in range(nprocs)]
    
    # print("div matrix")
    # print(Matrix)
else:
    
    data = None
print('Process {} rec vec:'.format(rank), vec)
Matrix = comm.scatter(Matrix, root=0)    
print('Process {} has data:'.format(rank), Matrix)



ans_vector=comm.gather(sp.matix_vec_mul_original(Matrix,vec), root=0)
    
    

if rank == 0:
    
    print(np.concatenate(ans_vector))
    print('computed in {:.3f} sec'.format(time.time() - t0))
    
    
    
# print(time.time()-t0)