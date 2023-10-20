#nested dictionary
child1={'ram':2006}
child2={'shiv':2010}
child3={'krish':2015}
family={}
family={'child1':child1,'child2':child2,'child3':child3}
print(family)

print(family['child1'])
print(family['child1']['ram'])
