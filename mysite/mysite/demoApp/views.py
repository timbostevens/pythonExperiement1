from django.shortcuts import render
from django.http.response import HttpResponse
from demoApp.models import SnesGame


def index(request):
    return render(request, 'demoApp/index.html')

def dataEntry(request):
    return render(request,'demoApp/dataEntry.html')

def dataDisplay(request):
    
    
    
    # get data from database
    data = SnesGame.objects.all()
    
    # what is the format of the third arument here?
    return render(request, 'demoApp/dataDisplay.html', {"data":data})


def inputView(request):
    
    
    if request.method == 'POST':
        
        
        # get will return None if nothing is found with that title
        # the second argument is the default value if the first arg is not found
        gameTitle = request.POST.get('gameTitle', 'Alert! Alert!')
        # this is currently text I think
        releaseDate = request.POST.get('releaseDate')
        description = request.POST.get('description', 'Alert! Alert!')
        rating = request.POST.get('rating')
        
        
        # bodge to get a date
        year = releaseDate[-4:]
        month = releaseDate[3:5]
        day = releaseDate[:2]
        
        # print(year + "/" + month + "/" + day)
        
        
        
        # when you do this it seems that the arguments aren't type-checked
        game = SnesGame(gameTitle, year + "-" + month + "-" + day, rating, description)

        game.save()
        
        outputString = game.__str__()
        
        return HttpResponse(outputString)
    else:
        return HttpResponse("Something has gone wrong")
    
    