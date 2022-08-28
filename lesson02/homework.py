import requests

def paragraph1():
    # Create two variables name X and Y
    # a Print “BIG” if X is bigger than Y
    # b Print “small” if X is smaller than Y
    x = 1
    y = 2
    if x > y:
        print('BIG')
    elif x < y:
        print('small')
    else:
        print('equals')


def paragraph2():
    # Run a “for ” loop 5 times.
    # a.Print iteration number every time.
    for i in range(5):
        print(i)


def paragraph3():
    season = 1
    if season == 1:
        print('summer')
    elif season == 2:
        print('winter')
    elif season == 3:
        print('fall')
    elif season == 4:
        print('spring')
    else:
        print('invalid value')


def paragraph4():
    # given the code:
    # count = 1
    # while count < 11:
    #     print(count)
    #     count = count + 1
    #
    # how many times will the loop run?
    # answer: 10
    # what will be printed last?
    # answer: numbers 1 to 10
    pass


def paragraph5():
    age = 38
    lname_first_letter = 'T'
    # url = "https://currency-converter5.p.rapidapi.com/currency/convert"
    #
    # querystring = {"format": "json", "from": "AUD", "to": "CAD", "amount": "1"}
    #
    # headers = {
    #     "X-RapidAPI-Key": "****",
    #     "X-RapidAPI-Host": "currency-converter5.p.rapidapi.com"
    # }
    #
    # response = requests.request("GET", url, headers=headers, params=querystring)
    # currency = response.json()
    currency = 0.31
    flight = False
    appartment = 38
    print(age)
    print(lname_first_letter)
    print(currency)
    print(flight)
    print(appartment)
    print(currency+age)


def paragraph6():
    digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    print('what is your phone number?')
    phone_number = input()
    print(f'phone number: {phone_number}')
    print('in words: ')
    for i in phone_number:
        if not i.isnumeric():
            print('only digits supported')
            return
    for i in phone_number:
        print(digits[int(i)])


def say_hello():
    print('hello')


def calculate():
    print(5+3.2)


def paragraph7():
    say_hello()
    calculate()


def print_name(name: str):
    print(name)


def devide(number):
    print(number/2)


def paragraph8():
    print_name('ilia')
    devide(5)


def sum_numbers(number1, number2):
    return number1 + number2


def concat(word1, word2):
    return f'{word1} {word2}'


def paragraph9():
    sum = sum_numbers(5, 25)
    print(sum)
    concatenated = concat('ilia', 'tankelevich')
    print(concatenated)


if __name__ == '__main__':
    paragraph1()
    paragraph2()
    paragraph3()
    paragraph4()
    paragraph5()
    paragraph6()
    paragraph7()
    paragraph8()
    paragraph9()
