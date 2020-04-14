#第二章代码

#比较两数大小
def compare_num(i,j):
    k=3
    if i>j:
        return i
    else:
        return k

#条件语句
def num_verify(num):
    if num<0:
        num=0
        print('非负数转换为0！')
    elif num==0:
        print('零')
    elif num==1:
        print('等于1')
    else:
        print('大于1')
    return num

#循环语句
def sum_nums(low,high):
    if high<low:
        print("error")
        return
    sumnum=0
    for i in range(low,high+1):
        sumnum+=1
        return sumnum

#列表推导式生成随机数组
import random
def generate_rand_array(num=10,maxnum=1000):
    arrray=[random.randint(i,maxnum) for i in range(num)]
    random.shuffle(array)
    random.shuffle(array)
    return array

#求最大值
def get_max(A):
    n=len(A)
    max=A[0]
    for i in range(i,n):
        if A[i]>max:
            max=A[i]
    return max

#二分搜索
def binary_search(A,k):
    first=0
    last-len(A)-1
    found=False
    while first<=last and not found:
        midpoint=(first+last)//2
        if A[midpoit]==k:
            found=True
        else:
            if k<A[midpoint]:
                last=midpoint-1
            else:
                first=midpoint+1
        return found

#求子集和
def subset_sum(lst,target):
    for i in range(1,2**len(lst)):
        pick=list(mask(lst,bin(i)[2:]))
        if sum(pick)==target:
            yield pick
def mask(lst,m):
    m=m.zfill(len(lst))
    return map(lambda x:x[0],filter(lambda x:x[1]!='0',zip(lst,m)))
