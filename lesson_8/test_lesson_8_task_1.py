import requests

base_url = "https://x-clients-be.onrender.com"


def get_company_list(params_to_add=None):
    resp = requests.get(f"{base_url}/company", params=params_to_add)
    return resp.json()


def get_token(user='bloom', password='fire-fairy'):
    creds = {
        'username': user,
        'password': password
    }
    resp = requests.post(f"{base_url}/auth/login", json=creds)
    return resp.json()["userToken"]


def add_new_employee(company_id):
    new_employee = {
        "id": 0,
        "firstName": "Федор",
        "lastName": "Федоров",
        "middleName": "Федорович",
        "companyId": company_id,
        "email": "fedor@mail.ru",
        "url": "string",
        "phone": "string",
        "birthdate": "2024-01-31T05:47:53.986Z",
        "isActive": True
    }

    headers = {"x-client-token": get_token()}
    resp = requests.post(f"{base_url}/employee", json=new_employee, headers=headers)
    resp.raise_for_status()

    new_employee_id = resp.json()["id"]
    return new_employee_id


def get_employee_by_id(employee_id):
    resp = requests.get(f"{base_url}/employee/{employee_id}")
    resp.raise_for_status()
    return resp.json()


def change_employee(employee_id):
    new_data = {
        "lastName": "Пупкин",
        "email": "pup@mail.ru",
        "url": "string",
        "phone": "string",
        "isActive": False
    }

    headers = {"x-client-token": get_token()}
    resp = requests.patch(f"{base_url}/employee/{employee_id}", json=new_data, headers=headers)
    resp.raise_for_status()

    return resp.json()


def test_get_list_employees():
    # Получение списка всех компаний
    list_companies = get_company_list()

    # Проверка, что список компаний не пустой
    assert len(list_companies) > 0

    # Получение id последней компании в списке
    company_id = list_companies[-1]['id']

    # Получение списка сотрудников по id компании
    list_employees = get_company_list(params_to_add={'company': company_id})

    # Проверка, что список сотрудников не пустой
    assert len(list_employees) > 0


def test_add_new_employee():
    # Получение списка всех компаний
    list_companies = get_company_list()

    # Проверка, что список компаний не пустой
    assert len(list_companies) > 0

    # Получение id последней компании в списке
    company_id = list_companies[-1]['id']

    # Получение списка сотрудников по id компании и их количества
    resp = requests.get(f"{base_url}/employee", params={"company": company_id})
    list_employees = resp.json()

    len_before = len(list_employees)

    # Добавление нового сотрудника в компанию
    new_employee_id = add_new_employee(company_id)

    # Получение количества сотрудников компании после добавления сотрудника
    resp = requests.get(f"{base_url}/employee", params={"company": company_id})
    list_employees = resp.json()
    len_after = len(list_employees)

    # Проверка, что количество сотрудников увеличилось на одного
    assert len_after - len_before == 1

    # Получение данных добавленного сотрудника по его id
    employee_data = get_employee_by_id(new_employee_id)

    # Проверка, что данные сотрудника совпадают с добавленными данными
    assert employee_data["id"] == new_employee_id
    assert employee_data["firstName"] == "Федор"
    assert employee_data["lastName"] == "Федоров"
    assert employee_data["middleName"] == "Федорович"
    assert employee_data["companyId"] == company_id


def test_get_employee_by_id():
    # Получение списка всех компаний
    list_companies = get_company_list()

    # Проверка, что список компаний не пустой
    assert len(list_companies) > 0

    # Получение id последней компании в списке
    company_id = list_companies[-1]['id']

    # Добавление нового сотрудника в компанию
    new_employee_id = add_new_employee(company_id)

    # Получение данных добавленного сотрудника по его id
    employee_data = get_employee_by_id(new_employee_id)

    # Проверка, что данные сотрудника совпадают с ожидаемыми
    assert employee_data["id"] == new_employee_id
    assert employee_data["firstName"] == "Федор"
    assert employee_data["lastName"] == "Федоров"
    assert employee_data["middleName"] == "Федорович"
    assert employee_data["companyId"] == company_id


def test_change_employee():
    # Получение списка всех компаний
    list_companies = get_company_list()

    # Проверка, что список компаний не пустой
    assert len(list_companies) > 0

    # Получение id последней компании в списке
    company_id = list_companies[-1]['id']

    # Получение списка сотрудников по id компании и их количества
    resp = requests.get(f"{base_url}/employee", params={"company": company_id})
    list_employees = resp.json()

    len_before = len(list_employees)

    # Добавление нового сотрудника в компанию
    new_employee_id = add_new_employee(company_id)

    # Получение данных сотрудника до изменений
    employee_data_before = get_employee_by_id(new_employee_id)

    # Изменение данных сотрудника
    change_employee(new_employee_id)

    # Повторное получение данных сотрудника после изменений
    employee_data_after = get_employee_by_id(new_employee_id)

    # Проверка, что данные до и после изменений не совпадают
    assert employee_data_before != employee_data_after

    # Проверка, что измененные данные сотрудника совпадают с ожидаемыми
    assert employee_data_after["id"] == new_employee_id
    assert employee_data_after["lastName"] == "Пупкин"
    assert employee_data_after["email"] == "pup@mail.ru"
    assert employee_data_after["isActive"] is False