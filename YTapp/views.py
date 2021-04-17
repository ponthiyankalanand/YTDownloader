from django.shortcuts import render, redirect
from django.http import HttpResponse
from pytube import YouTube

# Create your views here.

def home(request):
	#return render(request, 'index.html')
	yt = ""
	return render(request,"index.html",{'yt' : yt})

def download(request):
	#return render(request, 'index.html')
	save_path="media/"

	try:
		url= request.POST['url']
		radio=request.POST['format']
		yt = YouTube(url)
		print(radio)
		save_name=yt.title
		if radio == 'video':
			print('inside video block')
			
			yt.streams.filter(type = 'video').first().download(output_path = save_path, filename = save_name)
			save_name=save_name+'.mp4'
			return render(request, "index.html",{'yt' : yt,'save_name' : save_name,'save_path' : save_path})
		elif radio == 'audio':
			print('inside audio block')
			save_name=save_name+'.webm'
			yt.streams.filter(mime_type= 'audio/webm').first().download(output_path = save_path, filename = save_name)
			return render(request, "index.html",{'yt' : yt,'save_name' : save_name,'save_path' : save_path})
			print('done')
		else:
			yt='Not valid format'
			return render(request, "index.html",{'yt' : yt})
	except:
		yt="ERROR"
		return render(request, "index.html",{'yt' : yt})
def media(request):
	url= request.POST['name']
	filepath=os.save_path 