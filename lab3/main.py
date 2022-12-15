from fastapi import FastAPI
from pydantic import BaseModel
import math
import cmath
import re
from typing import List, Union 

app = FastAPI()
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

class Numlist(BaseModel):
    numlist: List[Union[int, float]]

class Solver(BaseModel):
    a: float
    b: float
    c: float
    complex: bool 

@app.post('/items/')
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({'price_with_tax': price_with_tax})
    return item_dict

@app.get('/')
def root():
    return {'message': 'hello, world!'}

@app.get('/items/{item_id}')
def read_item(item_id: int, q: str | None = None):
    if q:
        return {'item_id': item_id, 'q':q}
    return {"item_id": item_id}

@app.get('/bts/{boolean}')
def bts(boolean: bool):
    return str(boolean)

@app.get('/sr/{string}')
def sr(string):
    return string[::-1]

@app.post('/pnsum/')
async def pnsum(numlist: Numlist):
    sum = 0
    for i in numlist.num:
        print(i)
        if int(i) > 0:
            sum += int(i)
    return sum

@app.get('/triangle/{size}')
def triangle(size: int) -> str:
    size = round(size)
    result = ''
    for idx in range(1,size+1):
        spaces = ' '*(size-idx)
        star_num = idx+(idx-1)
        result += spaces+'*'*star_num+'\n'
    return result
    
@app.get('/sc/{text}')    
def sc(text: str) -> str:
    text = text.lower()
    dubl_count = 0
    for char in set(text):
        char_count = text.count(char)
        if char_count > 1:
            dubl_count += 1
    return dubl_count

@app.get('/c2k/{text}')
def camel2kebab(text: str) -> str:
    upper_chars = [char for char in text if char.isupper()]
    for char in upper_chars:
        text = text.replace(char, f'-{char.lower()}')
    return text
    
@app.get('/nums/{num}')    
def nums(num: int) -> int:
    pattern = r'[0]+|[1]+|[2]+|[3]+|[4]+|[5]+|[6]+|[7]+|[8]+|[9]+'
    ans = []
    expressions = re.findall(pattern=pattern, string=str(num))
    for ex in expressions:
        ans+=str(len(ex))+str(ex[0])
    return int(''.join(ans))

@app.post('/odd_sort/')
async def odd_sort(numlist: Numlist):
    even_dict = {}
    for idx, num in enumerate(numlist.numlist):
        if num%2 == 0:
            even_dict[idx]=num
    odd_list = [num for num in numlist.numlist if num%2==1]
    odd_list.sort()
    for key in even_dict.keys():
        odd_list.insert(key, even_dict[key])
    return odd_list

@app.post('/solver/')
async def quadratic_solver(solver: Solver):
    a = solver.a
    b = solver.b
    c = solver.c
    compl = solver.complex
    d = b**2-4*a*c
    if compl == False:
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
