while True:
    try:
        age=int(input('enter age:'))

    except ValueError:
        print('you enterd wrong datatype ')

    except: 
        print('unexpected error')

    else:
        print(f'user input=={age}')

    finally:
        print('finally blocks.....')