from django.shortcuts import render


def index(request):
    return render(request, 'survey/index.html', {'notification': 1})


def count_notification(request, current: int = 0):
    return render(request,
                  'survey/fragments/current_notification.html',
                  {'notification': current + 1})
