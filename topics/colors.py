from termcolor import colored, cprint
print(colored('Привет мир!', "blue", attrs=['underline']))
print('Привет, я люблю тебя!')
cprint('Вывод с помощью cprint', 'red', 'on_blue')
