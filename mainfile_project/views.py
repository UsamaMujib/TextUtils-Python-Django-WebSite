# This file is created by me
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #dicin = {'sec':'Website', 'fir':'Working'}
    return render(request, 'index.html')

def removepunc(request):
    form_value = request.POST.get("text", "default")
    remove_punc = request.POST.get("re_punc", "off")
    allcap = request.POST.get("all_cap", "off")
    nlremv = request.POST.get("nl_remv", "off")
    spremv = request.POST.get("sp_remv", "off")
    charcount = request.POST.get("char_count", "off")
    var_purpose = ""
    dic_para = {}
    #analyzed = ""

    if remove_punc == "on":
        #print(form_value)
        analyzed = "" 
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for i in form_value:
            if i not in punctuations:
                analyzed += i

        a = "Punctuation Removed,"
        var_purpose += a
        dic_para = {"purpose":var_purpose, "analyzed_text":analyzed}
        form_value = analyzed
        #return render(request, 'removepunc.html', dic_para)

    if allcap == "on":
        analyzed = form_value.upper()
        a = " Change TO Uppercase,"
        var_purpose += a 
        dic_para = {"purpose":var_purpose, "analyzed_text":analyzed}
        form_value = analyzed
        #return render(request, 'removepunc.html', dic_para)

    if nlremv == "on":
        analyzed = ""
        for i in form_value:
            if i != "\n" and i != "\r":
                analyzed += i
        
        a = " New Line Removed,"
        var_purpose += a
        dic_para = {"purpose":var_purpose, "analyzed_text":analyzed}
        form_value = analyzed
        #return render(request, 'removepunc.html', dic_para)

    if spremv == "on":
        analyzed = ""
        for index, char in enumerate(form_value):
            if not(form_value[index] == " " and form_value[index + 1] == " "):
                analyzed += char
                #pass
            #else:
                #analyzed += char

        a = " Extra Space Removed,"
        var_purpose += a
        dic_para = {"purpose":var_purpose, "analyzed_text":analyzed}
        form_value = analyzed
        #return render(request,'removepunc.html', dic_para)

    if charcount == "on":
        #analyzed = form_value
        l = len(form_value)
        #analyzed += "\n"
        #analyzed += l
        a = " Character Counted"
        var_purpose += a
        dic_para = {"purpose":var_purpose, "analyzed_text":analyzed, "analyzed_count":l}
        #form_value = analyzed
        #return render(request, 'removepunc.html', dic_para)

    if remove_punc != "on" and allcap != "on" and nlremv != "on" and spremv != "on" and charcount != "on":
        var_error = {"valu":"Error, Please Select an Option."}
        #return render(request, 'removepunc.html',var_error)
        return render(request, 'no_option.html', var_error)

    #else:
        #return HttpResponse("Error")

    return render(request, 'removepunc.html', dic_para)