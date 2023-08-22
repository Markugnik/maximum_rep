word = input('введите слово:  ')
def palindrome_check(str):
    inverted_str = str[::-1]
    if str == inverted_str:
        print('True')
    else:
        print('False')
palindrome_check(word)
