# Django + DRF


Steps to run: 

1) Set up a virtual environment for Python 3 and enable it
2) Run command `pip install -r requirements.txt` to install the dependencies
3) POST the request in the url http://127.0.0.1:8000/api/restaurants/ for create restaurant

```json
{
    "username": "admin",
    "name": "Name-restaurent",
    "street": "street",
    "number_house": 432,
    "password": "password"
}
```

4) POST the request in the url http://127.0.0.1:8000/api/pizzas/ for create pizza, having previously received the token in the url http://127.0.0.1:8000/api/auth/token/login

```json
{
    "name": "Маргарита",
    "pastry": "тонкое",
    "ingredients": [
        "Кетчуп",
        "Помидоры",
        "Сыр"
    ],
    "secret_ingredient": "клюква"
}
```

5) POST the request in the url http://127.0.0.1:8000/api/people/ for create people

```json
{
    "iin": "YYMMDDy00000"
}
```