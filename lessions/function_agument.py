def function1(*get_list):
    for arg in get_list:
        print(arg)

function1([1,2,3,4,5,6,7,8,9,0])

def function2(**get_hash):
    for k in get_hash.keys():
        print(k, ':',get_hash.get(k))

function2(rathana = 2345, nana = 'A Phong')
print('Annotation: ',function2.__annotations__)
