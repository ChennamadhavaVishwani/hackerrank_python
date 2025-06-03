

def split_and_join(line):
    newstr = ""
    line = line.split()
    
    newstr = "-".join(line)
    return newstr    

if __name__ == '__main__':
    line = str(input())
    result = split_and_join(line)
    print(result)
