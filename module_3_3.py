def print_params(a= 1, b= "Hello", c= True):
    print(a, b, c)


print_params(b= 25, c= [1,2,3])
values_list = 50, [2, 3.1, False], "Hi"
values_dict = {'a': 10, 'b': 20, 'c': 30}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = {'a': 666, 'c': 999}, ['Not False', 'Yes', True]
print_params(*values_list_2, 42)