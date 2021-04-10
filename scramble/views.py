from django.shortcuts import render,redirect
from django.http import HttpResponse
import random

# Create your views here.
words = [
	"covid",
	"corona",
	"lockdown",
	"pandemic",
	"epidemic",
	"hospital",
	"doctor",
	"fever",
	"cough",
	"sanitation",
	"distancing",
	"ambulance",
	"bats",
	"china",
	"virus",
	"mask",
	"sanitizer",
	"isolation",
	"quarantine",
	"vaccine",
]

msg = ""

def rword():
	global jword,word,score,total
	word = random.choice(words)
	jum = random.sample(word, len(word))
	jword="".join(jum)

def game(request):
	global score,total
	score=0
	total=0
	rword()
	global jword,msg
	return render(request, 'scramble.html', {'jum_word':jword, 'msg':msg, 'score':score, 'total':total})


def checkans(request):
	global word,msg,jword,score,total
	user_ans = request.POST.get('answer')
	if user_ans == word:
		msg = "Correct answer"
		score=score+1
		return redirect('/scramble/games')
	else:
		msg = "Try again"
	return render(request, 'scramble.html', {'jum_word':jword, 'msg':msg, 'score':score, 'total':total})

def next(request):
	global score,total,jword,msg
	total=total+1
	msg=""
	rword()
	return render(request, 'scramble.html', {'jum_word':jword, 'msg':msg, 'score':score, 'total':total})
