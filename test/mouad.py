import numpy as np 

w1  = -0.994    
w2  = -0.951
w3  = -0.866
w4  = -0.743
w5  = -0.587
w6  = -0.406
w7  = -0.207
w8  = 0
w9  = 0.207
w10 = 0.406
w11 = 0.587
w12 = 0.743
w13 = 0.866
w14 = 0.951
w15 = 0.994

line = [w1 ,w2 ,w3 ,w4 ,w5 ,w6 ,w7 ,w8 ,w9 ,w10 ,w11 ,w12 ,w13 ,w14 ,w15]

A =  np.matrix([[ line[j]**i for j in range(15)] for i in range(0,15)])
Y =  np.matrix([[ 2/i if i%2 else 0 ] for i in range(1,16)])

print(A.I @ Y)
# print(A @ A.I @ Y )
