immutable_var = (1 ,'a', 'mambo')
print('immetable tuple:', immutable_var)
try:
    immutable_var [0] = 5
except TypeError as e:
    print('error: ', e)
mutable_list=[1, 'a', 'mambo']
mutable_list[2]='modified'
print('mutable_list:', mutable_list)




