import requests

def get_categories():
    r = requests.get("https://api.escuelajs.co/api/v1/categories")
    print(r.status_code)
    print()
    print(r.text)
    print()
    print(type(r.text))
    print()
    categories = r.json()
    for category in categories:
        print(category["name"])
