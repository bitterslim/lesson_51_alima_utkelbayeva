from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect
from webapp.cat import Cat


def cat_view(request: WSGIRequest):
    action = request.POST.get('action')
    name = request.POST.get('name')
    message = Cat.get_action(action)
    cat_status = Cat.get_status()
    if cat_status:
        context = {
            'name': name,
            'image': Cat.image,
            'age': Cat.age,
            'happiness': Cat.happiness,
            'hunger': Cat.hunger,
            'message': message
        }
        return render(request, 'cat.html', context=context)
    else:
        response = redirect('/')
        return response