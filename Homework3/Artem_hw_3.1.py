#Вывести предложение стостящие их двх строк. Поменять местами слова, добавить восклицательный знак в начало и конец
#слова разделить 3 символами (пробел, восклицательный знак и ещё пробел)
#Задание нужно выполнить 3-мя разными способами форматирования.

def foo(s):
    a, b = s.split(" ", maxsplit=2)
    return b + " ! " + a
if True:
    s = input()
    print('!' + foo(s) + "!")

# _____________________________________________________________________
# word = input()
# letter = "!"

# if not word.isdigit():
#    word = word.replace(" ", ' ! ')
#    word = word.split(' ')[::-1]
#    print('{}'.format(letter),word, '{}'.format(letter))
# else:
#    print("no")
# _____________________________________________________________________
# words = " ! ".join(input().split(' ')[::-1])
# print(f'!{words}!')