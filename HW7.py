import numpy as np
import matplotlib.pyplot as plt
from _collections import OrderedDict
states = list(map(lambda x : round(x,3),np.arange(0, 1.002, 0.002)))
controls = list(map(lambda x : round(x,3),np.arange(-0.4, 0.402, 0.002)))
new_st = []
dict=OrderedDict()
jj={}



def opt_con_cst():

    for i in states:
        dict[i]={}
        for j in controls:
            a= (i - (0.4*i*i) + j)
            if a<=1 and a>=0:
                dict[i][j]=round(a,5)


#
def optcost_st(step):
    a=step-1
    print(a)
    jj[a]={}
    if step == 20:
       for i in states:
           cost_cont=[]
           for u , x_next in dict[i].items():
               cost=4*x_next + abs(u)
               cost_cont.append([round(cost,5),u])
           jj[a][i]=min(cost_cont)
    else:
        for i in states:
            cost_cont = []
            for u, x_next in dict[i].items():
                cost = j_opt(round(x_next,3),step) + abs(u)
                cost_cont.append([round(cost,5),u])
            jj[a][i] = min(cost_cont)


def j_opt(x_nt,step):
    b=np.trunc(x_nt/0.002)
    a=(x_nt)-(b*0.002)
    if a==0:
       return jj[step][x_nt][0]

    else:
        m=(jj[step][round((b+1)*0.002,3)][0])
        n=(((x_nt-round((b+1)*0.002,3))/(round((b)*0.002,3)-round((b+1)*0.002,3))))
        l=((jj[step][round((b)*0.002,3)][0])-(jj[step][round((b+1)*0.002,3)][0]))

        return ((m)+(n*l))


def j_cont(x_nt,step):
    b=np.trunc(x_nt/0.002)
    a=(x_nt)-(b*0.002)
    if a==0:
       return jj[step][x_nt][1]

    else:
        m=(jj[step][round((b+1)*0.002,3)][1])
        n=(((x_nt-round((b+1)*0.002,3))/(round((b)*0.002,3)-round((b+1)*0.002,3))))
        l=((jj[step][round((b)*0.002,3)][1])-(jj[step][round((b+1)*0.002,3)][1]))

        return ((m)+(n*l))



if __name__ == "__main__":


    nstep=20
    opt_con_cst()

    for i in range(20,0,-1):
         optcost_st(i)

    #[print(jj[k]) for k in range(19,0,-1)]

    # question 3.a
    for pt in [0,1,18,19]:
        plt.figure()
        for key,value in jj[pt].items():


            plt.plot(key,value[0],'*')
            plt.xlabel("x")
            plt.ylabel("j")
    plt.show()

    # question 3.b
    print('cost for initial state =1 from j(0-20) is :',jj[0][1][0])

    # question 3.c
    for pt in [18,19]:
        plt.figure()
        for key,value in jj[pt].items():


            plt.plot(key,value[1],'*')
            plt.xlabel("x")
            plt.ylabel("j")

    plt.show()


    # question 3.d
    u=[]
    x=[]
    k1=np.arange(0,21,1)
    k2=np.arange(0, 20, 1)
    initial_st=1
    for i in range(nstep):
        x.append(round(initial_st,5))
        u.append(round(j_cont(initial_st,i),5))
        initial_st=(initial_st - (0.4*initial_st*initial_st) + u[i])
    x.append(round(initial_st, 5))
    l=sum(list(map(lambda y: abs(y) ,u)))
    cost=(4*x[20])+ l

    print('calculate cost using x* and u*  for intial state =1 is :',cost)

    plt.figure()
    plt.plot(k1,x)

    plt.figure()
    plt.plot(k2,u)

    plt.show()




