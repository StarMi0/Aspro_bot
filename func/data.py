from .functions import key_dict
import requests
import json

company = key_dict["Company_name"]
aspro_token = key_dict["Company_key"]


def url_parser(company_name: str,
               company_key: str,
               module_name: str,
               entity_name: str,
               method: str
               ) -> str:
    """
    Функция формирования URL адреса по заданным параметрам.
    :param company_name: код аккаунта
    :param company_key: персональный ключ доступа к апи
    :param module_name: указывает на модуль
    :param entity_name: указывает на сущность
    :param method: указывает на метод
    :return: URL для запроса. Ответ на запрос будет возвращен в формате JSON
    с HTTP-кодом 200, успешно выполненный запрос содержит объект response.
    """
    url = f"https://{company_name}.aspro.cloud/api/v1/module/{module_name}/{entity_name}/{method}?api_key={company_key}"
    return url


def get_json_response(url: str) -> json:
    """

    :param url:
    :return:
    """
    response = requests.get(url)
    json_data = response.json()
    return json_data


def print_json_response(json_data: json):
    """

    :param json_data:
    :return:
    """
    print(json.dumps(json_data, indent=4, sort_keys=True))


if __name__ == "__main__":
    pass
