
def paragraph1():
    print('paragraph 1')
    first = 7
    second = 44.3
    print(f'{first} + {second} = {first + second}')
    print(f'{first} * {second} = {first * second}')
    print(f'{second} / {first} = {second / first}')


def paragraph2():
    print('paragraph 2')
    """what will be the end values of a, b, and c
    a = 8
    a = 17
    a = 9
    b = 6
    c = a + b
    b = c + a
    b = 8"""
    
    print(f'end values will be: a=9, b=8, c=15')


def paragraph3():
    print('paragraph 3')
    """is there a difference between name = 'john' and name = "john" ?"""

    print('no difference, in Python double quotes (\") and single quotes (\') are the same')


def paragraph4():
    print('paragraph 4')
    """what is the issue with the code below? suggest an edit
    my_number = 5 + 5
    print("result is: " + my_number)"""

    print('the variable "my_number" is an int bit in print method a str expected')
    print('the solution can be a string interpolation or a casting')


def paragraph5():
    print('paragraph 5')
    """what will be the output of
    x =5
    y = 2.36
    print(x+int(y))"""
    print('the output will be 7, because a casting of a string that represents a double/float converts it to integer '
          'without the values after the point')


def paragraph6():
    print('paragraph 6')
    '''fix the following code, without changing a or b:
    a = 8
    b = "123"
    print(a+b)'''
    a = 8
    b = "123"
    print(str(a + int(b)))


if __name__ == '__main__':
    paragraph1()
    paragraph2()
    paragraph3()
    paragraph4()
    paragraph5()
    paragraph6()


