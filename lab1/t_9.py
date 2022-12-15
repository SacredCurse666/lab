import os
import t_1, t_2, t_3

def wtf(text, path):
    try:
        text = str(text)
        dir_path = os.path.dirname(path)
        os.makedirs(dir_path, exist_ok=True)
        with open(path, 'a') as file:
            file.write(text + '\n')   
    except Exception as e:
        print(e)

def main():
    wtf(text=t_1.bts(2==2), path='lab_1/1.txt')
    wtf(text=t_2.sr('Hello, Wolrd!'), path='lab_1/2.txt')
    wtf(text=t_3.pnsum([2, -4, 5, 1, 0, -10]), path='lab_1/3.txt')

if __name__ == '__main__':
    main()