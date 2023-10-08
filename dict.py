list = [{'cool':'spoon', 'rupture': 'algo'},{'cool':'splash','rupture':'control'}]

def iterate(co):
    for i in list:
        for key,value in enumerate(i):
            key = i[value]
            print(key)

iterate(list)