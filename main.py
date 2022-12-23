import requests

token = 'e5ea37ef-112c-4055-82ac-ab6fa4affecb'
url_first_round = 'https://datsanta.dats.team/api/round'
headers = {"X-API-KEY": token, "Content-type": r"application/json"}


santa_speed = 70  # Метры в секунду скорость
santa_max_volume = 200  # киллограммы максимум которые влезут в сани
santa_max_weight = 100  # объект в дм3 которые влезут в сани


def sort_stack_id(stack):
    stack_id = sorted(list(map(lambda x: lst_children[x], stack)), key=lambda x: x['x'] + x['y'])
    print(stack_id)
    print(list(map(lambda x: x['y'] + x['x'], stack_id)))
    return stack_id


current_weight = 0  # текущий вес
current_volume = 0  # текущий вес

good = []  # список где будут храниться успешно пройденные дома

dt = requests.get('https://datsanta.dats.team/json/map/faf7ef78-41b3-4a36-8423-688a61929c08.json')  # запрос получаю АПИ
lst_gifts = dt.json()['gifts']  # получаю объект гифтс (id, вес, объем)
lst_children = dt.json()['children']  # получая объект состоящий из координатов домов детей
stack_id = []
for row in range(len(lst_children)):
    print(lst_gifts[row], lst_children[row], f"my stats: volume: {current_volume}, weight: {current_weight}")
    if (int(lst_gifts[row]['volume']) + current_volume > 100) \
            or \
            (int(lst_gifts[row][
                     'weight']) + current_weight > 200):  # если вес или объем будет превышен мы отправляем санту раздаваит подарки
        santa_coords_x, santa_coords_y = (0, 0)  # начинаем с нулевых координат
        for res in sort_stack_id(stack_id):
            pass

        print('STOP', current_volume, current_weight, stack_id)
        current_weight = 0  # сбрасываем значения
        current_volume = 0  # сбросываем значения
        stack_id.clear()
    else:
        current_weight = current_weight + int(lst_gifts[row]['weight'])
        current_volume = current_volume + int(lst_gifts[row]['volume'])
        stack_id.append(lst_gifts[row]['id'])


MAP_ID = 'faf7ef78-41b3-4a36-8423-688a61929c08.json'
moves = []
stackOfBags = []
dt = requests.post(url_first_round, headers=headers)
print(dt.json())