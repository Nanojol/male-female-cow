import simple_draw as sd
import random

all_random_values = []


def check_colour():
    colour_list = [
        (1, 'RED'),
        (2, 'ORANGE'),
        (3, 'YELLOW'),
        (4, 'GREEN'),
        (5, 'CYAN'),
        (6, 'BLUE'),
        (7, 'PURPLE')
    ]
    colour_number_dict = {
        '1': (255, 0, 0),
        '2': (255, 127, 0),
        '3': (255, 255, 0),
        '4': (0, 255, 0),
        '5': (0, 255, 255),
        '6': (0, 0, 255),
        '7': (255, 0, 255)
    }

    print('Список доступных цветов', *colour_list)
    user_input_colour = input("Введите, пожалуйста, номер цвета: ")
    number_colour = int(user_input_colour)
    while True:
        if number_colour < 1 or number_colour > 7:
            print('Введите корректное значение от 1 до 7')
            user_input_colour = input("Введите, пожалуйста, номер цвета: ")
            number_colour = int(user_input_colour)

        else:
            return colour_number_dict[str(number_colour)]


def random_values_snow():
    return {
        'start_x': random.randrange(50, 1600),
        'start_y': random.randrange(500, 650, 50),
        'a_list': random.randrange(1, 8) / 10,
        'b_list': random.randrange(1, 8) / 10,
        'c_list': random.randrange(30, 60),
        'length_list': random.randrange(20, 50),
    }


def create_snow():
    user_input_count_snow = input("Введите, пожалуйста, количество снежинок: ")
    for _ in range(int(user_input_count_snow)):
        all_random_values.append(random_values_snow())


def next_step():
    new_game = input('Показать следующий шаг? Введите Да/Нет:')
    if str.upper(new_game) == 'ДА':
        return 10

def remove_or_create(number):
    print(all_random_values.index(number))
    chose = input('Удалить снежинку или добавить? Введите Удалить/Добавить:')
    if str.upper(chose) == 'УДАЛИТЬ':
        all_random_values.remove(number)
    elif str.upper(chose) == 'ДОБАВИТЬ':
        all_random_values.append(create_snow())




# print(next_step())

