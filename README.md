# Simplex-method-by-BigM-
V2.0
----
Esta version culmina la solucion incluyendo resultados y precio sombra de cada una de las restricciones

     resultados(A,bas,n,pos,pr)  : se ingresa tableu(A), listado de variables basicas(bas), numero de variables(n), posicion inicial de      bases(pos), tipo de problema('min' o 'max')

V1.0
----
Esta version añade rutinas de inversion de matrices y resolucion de ecuaciones.

    inv_matriz(A) : entrega como resultado matriz invertida

    res_ecuaciones(A,b) : entrega como resulado un vector de solucion de ecuaciones


V0.0
----
Optimizacion mediante el metodo SIMPLEX, version general utilizando BigM


Ejemplo:

      min -3x1 + x2 + x3
      s.a
      
      x1 - 2x2 +  x3 <= 11
    -4x1 +  x2 + 2x3 >=  3
    -2x1 +       +x3 =   1
    
            x1,x2,x3 >=  0
            

     Para correr:  corre_simplex(A,b,c,inecuaciones,problema)
     valores para inecuaciones :
       1 : '<='
      -1 : '>='
       0 : '='
     
     valores para problema :
       'max'
       'min'

     \>corre_simplex([[1,-2,1],[-4,1,2],[-2,0,1]],[-3,1,1],[11,3,1],[1,-1,0],'min')
     
     
  
