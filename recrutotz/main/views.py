from django.shortcuts import render
from django.http import HttpResponse


def main(requests):
    name = requests.GET.get("name")
    message = requests.GET.get("message")
    if name == None or message == None:
        name = 'Recruto'
        message = 'Давай дружить'
    return HttpResponse(f'<h1>Hello {name}! </h1><br> <h1>{message}<h1>')
