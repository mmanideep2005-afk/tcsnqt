
def find_pair(arr, target):
    seen = set()
    for num in arr:
        diff = target - num
        if diff in seen:
            return True
        seen.add(num)
    return False
def main():
    arr = [ 2, 7, 11, 13]
    target = 9
    print(find_pair(arr, target))
main()
