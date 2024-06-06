from django.shortcuts import redirect

def login_requerido(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('index')  # Nome da URL para a página 'index'
        return view_func(request, *args, **kwargs)
    return wrapper
