series=[]
def fibanocci_series(n):
    a=0
    b=1
    for i in range(n+1):
        series.append(a)
        a,b=b,a+b
    return ", ".join(map(str,series))
def main():
    n = int(input())
    print(fibanocci_series(n))
if __name__=='__main__':
    main()
