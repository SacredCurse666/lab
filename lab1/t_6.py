def camel2kebab(string):
    print(string)
    frmtd_string = []
    for i in string:
        if i.isupper() == True:
            i = '-' + i
        frmtd_string+=i
    print(''.join(frmtd_string).lower())


def main():
    camel2kebab('camelsHaveThreeHumps') 
    camel2kebab('allYourBaseAreBelongToUs')
    
if __name__ == '__main__':
    main()