from ast import Sub
import re
from django.shortcuts import render, redirect
from .models import Branch, Note, Tutorial, SubName
# from .models import PreviousYearQuestionPaper, Tutorial, Note


def home(request):
    print("heollo")
    branchs = Branch.objects.all()
    print(request.GET)
    context = {
        'branchs':branchs,
    }
    return render(request, 'src/home.html', context)

def filter_values(request):
    print(request.GET)
    d = dict(request.GET)
    # notes = Note.objects.filter(subname__branch=d['branch'][0], subname__sem=d['sem'][0])
    # print(notes)
    # question_paper = PreviousYearQuestionPaper.objects.filter(branch=d['branch'][0], sem=d['sem'][0])
    # tutorial = Tutorial.objects.filter(branch=d['branch'][0], sem=d['sem'][0])
    # print(notes)
    
    context = {
        'sem' : d['sem'][0],
        'branch': d['branch'][0],
    }
    return render(request, 'src/filtered_page.html', context)

def specific_page(request, sem, branch, type):
    print(request.GET)
    print(sem, branch, type)
    subjects = SubName.objects.filter(sem=sem, branch=branch)
    if type == 'note':
        notes = Note.objects.filter(subname__sem=sem, subname__branch=branch)
        context = {
            'type': 'NOTES',
            'items':notes,
            'subjects':subjects,
            'sem':sem,
            'branch':branch,

        }
    elif type == 'tutorial':
        try:
            tutorials = Tutorial.objects.filter(subname__sem=sem, subname__branch=branch)
            context = {
                'type':'TUTORIALS',
                'items':tutorials,
                'subjects':subjects,
                'sem':sem,
                'branch':branch,
            }
        except:
            context = {}

    return render(request, 'src/specific_page.html', context)