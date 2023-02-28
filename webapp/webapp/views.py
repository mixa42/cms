from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {'form': 1, 'EmailVer': 1, 'agr_list': 1, 'tel': 1})