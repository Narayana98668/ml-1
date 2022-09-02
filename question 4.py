it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

len_of_it = len(it_companies)

print(len_of_it)

it_companies.add('Twitter')

print(it_companies)

it_companies.update({'hcl', 'tcs', 'aptein'})

print(it_companies)

it_companies.remove('Microsoft')

print(it_companies)
# Whenever we use remove method to remove any element which i not present in the set, it will throw an error.
# whereas discard will not throw any error eventhough there is no element found.


A = {19, 22, 24, 20, 25, 26}

B = {19, 22, 20, 25, 26, 24, 28, 27}

C = A.union(B)

print(C)

A_inter_B = A.intersection(B)

print(A_inter_B)

subset_check = A.issubset(B)

print(subset_check)

disjoint_check = A.isdisjoint(B)

print(disjoint_check)

E = A.union(B)

D = B.union(A)

print(E)

print(D)

del A

del B

del C

del D

del E

age = [22, 19, 24, 25, 26, 24, 25, 24]

len_age = len(age)

age_set = set(age)

len_age_set = len(age_set)

diff_age = len_age - len_age_set

print(diff_age) 