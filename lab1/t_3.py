def pnsum(list):
    sum = 0
    if len(list) > 0:
        for i in list:
            if i > 0:
                sum += i
    else:
        sum = 0
    return sum        
    
def main():    
    print('list [2, -4, 5, 1, 0, -10]')
    print(pnsum([2, -4, 5, 1, 0, -10]))
    print('list []')
    print(pnsum([]))
    print('list [-5, -6, -1]')
    print(pnsum([-5, -6, -1]))
    
if __name__ == '__main__':
    main()    