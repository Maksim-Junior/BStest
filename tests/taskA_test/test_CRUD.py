import random
import requests
from datetime import datetime


# CRUD operation tests for testing endpoint - user. Pet swagger: https://petstore.swagger.io/ (task 3(a)).
# PUT method doesn't work.The information is not updated. The response status is always 200...

def test_get_login():
    response = requests.get('https://petstore.swagger.io/v2/user/login?username=some_name&password=some_password')
    message = response.json()['message']
    assert response.status_code == 200
    assert message.startswith('logged in user session:')


def test_get_logout():
    response = requests.get('https://petstore.swagger.io/v2/user/logout')
    message = response.json()['message']
    assert response.status_code == 200
    assert message == 'ok'


def test_get_user_not_found():
    response = requests.get('https://petstore.swagger.io/v2/user/some_name')
    assert response.status_code == 404
    assert response.json()['message'] == 'User not found'


def test_delete_user_not_found():
    response = requests.get(f'https://petstore.swagger.io/v2/user/some_name{datetime.now()}')
    assert response.status_code == 404


def test_post_createWithList():
    time = datetime.now()
    status = random.randint(1, 10000)
    body = [
        {
            "username": f"python{time}",
            "firstName": "Ivan",
            "lastName": "Ivanov",
            "email": "ivan.ivanov@gmail.com",
            "password": "top_secret",
            "phone": "+375440001122",
            "userStatus": status
        }
    ]
    response = requests.post('https://petstore.swagger.io/v2/user/createWithList', json=body)
    assert response.status_code == 200
    assert response.json()['message'] == 'ok'

    response2 = requests.get(f'https://petstore.swagger.io/v2/user/python{time}')
    user_id = response2.json()['id']
    assert type(user_id) == int
    assert response2.json()['username'] == body[0]['username']
    assert response2.json()['firstName'] == body[0]['firstName']
    assert response2.json()['lastName'] == body[0]['lastName']
    assert response2.json()['email'] == body[0]['email']
    assert response2.json()['password'] == body[0]['password']
    assert response2.json()['phone'] == body[0]['phone']
    assert response2.json()['userStatus'] == body[0]['userStatus']


def test_post_createWithArray():
    time = datetime.now()
    status = random.randint(1, 10000)
    body = [
        {
            "username": f"user{time}",
            "firstName": "Vladimir",
            "lastName": "Wrutin",
            "email": "fair.vova@gmail.com",
            "password": "1111",
            "phone": "+375296660033",
            "userStatus": status
        }
    ]
    response = requests.post('https://petstore.swagger.io/v2/user/createWithArray', json=body)
    assert response.status_code == 200
    assert response.json()['message'] == 'ok'

    response2 = requests.get(f'https://petstore.swagger.io/v2/user/user{time}')
    user_id = response2.json()['id']
    assert type(user_id) == int
    assert response2.json()['username'] == body[0]['username']
    assert response2.json()['firstName'] == body[0]['firstName']
    assert response2.json()['lastName'] == body[0]['lastName']
    assert response2.json()['email'] == body[0]['email']
    assert response2.json()['password'] == body[0]['password']
    assert response2.json()['phone'] == body[0]['phone']
    assert response2.json()['userStatus'] == body[0]['userStatus']


def test_create_delete_user():
    time = datetime.now()
    status = random.randint(1, 10000)
    body = {
        "username": f"new{time}",
        "firstName": "Alex",
        "lastName": "Martin",
        "email": "alex.alex@gmail.com",
        "password": "30541alex",
        "phone": "+375334567890",
        "userStatus": status
    }

    response = requests.post('https://petstore.swagger.io/v2/user', json=body)
    message = response.json()['message']
    assert response.status_code == 200
    assert type(message) == str

    response2 = requests.get(f'https://petstore.swagger.io/v2/user/new{time}')
    assert response2.json()['id'] == int(message)
    assert response2.json()['username'] == body['username']
    assert response2.json()['firstName'] == body['firstName']
    assert response2.json()['lastName'] == body['lastName']
    assert response2.json()['email'] == body['email']
    assert response2.json()['password'] == body['password']
    assert response2.json()['phone'] == body['phone']
    assert response2.json()['userStatus'] == body['userStatus']

    response3 = requests.delete(f'https://petstore.swagger.io/v2/user/new{time}')
    assert response3.status_code == 200
    assert response3.json()['message'] == body['username']

    response4 = requests.get(f'https://petstore.swagger.io/v2/user/new{time}')
    assert response4.status_code == 404
    assert response4.json()['message'] == 'User not found'
