a=[[1,2,3],[0,2,1],[1,3,2],[0,2,1]]
b=[[1,3,0],[0,1,3],[1,2,2]]

c=[[1,1],[2,3],[-1,-2]]
d=[[1,2,3],[4,5,6]]

e=[[1,2,3],[4,5,6]]
k=[[1,1],[2,3],[-1,-2]]



def get_row(t):
    return len(t)

def get_column(t):
    return len(t[0])



def f(t1,t2): #creates a sample matrix of proper output size
    res=[]
    for i in range(0,get_row(t1),1):
        res.append([])
    for i in range(0,len(res),1):
        for j in range(0,get_column(t2),1):
            res[i].append(j)
    return res


def h(t): #helper for invert
    res=[]
    for i in range(0,get_column(t),1):
        res.append([])
    for i in range(0,len(res),1):
        for j in range(0,get_row(t),1):
            res[i].append(j)
    return res


def invert(t):
    res=h(t)
    for i in range(0,get_column(t),1):
        for j in range(0,get_row(t),1):
            res[i][j]=t[j][i]
    return res




def g(t1,t2): #helper in product, multiplies row of t1 with row of t2
    res=0
    for i in range(0,len(t1),1):
        res=res+t1[i]*t2[i]
    return res


def product(t1,t2):
    if get_column(t1)!=get_row(t2):
        return 'Matrix multiplication not possible'
    else:
        res=f(t1,t2)
        t2=invert(t2)
        for i in range(0,get_row(t1),1):
            for j in range(0,get_row(t2),1):
                res[i][j]=g(t1[i],t2[j])
        return res


            

