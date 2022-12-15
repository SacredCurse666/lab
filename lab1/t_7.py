import re

def nums(num):
    pattern = r'[0]+|[1]+|[2]+|[3]+|[4]+|[5]+|[6]+|[7]+|[8]+|[9]+'
    ans = []
    expressions = re.findall(pattern=pattern, string=str(num))
    for ex in expressions:
        ans+=str(len(ex))+str(ex[0])
    return int(''.join(ans))
        
def main():
    print(nums(1))
    print(nums(0))
    print(nums(21))
    print(nums(9000))
    print(nums(222222222222))
    print(nums(3333444112))

if __name__ == '__main__':
    main()