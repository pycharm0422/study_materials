from ast import Sub
from operator import mod
from pyexpat import model
from statistics import mode
from unittest.util import _MAX_LENGTH
from django.db import models


sem = (
        (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8),
    )

# class Basic(models.Model):
    
#     branch = models.CharField(max_length=200, choices=branch, null=True)
#     sem = models.IntegerField(choices=sem, null=True)
#     sec = models.CharField(max_length=200, choices=section, null=True)

#     def __str__(self):
#         return (str(self.sem))

class Branch(models.Model):
    bname = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.bname

class SubName(models.Model):
    sname = models.CharField(max_length=200, blank=True, null=True, unique=True)
    branch = models.ForeignKey(Branch, null=True, blank=True, on_delete=models.CASCADE)
    sem = models.IntegerField(choices=sem, null=True)

    def __str__(self):
        return self.sname + "  " + str(self.branch) + "  " + str(self.sem)

class Note(models.Model):
    subname = models.ForeignKey(SubName, on_delete=models.SET_NULL, null=True)
    nname = models.CharField(max_length=200, null=True, blank=True, default="notes")
    note_file = models.FileField(upload_to='notes_file/', null=True, blank=True)

    def __str__(self):
        return str(self.subname) + "  " + self.nname

class Tutorial(models.Model):
    subname = models.ForeignKey(SubName, on_delete=models.CASCADE)
    name_tut_ques = models.CharField(max_length=200, null=True, blank=True, default="tut")
    tut_ques = models.FileField(upload_to='tutorials/', null=True, blank=True)
    name_tut_ans = models.CharField(max_length=200, null=True, blank=True, default="tut_ans")
    tut_ans = models.FileField(upload_to='tutorials/', null=True, blank=True)

    def __str__(self):
        return str(self.subname)



# class PreviousYearQuestionPaper(models.Model):
#     branch = models.CharField(max_length=200, choices=branch, null=True)
#     sem = models.IntegerField(choices=sem, null=True)
#     sec = models.CharField(max_length=200, choices=section, null=True)
#     paper = models.FileField(upload_to='prev_ques/', null=True, blank=True)
#     ans = models.FileField(upload_to='prev_ques/', null=True, blank=True)
    
#     def __str__(self):
#         return (str(self.branch) + str(self.sem) + str(self.sec))