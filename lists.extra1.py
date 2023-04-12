#1
list_languages = ['Norwegian', 'Ukrainian', 'Latvian', 'Bulgarian', 'French']
print(list_languages)

sorted_list_languages = sorted(list_languages)
print(sorted_list_languages)

list_languages.reverse()
print(list_languages)

list_languages.sort()
print(list_languages)

#2
numbers = "2 -1 9 6"
numbers_list = numbers.split()
sum = 0
for numbers in numbers_list:
    sum += int(numbers)

print(sum)

#3
cities = ['Budapest', 'Rome', 'Istanbul', 'Sydney', 'Kyiv', 'Hong Kong']
extra_and = ", ".join(cities[:5]) + " and " + cities[5]
print(extra_and)

#4
numbers = "1 2 3 4 5"
numbers_list = numbers.split()
print(numbers_list)

numbers_list.reverse() 
print(numbers_list)

combining = ''.join(numbers_list)
print(combining)

#5
family_members = ['mom', 'dad', 'son', 'daughter', 'grandmom']
print(family_members)

family_members.remove('grandmom')
print(family_members)

family_members.append('stepson')
print(family_members)

family_members.insert(4, 'stepdaughter')
print(family_members)

print(len(family_members))