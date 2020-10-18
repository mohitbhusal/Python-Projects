


m = ""
def data(value):
    global m
    for info in value:
        m = m + info

        if info == ',':
            operation(m)
            #print(m)
            m = ''

        elif value[len(value)-1] == m[len(m)-1]:
            #print(m)
            operation(m)
            m=''






def operation(inner_value):

        if '-' in inner_value:
            if ',' in inner_value:
                start = inner_value[:inner_value.index('-')]
                end = inner_value[inner_value.index('-') + 1:inner_value.index(',')]
                print('start is', start)
                print('end is', end)

            else:
                start =inner_value[:inner_value.index('-')]
                end = inner_value[inner_value.index('-') + 1:]
                print('start is', start)
                print('end is', end)
        elif not '-' in inner_value:
             single_page = inner_value[:len(inner_value)-1]
             print('one page is',single_page)


b = '1,2-3,4-5,6,8-9'
data(b)