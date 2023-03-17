import pickle
import numpy as np
from django.shortcuts import render
from .forms import CommentForm

def get_score_pred(y_pred):
    y_pred = y_pred.round().astype('int')
    y_pred = np.where(y_pred < 1, 1, y_pred)
    y_pred = np.where(y_pred > 10, 10, y_pred)
    return y_pred

def get_status(y):
    return y > 5.5

def index(request):
	submitbutton = request.POST.get("submit")

	comment = "Good movie, like, love, syper, puper!!!!"
	form = CommentForm(request.POST or None)
	if form.is_valid():
		comment = form.cleaned_data.get("comment")

	with open('best_model.pkl', 'rb') as f:
		model = pickle.load(f)
	
	y_pred = model.predict([comment])
	comment_info = {
	'name': comment[:20] + '...',
	'rating': get_score_pred(y_pred)[0], 
	'status': 'Позитивный' if get_status(y_pred) else 'Негативный'
	}
	context = {'info': comment_info}
	return render(request, 'analyzer/index.html', context)
