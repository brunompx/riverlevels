from django.shortcuts import render
#from levels.models import Level


def levelchart_index(request):
    #levels = Level.objects.all()

    return render(request, 'levelchart.html')

