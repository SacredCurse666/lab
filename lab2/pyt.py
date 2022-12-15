import re
import os
import cmath
import sys
import math
import pytest

def bts(bool):
    return (str(bool))

def sr(str):
    return (str)[::-1]

def pnsum(list):
    sum = 0
    if len(list) > 0:
        for i in list:
            if i > 0:
                sum += 1
    else:
        sum = 0
    return sum

def triangle(size):
    print(f'triangle({size})')
    for i in range(size):
        print(' ' * (size - i - 1), end='')
        if i == 0:
            print('*')
        else:
            print('*' * (2*i+1))
    print('\n')
    
def sc(string):
    string = string.lower()
    count  = 0
    print(string)
    sym_set = list(set(string))
    for i in sym_set:
        cncdnc = 0
        for j in string:
            if i == j:
                cncdnc +=1
            if cncdnc > 1:
                count +=1
                break

def camel2kebab(string):
    print(string)
    frmtd_string = []
    for i in string:
        if i.isupper() == True:
            i = '-' + i
        frmtd_string+=i
    print(''.join(frmtd_string).lower())
    
def nums(num):
    pattern = r'[0]+|[1]+|[2]+|[3]+|[4]+|[5]+|[6]+|[7]+|[8]+|[9]+'
    ans = []
    expressions = re.findall(pattern=pattern, string=str(num))
    for ex in expressions:
        ans+=str(len(ex))+str(ex[0])
    return int(''.join(ans))

def odd_sort(num_list):
    even_dict = {}
    for idx, num in enumerate(num_list):
        if num%2 == 0:
            even_dict[idx]=num
    odd_list = [num for num in num_list if num%2==1]
    odd_list.sort()
    for key in even_dict.keys():
        odd_list.insert(key, even_dict[key])
    return odd_list

def wtf(text, path):
    try:
        text = str(text)
        dir_path = os.path.dirname(path)
        os.makedirs(dir_path, exist_ok=True)
        with open(path, 'a') as file:
            file.write(text + '\n')   
    except Exception as e:
        print(e)
        
def quadratic_solver(a,b,c,complex):
    d = b**2-4*a*c
    if complex == False:
        if d < 0:
            return('no solutions')
        elif d == 0:
            x = -b/2*a
            return(f'solutions: {x}')
        else:
            x1 = (-b+math.sqrt(d))/(2*a)
            x2 = (-b-math.sqrt(d))/(2*a)
            return(f'solutions: {x1}, {x2}')
    else:
        x1 = (-b+cmath.sqrt(d))/(2*a)
        x2 = (-b-cmath.sqrt(d))/(2*a)
        return(f'solutions: {x1}, {x2}')

  
class TestClass:
    def test_1(self):
        assert bts((2==2)) == 'True'
    def test_2(self):
        assert bts((2!=2)) == 'False'
    def test_3(self):
        assert bts((2!=2)) == 'True'
    def test_4(sefl):
        assert sr('Hello, world!') == '!dlrow ,olleH'
    def test_5(self):
        assert sr('Hello, world!') == 'Hello, world!'
    def test_6(self):
        assert pnsum([2, -4, 5, 1, 0, -10]) == 3
    def test_7(self):
        assert pnsum([]) == 0
    def test_8(sefl):
        assert pnsum([-5, -6, -1]) == 0
    def test_9(sefl):
        assert pnsum([-5, -6, -1]) == 1
    def test_10(sefl):
        assert pnsum([-5, -6, -1]) == 'sdgfd'
    def test_11(sefl):
        assert triangle(3) == '  *  \n *** \n*****\n'
    def test_12(self):
        assert sc('abcde') == 0
    def test_13(self):
        assert sc('aabcde') == 1
    def test_14(self):
        assert sc('abcbcde') == 2
    def test_15(self):
        assert sc('abcbcde') == 0
    def test_16(self):
        assert camel2kebab('camelsHaveThreeHumps') == 'camels-have-three-humps'
    def test_17(self):
        assert camel2kebab('CamelsHaveThreeHumps') == 'camels-have-three-humps'
    def test_18(sefl):
        assert nums(0) == 10
    def test_19(sefl):
        assert nums(2232) == 221312
    def test_20(sefl):
        assert nums(2232) == 3213
    def test_21(self):
        assert odd_sort([5, 8, 6, 3, 4]) == [3, 8, 6, 5, 4]
    def test_22(self):
        assert odd_sort([5, 8, 6, 3, 4]) == [5, 8, 6, 3, 4]
    def test_23(self):
        assert odd_sort([5, 8, 6, 3, 4]) == '[3, 8, 6, 5, 4]'
    def test_24(self):
        assert quadratic_solver(2, 5, 3, True) == 'solutions: (-1+0j), (-1.5+0j)'
    def test_25(self):
        assert quadratic_solver(2, 5, 3, True) == 'solutions: (-1+0j), (1.5+0j)'