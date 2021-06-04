

import numpy as np
from matplotlib import pyplot as plt

##-------- sprawdzenie czy element x,y miesci sie w kuli ---
def check_ball(x,y,m,r):
    if abs(x)**m + abs(y)**m < r**m:
       return 1
    else:
       return 0

def draw_ball(m):
    n= 100000
    ##------- losowanie współrzedych x,y 
    r_x = np.random.uniform(-1,1,n)
    r_y = np.random.uniform(-1,1,n)
    x=[]
    y=[]
    for k in range(n):
        ##---- jeżeli spełnia warunek, dodajemy do tablic, które naniesiemy na wykres
        if check_ball(r_x[k],r_y[k],m,1):
            x.append(r_x[k])
            y.append(r_y[k])
            
    plt.figure(figsize=(10,10))
    plt.plot(x,y,'bo')

draw_ball(100)







