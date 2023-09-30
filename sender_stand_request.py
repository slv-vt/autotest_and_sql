import configuration
import data
import requests


# Функция, отправляющая запрос на создание нового заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH, json=body,
                                                                                     headers=data.headers)


# Функция, отправляющая запрос на получение информации о заказе по его трекинговому номеру
def get_order_info(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_DETAILS_PATH, params=track)
