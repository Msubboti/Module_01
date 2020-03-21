def spam(number):
    '''Function should return something like this:
    spam(1);#bulochka
    spam(3);#bulochkabulochkabulochka
    But it is broken. Fix it please!

    Эта функция принимает числовой параметр. Должна вернуть строку, которая
    повторяется столько раз, сколько параметров передано. Она уже написана,
    но не работает. Любым способом заставьте ее работать.
    '''
    x = "bulochka"
    stroka = ''.join(x for i in range(0, number))
    return stroka


def my_sum(list_of_numbers):

    """Function receives a list with integer numbers,
    should return its sum as an integer. Do not use built in summarize functions.
    :param list

    Функция получает на вход массив чисел, должна вернуть сумму этих чисел.
    Не использовать встроенные функции суммирования.
    
    """

    pass
    #  ...wite your code here
    x = 0
    for i in list_of_numbers:
        x += i
    return x



def shortener(string):
    """
    Function receives a long string with many words.
    It should return the same string, but words,
    larger then 6 symbols should be changed, symbols
    after the sixth one should be replaced by symbol *
    :param string
    :returns string

     Функция получает на вход длинную строку с множеством слов.
     Она должна вернуть ту же строку, но в словах, которые длиннее 6 символов,
     функция должна вместо всех символов после шестого поставить одну звездочку.
     Пример: Из слова 'verwijdering' должно получиться 'verwij*'


    """
    pass
    #  ...wite your code here
    temp_string = string.split(' ')
    temp = [id for id, i in enumerate(temp_string) if len(i) > 6]
    for index in temp:
        temp_string[index] = temp_string[index][0:6] + "*"
    answer = " ".join(i for i in temp_string)
    return answer


def compare_ends(words):
    """
    Function receives an array of strings.
    Please return number of strings, which
    length is at least 2 symbols and first character
    is equal to the last character

    Функция получает на вход массив строк. Вернуть надо количество строк,
    которые не короче двух символов и у которых первый и последний
    символ совпадают.

    """
    pass
    #  ...wite your code here

    listing = [i for i in words if len(i) > 1 and i[0] == i[-1]]
    return len(listing)
