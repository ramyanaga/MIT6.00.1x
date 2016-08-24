sup = {'a': 1, 'b': 3, 'c': 2}
l = 'a'
sup[l]-=1
print sup
del sup[l]
print sup

sum = [sup[l] for l in sup]
print sum