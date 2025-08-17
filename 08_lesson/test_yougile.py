import requests


token = "MDgHPcNyvXiAtZVtY54eAcATpzspc+p7C7HynxLEMp4eyVm00zXVzrOjrY76z2Ri"
base_url = "https://ru.yougile.com/api-v2"
key = "Bearer " + token
headers = {
"Authorization": key,
"Content-Type": "application/json"
}
# Проверяем успешное создание проекта
def test_create_project_positive():
    body = {
        "title": "test"
    }
    response = requests.post(base_url + "/projects",
                             json=body, headers=headers)
    assert response.status_code == 201

# Проверяем изменение проекта
def test_change_project():
    body = {
        "title": "test"
    }
    response = requests.post(base_url + "/projects", json=body,
                             headers=headers)
    id_project = response.json()["id"]
    response = requests.put(base_url + "/projects/" + id_project,
                            json={"title": "updated_title"}, headers=headers)
    assert response.status_code == 200
    response = requests.get(base_url + "/projects/" + id_project,
                            headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "updated_title"

# Проверяем получение проекта
def test_get_project():
    body = {
        "title": "test"
    }
    response = requests.post(base_url + "/projects", json=body,
                             headers=headers)
    id_project = response.json()["id"]
    response = requests.get(base_url + "/projects/" + id_project,
                            headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == id_project

# Проверяем неудачную попытку создания проекта:
# Пытается создать проект с пустым названием
# Проверяем, что сервер вернул ошибку 400
def test_create_project_negative():
    body = {
        "title": ""
    }
    response = requests.post(base_url + "/projects",
                             json=body, headers=headers)
    assert response.status_code == 400

# Проверяем ошибку при изменении проекта:
# Создаём проект
# Успешно изменяем его название (проверяем статус 200)
# Пытаемся получить проект по некорректному URL (без "/projects/")
# Проверяем, что получаем 404
def test_change_project_negative():
    body = {
      "title": "test"
    }
    response = requests.post(base_url + "/projects", json=body,
                             headers=headers)
    id_project = response.json()["id"]
    response = requests.put(base_url + "/projects/" + id_project,
                            json={"title": "updated_title"},
                            headers=headers)
    assert response.status_code == 200
    response = requests.get(base_url + id_project, headers=headers)
    assert response.status_code == 404

# Проверяем ошибку авторизации:
# Делаем GET-запрос без авторизационных заголовков
# Проверяем, что получаем статус 401
def test_get_project_negative():
    response = requests.get(base_url + "/projects/")
    assert response.status_code == 401
