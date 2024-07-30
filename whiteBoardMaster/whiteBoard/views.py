
from django.shortcuts import render

def whiteboard(request):
    return render(request, 'whiteBoard/whiteboard.html')
