# -*- coding: utf-8 -*-

import simple_draw as sd

from python_snippets.snowfall import check_colour, create_snow, all_random_values, next_step, remove_or_create

sd.resolution = (1800, 600)

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

# создать_снежинки(N)
sd.start_drawing()

while True:
    create_snow()
    colour = check_colour()
    while True:

        for i in all_random_values:

            for _ in range(next_step()):

                # sd.clear_screen()

                point_starter = sd.get_point(i['start_x'], i['start_y'])
                sd.snowflake(point_starter, i['length_list'], sd.background_color, i['a_list'], i['b_list'],
                             i['c_list'])
                if i['start_y'] < 1:
                    continue
                else:
                    i['start_y'] -= 50

                i['start_x'] -= sd.randint(-10, 10)

                point_starter = sd.get_point(i['start_x'], i['start_y'])
                sd.snowflake(point_starter, i['length_list'], colour, i['a_list'], i['b_list'], i['c_list'])
                if i['start_y'] < 1:
                    remove_or_create(i)
                    all_random_values.pop(int(len(all_random_values) - 1))
                sd.finish_drawing()


        #  нарисовать_снежинки_цветом(color=sd.background_color)
        #  сдвинуть_снежинки()
        #  нарисовать_снежинки_цветом(color)
        #  если есть номера_достигших_низа_экрана() то
        #       удалить_снежинки(номера)
        #       создать_снежинки(count)

        sd.sleep(0.1)

        if sd.user_want_exit():
            break

sd.pause()
