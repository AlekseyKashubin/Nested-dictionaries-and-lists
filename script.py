

#1

x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]


x[1][0] = 15
print(x)
print('----------------------------')
students[0]['last_name'] = 'Bryant'
print(students[0])
print('----------------------------')
sports_directory ['soccer'][0] = 'Andres'
print(sports_directory['soccer'])
print('----------------------------')
z[0]['y'] = 30
print(z)




#2
print('----------------------------')
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]




def iterateDictionary_2lines(some_list):
    for dict in some_list:
        for key, val, in dict.items():
            print(key, '-', val)
    return some_list




def iterateDictionary(some_list):
    for dict in some_list:
        output = ''
        for key, val, in dict.items():
            output += f'{key} - {val},'
        print(output)
    return some_list



iterateDictionary_2lines(students) 
print('----------------------------')
iterateDictionary(students) 
# # should output: (it's okay if each key-value pair ends up on 2 separate lines;
# # bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel


#3

print('----------------------------')
def iterateDictionary2(key_name,some_list):
    for val in some_list:
        print(val[key_name])
                
iterateDictionary2('first_name', students)
print('----------------------------')
iterateDictionary2('last_name', students)


# # Michael
# # John
# # Mark
# # KB


# # Jordan
# # Rosales
# # Guillen
# # Tonel






#4  
print('----------------------------')


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key in some_dict:
        print(len(some_dict[key]),key)
        for item in some_dict[key]:
            print(item)



printInfo(dojo)




# # output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon




