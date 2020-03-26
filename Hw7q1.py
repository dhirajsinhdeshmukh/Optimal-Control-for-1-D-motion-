import numpy as np
import matplotlib.pyplot as plt
from _collections import OrderedDict
states = list(map(lambda x : round(x,3),np.arange(0, 1.5, 0.5)))
controls = list(map(lambda x : round(x,3),np.arange(-0.4, 0.6, 0.2)))
new_st = []
dict=OrderedDict()
jj={}



def opt_con_cst():

    for i in states:
        dict[i]={}
        for j in controls:
            a= (i - (0.4*i*i) + j)
            if a<=1 and a>=0:
                dict[i][j]=round(a,3)


#
def optcost_st(step):
    a=step-1
    jj[a]={}
    if step == 2:
       for i in states:
           cost_cont=[]
           for u , x_next in dict[i].items():
               cost=4*x_next + abs(u)
               cost_cont.append(round(cost,3))
           jj[a][i]=min(cost_cont)
    else:
        for i in states:
            cost_cont = []
            for u, x_next in dict[i].items():
                cost = j_opt(round(x_next,3),step) + abs(u)
                cost_cont.append(round(cost,3))
            jj[a][i] = min(cost_cont)


def j_opt(x_nt,step):
    b=np.trunc(x_nt/0.5)
    a=(x_nt)-(b*0.5)
    if a==0:
       return jj[step][x_nt]

    else:
        m=(jj[step][round((b+1)*0.5,3)])
        n=(((x_nt-round((b+1)*0.5,3))/(round((b)*0.5,3)-round((b+1)*0.5,3))))
        l=((jj[step][round((b)*0.5,3)])-(jj[step][round((b+1)*0.5,3)]))

        return ((m)+(n*l))




if __name__ == "__main__":
    nstep=2
    opt_con_cst()


    for i in range(2,0,-1):
         optcost_st(i)

    print(jj)

