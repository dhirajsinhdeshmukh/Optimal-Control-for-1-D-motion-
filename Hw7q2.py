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
    if step == 2:
       for i in states:
           cost_cont=[]
           for u , x_next in dict[i].items():
               cost=4*x_next + abs(u)
               cost_cont.append([round(cost,3),u])
           jj[a][i]=min(cost_cont)
    else:
        for i in states:
            cost_cont = []
            for u, x_next in dict[i].items():
                cost = j_opt(round(x_next,3),step) + abs(u)
                cost_cont.append([cost,u])
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
    nstep=2
    opt_con_cst()

    for i in range(2,0,-1):
         optcost_st(i)

    #[print(jj[k]) for k in range(19,0,-1)]
    # print(jj[0][1])

    # question 2.a
    for pt in [0,1]:
        plt.figure()
        for key,value in jj[pt].items():


            plt.plot(key,value[0],'*')
            plt.xlabel("x")
            plt.ylabel("j")

    plt.show()

    # question 2.b
    u=[]
    initial_st=1
    for i in range(nstep):
        u.append(j_cont(initial_st,i))
        initial_st=(initial_st - (0.4*initial_st*initial_st) + u[i])

    print('initial state = 1   u=', u)
    print('Cost of J 0,2(x(0)=1) =',jj[0][1][1])