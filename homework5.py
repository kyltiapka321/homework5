my_list = ['apple', 'banana', 'orange', 'kiwi', 'plum']
print('List: ' + str(my_list))
print('First element: ' + str(my_list[0]))
print('Last element: ' + str(my_list[-1]))
print('Sublist:' + str(my_list[2:5]))
my_list[2] = 'Cake'
print('Modified list: ' + str(my_list))

my_dict = {'Nikita': 89896022325, 'Sash04ka': 89036555893, 'Baburex' : 89457427556, 'Ivasha' : 89457427556}
print('phone book: ' + str(my_dict))
print('phone number: ' + str(my_dict.get('Baburex')))
my_dict['Sash04ka'] = 89001112233
print('Modified phone book: ' + str(my_dict))
my_dict.update({'Tolik' : 89645896585})
print('Modified phone book: ' + str((my_dict)))
