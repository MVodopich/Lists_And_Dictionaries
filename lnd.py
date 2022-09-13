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

students[0]["first_name"] = "Bryant"
print(students)

sports_directory["soccer"][0] = "Andres"
print(sports_directory)

z[0]["y"] = 30
print(z)

students1 = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
#iterateDictionary(students) 
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
#first_name - Michael, last_name - Jordan
#first_name - John, last_name - Rosales
#first_name - Mark, last_name - Guillen
#first_name - KB, last_name - Tonel

#2
def iterate_dictionary(some_list):
    for i in students1:
        print(i["first_name"])
        print(i["last_name"])

print("2")
print(iterate_dictionary(students1))
print("---------------------------------------------------------")

#3
def iterate_dictionary2(key_name, some_list):
    for i in range(len(some_list)):
        for key, val in some_list[i].items():
            if key == key_name:
                print(val)
print("3")
iterate_dictionary2("first_name", students1)
print("------------------------------------------------------")

#4
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

"""
printInfo(dojo)
# output:
7 LOCATIONS
San Jose
Seattle
Dallas
Chicago
Tulsa
DC
Burbank
    
8 INSTRUCTORS
Michael
Amy
Eduardo
Josh
Graham
Patrick
Minh
Devon
"""

#print the name of each key along with the size of its lists, 
#and then print the associated values within each key's list 




list = ("instructors", "locations")


some_dict = dojo



def printInfo(some_dict):
    for key, val in some_dict.items():
        print(len(val))
    for key, val in some_dict.items():
        print(key)  
    for val in some_dict["locations"]:
        print(val)
    for val in some_dict["instructors"]:
        print(val)


printInfo(dojo)





"""

"""