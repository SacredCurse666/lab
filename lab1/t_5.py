def sc(string):
    string = string.lower()
    count = 0
    print(string)
    sym_set = list(set(string))
    for i in sym_set:
        cncdnc = 0
        for j in string:
            if i == j:
                cncdnc +=1
            if cncdnc > 1:
                count+=1
                break
    print(count)
    
def main():
    sc('abcde')
    sc('aabcde')
    sc('aabBcde')
    sc('aabbccde')
    sc('indivisibilities')
    
if __name__ == '__main__':
    main()