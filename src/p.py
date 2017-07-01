import sys

def repeat(s, exclaim):

    result = s + s + s + s
    if exclaim:
        result = result + '!!!'
    return result

def main():
    name = sys.argv[1]
    if name == 'David':
        print repeat( name, False) + '!!!'
    else:
        print repeat( 'yay', True)

if __name__ == '__main__':
    main()
