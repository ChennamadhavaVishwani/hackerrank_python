import re

def count_substring(string, sub_string):
    pattern = f"(?={re.escape(sub_string)})"
    return (len(re.findall (pattern, string)))
    
    
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)