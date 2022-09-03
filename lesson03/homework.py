from typing import TextIO, AnyStr, List
from flask import Flask
from markupsafe import escape
from PIL import Image, ImageDraw


def paragraph1() -> None:
    try:
        a = 1/0
    except ZeroDivisionError as e:
        print(e)
    except Exception as e:
        print('hhm', e)


def paragraph2():
    print('no')


def paragraph3():
    print('all types')


def paragraph4():
    print('it\'s not recommended, too general the full answer is here '
          'https://medium.com/the-conscious-way/5-powerful-self-reflection-questions-to-get-to-know-yourself-better-69a9c9006008')


def paragraph5():
    print('the question is also the answer, no?')


def paragraph6():
    file = None
    try:
        file = open('words.txt', 'a')
        if file is not None:
            file.write('Ilia')
        else:
            print('failed to open file')
    except Exception as e:
        print(e)
    finally:
        file.close()


def print_file_content(file: TextIO) -> List[AnyStr]:
    print(type(file))
    try:
        lines = file.readlines()
        for line in lines:
            print(line)
        return lines
    except Exception as e:
        print(e)


def paragraph7():
    file = None
    try:
        file = open('words.txt', 'r')
        print_file_content(file)
    except Exception as e:
        print(e)
    finally:
        file.close()


def paragraph8():
    file = None
    try:
        file = open('hebrew_words.txt', 'a')
        if file is not None:
            file.write(u'\u202B''איליה'u'\u202c')
        else:
            print('failed to open file')
    except Exception as e:
        print(e)
    finally:
        file.close()

    file = None
    try:
        file = open('hebrew_words.txt', 'r')
        print_file_content(file)
    except Exception as e:
        print(e)
    finally:
        file.close()


app = Flask(__name__)


@app.route('/content')
def get_content():
    file = open('words.txt', 'r')
    return file.readlines()


@app.route('/register/<name>', methods=['PUT'])
def register(name):
    file = None
    try:
        file = open('words.txt', 'a')
        if file is not None:
            file.write(escape(name))
            return 'success', 201
        else:
            print('failed to open file')
    except Exception as e:
        print(e)
    finally:
        file.close()


def paragraph9():
    app.run(host='127.0.0.1', port=4000)


def paragraph10():
    img = Image.new('RGB', (100, 30), color=(73, 109, 137))

    d = ImageDraw.Draw(img)
    for line in print_file_content(open('words.txt', 'r')):
        d.text((10, 10), line, fill=(255, 255, 0))
    img.save('my_image.png')


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
    paragraph10()
