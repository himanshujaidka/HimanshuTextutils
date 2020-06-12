#I have created a file-Himanshu
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps=request.POST.get('fullcaps','off')
    no_space=request.POST.get('no_space','off')
    line_remover=request.POST.get('line_remover','off')
    char_count=request.POST.get('char_count','off')



    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for item in djtext:
            if item not in punctuations:
                analyzed = analyzed + item
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed


    if (fullcaps == 'on'):
        analyzed=""
        for item in djtext:
            analyzed= analyzed + item.upper()
        params={'purpose':'Capitalize Text','analyzed_text':analyzed}
        djtext=analyzed


    if(no_space == 'on'):
        analyzed=""
        for index,char in enumerate(djtext):
            if djtext[index]==" " and djtext[index+1]==" ":
                pass
            else:
                analyzed=analyzed+char
        params={'purpose':'Removed Space','analyzed_text':analyzed}
        djtext=analyzed


    if (line_remover == 'on'):
        analyzed=""
        for item in djtext:
            if item!='\n' and item!='\r':
                analyzed=analyzed+item
        params={'purpose':'Line Removed','analyzed_text':analyzed}
        djtext=analyzed

    if (char_count == 'on'):
        char=0
        analyzed=""
        for item in range(len(djtext)):
            char+=1
        params={'purpose':'Character Count','analyzed_text':char}
        djtext=analyzed
    if ((removepunc !='on')and (fullcaps!='on') and (no_space!='on') and (line_remover!='on') and (char_count!=0)):
        return HttpResponse("ERROR! Please Select any operation")

    return render(request,'analyze.html',params)