def average(arr):
   
    distinct_elements = set(arr)           # remove duplicates
    avg = sum(distinct_elements) / len(distinct_elements)  # calculate average
    return round(avg, 3)    
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)