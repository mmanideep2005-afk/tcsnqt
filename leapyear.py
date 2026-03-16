def leap_year(start,end):
    leap=[]
    for i in range(start,end+1):
        if (i%4==0 and i%100!=0) or i%400==0:
            leap.append(i)
    return ", ".join(map(str,leap))
def main():
    start=int(input())
    end=int(input())
    print(leap_year(start,end))
if __name__=='__main__':
    main()
    
