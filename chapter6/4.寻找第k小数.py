#得到第k小的数的分治算法
def select_fct(array,k):
    if len(array)<=10:
        array.sort()
        return array[k]
    pivot = get_pivot(array)
    array_lt,array_gt,array_eq = patition_array(array,pivot)
    if k<len (array_lt):
        return select_fct(array_lt,k)
    elif k <len(array_lt)+len(array_eq):
        return array_eq[0]
    else:
        normalized_k = k - (len(array_lt)+len(array_eq))
        return select_fct(array_gt,normalized_k)

#得到数组的支点数x
