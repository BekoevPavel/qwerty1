from django.shortcuts import render


def landing(request):
    return render(request, 'landing/landing.html', locals())


def ff(request):
    return render(request, 'landing/ff.html', locals())
