#6.6 计算最近距离的遍历算法
import math
def closestpair_simple(X,n):#X为点集，n为点的个数
    min_d = distance(X[0],X[1])
    for i,(x,y) in enumerate(X):
        for j in range(i+1,n):
            if distance(X[i],X[j])<min_d:
                min_p=[X[i],X[j]]
                min_d=distance(X[i],X[j])
    return min_p,min_d

def distance(a,b):
    return math.sqrt(math.pow((a[0]-b[0]),2)+math.pow((a[1]-b[1]),2))


#6.7

def closest(P,n):
    X=list(P)
    Y=list(P)
    X.sort()
    Y=sort_y(Y)
    return closest_pair(X,Y,n)

#6.8
def closest_pair(X,Y,n):
    if n<=3:
        return brute_force(X,n)
    mid = n/2
    Y_left=[]
    Y_right=[]
    for P in Y:
        if p in X[:mid]:
                Y_left.append(p)
            else:
                Y_right.append(p)
    dis_left = closest_pair(X[mid:],Y.left,mid)
    dis_right = closest_pair(X[mid:],Y.right,n-mid)
    min_dis = min(dis_left,dis_right)
    strip=[]
    for(x,y) in Y:
        if abs(x-X[mid][0])<mid_dis:
            strip.append((x,y))
        return min(min_dis,strip_closet(strip,min_dis))

#6.9
