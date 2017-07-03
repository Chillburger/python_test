import sys

def repeat(s, exclaim):

    result = s + s + s + s
    if exclaim:
        result = result + '!!!'
    return result

def absolute(num):
    try:
        return abs(int(num))
    except ValueError:
        return "the input: " + num + " is not an integer"

def isString(input):
    callable(test)
    try:
        callable(test)
        return True
    except StringException:
        return False

class Foo:
    def __call__(self):
        print 'called'


def main():
    foo_instance =  Foo()
    foo_instance()

if __name__ == '__main__':
    main()
