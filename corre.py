from tools import *
#ejemplo 1
'''A = [[1,-2,1],
     [-4,1,2],
     [-2,0,1]]
c=[-3,1,1]
b=[11,3,1]
ine=[1,-1,0]
prob ='min' '''

'''A=[[1,1,0],
    [1,0,1],
    [0,1,1]]
c=[1,-1,3] 
b=[20,5,10]
ine=[1,0,-1] # 1:'<=', -1:'>=', 0:'='
prob='max' '''


A=[[1,1],[1,0],[0,1],[1,-2]]
b=[21,13,6,0]
c=[0.10,0.08]
ine=[1,1,-1,0]
prob='min'

corre_simplex(A,b,c,ine,prob)
#res_ecuaciones(A,b)
#inv_matriz(A)
