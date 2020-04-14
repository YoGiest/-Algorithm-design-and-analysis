#第四章代码

#筹措善款的递归算法
def collect_contribution(n):
    if (n<=100):
        return 100
    else:
        friends=find_friend()
        sum=0
        for(i=0;i<length(friends);i++):
        sum+= collect_contributions(n/10)
    return sum

#斐波那契额数列的递归算法
def fib.rec(n):
    if n<=1:
        f=n
    else:
        f=fib_rec(n-1)+fib_rec(n-2)
    return f
if __name__=='__main__':
    num=24
    print('{0：5}==>{1:10d}'.format('fib('+str(num)+')',fib_rec(num)))

#回文算法
def is_palindrome(s):
    if len(s)<=1:
        return True
    else:
        return s[0]==s[-1] and is_palindrome(s[1:-1])

#判断中文字符串的回文算法
def is_palindrome(s):
    if len(s)<=1:
