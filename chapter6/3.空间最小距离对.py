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
#空间最小距离点对的辅助函数
def strip_closest(strip,d):
    min_d = d
    for i,(x,y) in enumerate(strip):
        for j in range(i+1,8):#只需要考虑最多7个点
            if i+j < len(strip):
                temdis = distance(strip[i],strip[j])
                if temdis < min_d:
                    min_d = temdis
    return min_d

#计算两点之间的距离
def distance(a,b):
    return math.sqet(math.pow((a[0]-b[0]),2)+math.pow((a[1]-b[1]),2))

#按照y轴坐标进行排序
def sort_y:(tuples):
    return sorted (tuples,key=lambda last: last[-1])

#当点数小于3时，直接计算最小距离
def brute_force(X,n):
    min_d = distance(X[0],X[1])
    for i,(x,y) in enumerate(strip):
        for j in range(i+1,n):
            if distance(X[i],X[j]) < min_d:
                min_d = distance(X[i],X[j])
    return min_d
