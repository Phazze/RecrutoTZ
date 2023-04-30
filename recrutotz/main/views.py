from django.shortcuts import render
from django.http import HttpResponse


def main(requests):
    name = requests.GET.get("name")
    message = requests.GET.get("message")
    contex = {
        "name": name,
        "message": message
    }
    if name == None or message == None:
        contex = {
            "name": 'Recruto',
            "message": "Давай дружить"
        }
    return render(requests, 'main/main.html', contex)
