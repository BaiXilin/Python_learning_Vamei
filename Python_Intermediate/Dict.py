dic = {'tom':11, 'sam':57, 'lily':100}
print type(dic)
print(dic['tom'])
dic['tom'] = 30
print dic

dic = {}
print dic

#add an element in the dictionary
dic['lilei'] = 99
print dic

#print every value in the dic using loop
dic = {'lilei': 90, 'lily': 100, 'sam': 57, 'tom': 90}
for key in dic:
    print dic[key]

print dic.items()
