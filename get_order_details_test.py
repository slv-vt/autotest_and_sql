# Вячеслав Войтенко, когорта 8-а — Финальный проект. Инженер по тестированию плюс

import sender_stand_request
import data

# Тест, проверяющий корректность запроса на получение данных о заказе при передаче трекингового номера.
def test_correct_orders_info_response():
    resp_create_order = sender_stand_request.post_new_order(data.order_body)    # Создание переменной, вызывающей функцию создания нового заказа
    track = {"t": resp_create_order.json()["track"]}    # Создание переменной, содержащей словарь, в которой ключ = t, а значение = полученному трекинговому номеру заказа из предыдущего шага
    resp_order_info = sender_stand_request.get_order_info(track)    # Создание переменной, вызывающей функцию получения информации о заказе и передающей переменную с трекингововым номером
    assert resp_order_info.status_code == 200   # Проверка, что код ответа равен 200
