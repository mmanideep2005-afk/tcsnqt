def lcm_gcd(a,b):
    temp=0
    if a<b:
        temp=a
        a=b
        b=temp
    s=a*b
    for i in range(a,s,a):
        if i%a==0 and i%b==0:   #lcm = a*b//gcd
            print(i)
            break
    for j in range(b,1,-1):
        if a%j==0 and b%j==0:   
            print(j)
            break
    return 'gcd returned'
def main():
    a,b = map(int,input().split())
    print(lcm_gcd(a,b))
if __name__=='__main__':
    main()
