while True:
    try:
        age=int(input('enter age:'))
        break

    except ValueError:
        print('you enterd wrong datatype ')

    except: 
        print('unexpected error')

if age>18:
    print('you can watch movie')
else:
    print('you cant watch movie')

