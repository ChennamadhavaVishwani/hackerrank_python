# Enter your code here. Read input from STDIN. Print output to STDOUn
n = int(input())

countries = set()
for i in range (n):
    country = input()
    countries.add(country)
    
print(len(countries))    
    