from os import listdir

cook_book = {}
with open('recipes.txt', encoding='UTF-8') as file:
    for line in file:
        if line.strip().isdigit():
            list = []
            for i in range(0, int(line)):
                l = []
                ingr = {}
                l = file.readline().strip().split(' | ')
                ingr['ingredient_name'] = l[0]
                ingr['quantity'] = int(l[1])
                ingr['measure'] = l[2]
                list.append(ingr)
            cook_book[name_recipe] = list
        else:
            name_recipe = line.strip()


# print(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    ingr = {}
    for dish in dishes:
        for recipe in cook_book:
            if dish == recipe:
                for i in cook_book[recipe]:
                    if i["ingredient_name"] not in ingr:
                        ingr[i["ingredient_name"]] = {'measure': i['measure'], 'quantity': i['quantity'] * person_count}
                    else:
                        ingr[i["ingredient_name"]]['quantity'] += i['quantity']
    return ingr


# get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

def sort_files():
    files = listdir('files_for_sort')
    txt_files = filter(lambda x: x.endswith('.txt'), files)
    file_dict = {}
    for file in txt_files:
        with open(f'files_for_sort/{file}', encoding='UTF-8') as f:
            row_list = f.readlines()
            file_dict[file] = len(row_list)
    sort_dict = {}
    sort_keys = sorted(file_dict, key=file_dict.get)
    for w in sort_keys:
        sort_dict[w] = file_dict[w]
    with open('sorted_file.txt', 'a', encoding='UTF-8') as s_f:
        for file in sort_dict.keys():
            with open(f'files_for_sort/{file}', encoding='UTF-8') as f:
                row_list = f.readlines()
                s_f.write(f'{file}\n{sort_dict[file]}\n')
                for row in row_list:
                    s_f.write(row)
            s_f.write(f'\n')

# sort_files()
