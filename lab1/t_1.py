def bts(bool):
    return (str(bool), type(str(bool)))


def main():
    print('2 == 2')
    print(bts(2 == 2))
    print('2 != 2')
    print(bts(2 != 2))
    
if __name__ == '__main__':
    main()