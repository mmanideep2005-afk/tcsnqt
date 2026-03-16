primes=[]
def primes_list(n):
    for i in range(1,n+1):
        divisors=0
        for j in range(1,i+1):
             if i%j==0:
                 divisors+=1
        if divisors==2:
            primes.append(i)
    return ", ".join(map(str,primes))
def main():
    n=int(input())
    print(primes_list(n))
if __name__=='__main__':
    main()
