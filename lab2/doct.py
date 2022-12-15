import re
import os
import cmath
import sys
import argparse
import math

def bts(bool):
    """
    возвращает строковое представление значений bool типа
    >>> bts(2==2)
    'True'
    >>> bts(2==2)
    'False'
    >>> bts(2!=2)
    'False'
    """
    return (str(bool))

def odd_sort(num_list):
    """
    возвращает список, где нечетные числа отсортированы
    >>> odd_sort([7,8,1])
    [1, 8, 7]
    >>> odd_sort([5,8,6,3,4])
    [3, 8, 6, 5, 4]
    """
    even_dict = {}
    for idx, num in enumerate(num_list):
        if num%2 == 0:
            even_dict[idx]=num
    odd_list = [num for num in num_list if num%2==1]
    odd_list.sort()
    for key in even_dict.keys():
        odd_list.insert(key, even_dict[key])
    return odd_list

def sr(str):
    """
    возвращает строку в реверсе
    >>> sr('Hello, world!')
    '!dlrow ,olleH'
    >>> sr('key')
    'key'
    """
    return (str)[::-1]


def nums(num):
    """
    возвращает число в виде (nm)+, где n количество повторений числа m
    >>> nums(1)
    11
    >>> nums(0)
    10
    >>> nums(21)
    1211
    >>> nums(9000)
    1930
    >>> nums(222222222222)
    122
    >>> nums(3333444112)
    43342112
    """
    pattern = r'[0]+|[1]+|[2]+|[3]+|[4]+|[5]+|[6]+|[7]+|[8]+|[9]+'
    ans = []
    expressions = re.findall(pattern=pattern, string=str(num))
    for ex in expressions:
        ans+=str(len(ex))+str(ex[0])
    return int(''.join(ans))

def camel2kebab(text):
    """
    возвращает строку, переформатированню из camelCase в kebab-case
    >>> camel2kebab('camelsHaveThreeHumps')
    'camels-have-three-humps'
    >>> camel2kebab('allYourBaseAreBelongToUs')
    'all-your-base-are-belong-to-us'
    """
    upper_chars = [char for char in text if char.isupper()]
    for char in upper_chars:
        text = text.replace(char, f'-{char.lower()}')
    return str(text)

def sc(text):
    """
    возвращает количество одинаковых символов без учета регистра
    >>> sc('abcde')
    0
    >>> sc('aabcde')
    1
    >>> sc('aabBcde')
    2
    >>> sc('aabbccde')
    3
    >>> sc('indivisibilities')
    2
    """
    text = text.lower()
    dubl_count = 0
    for char in set(text):
        char_count = text.count(char)
        if char_count > 1:
            dubl_count += 1
    return dubl_count
    
def triangle(size):
    """
    возвращает треугольник высотой size
    >>> triangle(5)
    '    *   ***  ***** ****************'
    """
    size = round(size)
    result = ''
    for idx in range(1,size+1):
        spaces = ' '*(size-idx)
        star_num = idx+(idx-1)
        result += spaces+'*'*star_num
    return str(result)

def pnsum(list):
    """
    возвращает суммму положительных элементов списка
    >>> pnsum([])
    0
    >>> pnsum([2, -4, 5, 1, 0, -10])
    8
    >>> pnsum([2, -4, 5, 1, 0, -10])
    -6
    """
    sum = 0
    if len(list) > 0:
        for i in list:
            if i > 0:
                sum += i
    else:
        sum = 0
    return sum        

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
    """
    >>> quadratic_solver(2, 5, 3, True)
    'solutions: (-1+0j), (-1.5+0j)'
    >>> quadratic_solver(2, 5, 3, True)
    'solutions: (-1+0j), (1.5+0j)'
    """
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
