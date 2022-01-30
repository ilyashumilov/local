from django.shortcuts import redirect

def restriction(view):
    def wrapper(request, *args, **kwargs):
        if request.user.is_anonymous == True:
            return redirect('LoginView')
        else:
            return view(request, *args, **kwargs)
    return wrapper
