from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    DJ = {'name':'djbravo', 'place':'mars'}
    return render(request, 'index.html', DJ)
    # return HttpResponse("hello harry bhai")

def about(request):
    return HttpResponse("about harry bhai")

#Making back button
def GoBackSimon(request):
    return HttpResponse("<a href='/'>Go Back</a>")

def removepunc(request):
    djtext = request.POST.get('text', 'default')
    check  = request.POST.get('check', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charactercounter = request.POST.get('charactercounter', 'off')
    

    # print(djtext)
    # print(check)

    
    if check == "on":
        # analyzed = djtext
        punctuations = '''!()-[]{};:'"/\,<>.?@#$%^&*_~'''

        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char


        params = {'purpose':'Removed Punctuations', 'analyzed_text':analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed  +char.upper()

        params = {'purpose':'Changed to UpperCase', 'analyzed_text':analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed  +char

        params = {'purpose':'Removed New Line', 'analyzed_text':analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    elif(extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not djtext[index] == " " and djtext[index+1] ==" ":
                analyzed = analyzed +char         

        params = {'purpose':'Removed Extra Spaces', 'analyzed_text':analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    elif(charactercounter == "on"):
        analyzed = ""
        count = 0
        for char in djtext:
                # analyzed = analyzed  +char
                count+=1

        params = {'purpose':'Removed New Line', 'analyzed_text':count}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
        
    if(check!='on' and fullcaps!='on' and extraspaceremover!='on' and charactercounter!='on' and newlineremover!='on'):
        return HttpResponse("Nothing Selected - Error")

    return render(request, 'analyze.html', params)