# i have created this file -m jatin
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
def analyze(request):
    #getting text
    djtext = request.GET.get('text','default')
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps','off')
    newlineremover = request.GET.get('newlineremover','off')


    #check if removepunc is on or not
    if removepunc == "on":
        analyzed = " "
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuation', 'analyzed_text': analyzed}
        return render(request,'analyze.html',params)
    #checking if fullcaps in on or not
    elif(fullcaps == "on"):
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse('Error')
     #   return HttpResponse('removepunc')




#used before for checking the code whether its working or not
#def capfirst(request):
 #   return HttpResponse('capfirst')
#def spaceremover(request):
 #   return HttpResponse('spacefirst <a href="index"> Back </a>')
#def newlineremover(request):
 #   return HttpResponse('newlineremover')
##   return HttpResponse('charcount')