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

def main():
    print(odd_sort([7,8,1]))
    print(odd_sort([5,8,6,3,4]) )   

if __name__ == '__main__':
    main()