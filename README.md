# Simplex-method-by-BigM
Motor de optimizacion realizado con python, que utiliza la metodologia BigM para resolver por operaciones de algebra lineal, 
esta libreria no utiliza numpy, solo las rutinas simples de python.

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
            

  Para correr

     \>corre_simplex([[1,-2,1],[-4,1,2],[-2,0,1]],[-3,1,1],[11,3,1],[1,-1,0],'min')
     \>corre_simplex(A,b,c,ine,prob)
  
