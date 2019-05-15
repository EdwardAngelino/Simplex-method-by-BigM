import math, copy
def pivot(A, pivot_index):
        ''' Perform operations on pivot.
        '''
        T=copy.deepcopy(A)
        i,j = pivot_index[0]-1,pivot_index[1]-1
        pivot = T[i][j]
        T[i] = [element / pivot for
                           element in T[i]]
        for index, row in enumerate(T):
           if index != i:
              row_scale = [y * T[index][j]
                          for y in T[i]]
              T[index] = [x - y for x,y in
                                     zip(T[index],
                                         row_scale)]
        return T
def ver(A):
	for k in A:
		for j in k:
		   val = redondea(j)
		   print('{0:7.1f}'.format(val),end='')
		print()
		 
def vertableu(AA,vbase,vvar):
    A = copy.deepcopy(AA)
    var=copy.deepcopy(vvar)
    base = copy.deepcopy(vbase)
    base.append('z ')
    print('       ',end='')
    for i in var:
      print('{0:7}'.format(i),end='')
    print()
    for k in range(0,len(A)):
      print(base[k],end='')
      for j in range(0,len(A[k])):
        val = redondea(A[k][j])
        print('{0:7.1f}'.format(val),end='')
      print()     

def redondea(x):
	x = math.ceil(x*10000)/10000
	return x
			
def appendcol(T,vc):
    A=copy.deepcopy(T)
    b=copy.deepcopy(vc)
    for i in range(0, len(A)):
      A[i] += [b[i]]  #añade al final de la suma
    return A

def tableu(AA,bb,cc, inq, pr):
    A=copy.deepcopy(AA)
    b=copy.deepcopy(bb)
    c=copy.deepcopy(cc)
    ineqq=copy.deepcopy(inq)
    prob=copy.deepcopy(pr)
    
    #las listas de variables
    variables=[]
    base=[]
    posbase=[]
    n = len(c)
    m = len(A)

    #inicializacion de variables
    for j in range(0, len(c)):  #c tiene la cantidad de variables
        variables.append(f"x{j+1}")
    c = [x*-1 for x in c]  #para minimizacion
    M = 100
    if prob == 'max' :
        c = copy.deepcopy(cc)
    A.append(c)   #añade al final
    b.append(0)
    zero=[0.0]*len(b) 
    naux=0
    nslack=0

    #construccion de tableu
    for i in range(0,len(ineqq)):
      A=appendcol(A,zero)
      if ineqq[i] == -1:
          A[i][n+nslack+naux]=-1
          variables.append(f"s{nslack+1}")
          nslack +=1
          #bigM aux
          A=appendcol(A,zero)
          A[i][n+nslack+naux]=1
          variables.append(f"a{naux+1}")
          base.append(f"a{naux+1}")
          A[m][n+nslack+naux]=-M
          naux +=1          
      elif ineqq[i] == 0:
          A[i][n+nslack+naux]=1
          variables.append(f"a{naux+1}")
          base.append(f"a{naux+1}")
          A[m][n+nslack+naux]=-M
          naux +=1          
      elif ineqq[i] == 1:
          variables.append(f"s{nslack+1}")
          base.append(f"s{nslack+1}")
          A[i][n+nslack+naux]=1
          nslack +=1
      posbase.append(n+nslack+naux)
    return (appendcol(A,b),variables,base,posbase)

def pivotabase(T,V):
    A=copy.deepcopy(T)
    pos=copy.deepcopy(V)
    for k in range(0,len(pos)):
      A=pivot(A,[k+1,pos[k]])
    return A
def vcol(A,cc):
    c=copy.deepcopy(cc)
    c-=1
    v=[]
    #print(c)
    for i in range(0,len(A)):
    	v.append(A[i][c])
    return v
def pivotec(vv):
    v=copy.deepcopy(vv)
    vmax=-1
    jmax=-2
    for j in range(0,len(v)-1):
      if v[j] > 0 and v[j] > vmax:
      	vmax = v[j]
      	jmax = j
    return jmax
def pivotef(vv,bb):
	  v=copy.deepcopy(vv)
	  b=copy.deepcopy(bb)
	  vmin = 99999999.99
	  imin = -2
	  for i in range(0,len(bb)-1):
	  	if v[i] != 0 and b[i]/v[i] > 0 and b[i]/v[i] < vmin:
	  		vmin = b[i]/v[i]
	  		imin = i
	  return imin
def indexpivote(AA):
    A=copy.deepcopy(AA)
    indexj=pivotec(A[len(A)-1])+1
    bb=vcol(A,len(A[0]))
    vv=vcol(A,indexj)
    indexi=pivotef(vv,bb)+1
    return [indexi,indexj]

def corre_simplex(A,b,c,ine,prob):
    print('c=',c)
    print('A=')
    ver(A)
    print('ineq=',ine)
    print('b=',b)
    print('Tableu inicial')
    (A,var,bas,pos)=tableu(A,b,c, ine, prob)
    vertableu(A,bas,var)
    print('Tableu')
    A=pivotabase(A,pos)
    vertableu(A,bas,var)
    #print('variables=',var)
    print('var.basicas=',bas)
    print('indice basicas',pos)
    print('----SIMPLEX----')
    for k in range(0,10):
      index=indexpivote(A)
      if index[0] > -1 and index[1] > -1:
        print('paso',k+1,': pivote encontrado=',index, sep='')
        A=pivot(A,index)
        bas[index[0]-1]=var[index[1]-1]
        vertableu(A,bas,var)

    
