def triangle(size):
    print(f'triangle({size})')
    for i in range(size):
        print(' ' * (size - i - 1), end='')
        if i == 0:
            print('*')
        else: 
            print('*' * (2*i+1))
    print(end='\n')       
    
    
def main():  
    triangle(5)
    triangle(1)
    triangle(3)
    
if __name__ == '__main__':
    main()    