def coin_change(coins,amount):
    coins.sort(reverse=True)
    count=0
    result=[]

    for coin in coins:
        while amount >= coin:
            amount -= coin
            result.append(coin)
            count +=1
    return count , result
coins=[1,2,5,10]
amount = 18
print(coin_change(coins,amount))