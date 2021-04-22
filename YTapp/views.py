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
	save_path="/media/"

	try:
		url= request.POST['urlval']
		radio=request.POST['format']
		yt = YouTube(url)
		print(radio)
		strObj = yt.title
		print(strObj)
		save_name = ''.join((filter(lambda x: x in ['q','e','r','t','y','u','i','','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M','ആ','എ','ഈ','ഇ','ഉ','ന','മ','സ','അ','യ','ക്ക','ക','ത','ഥ','ര','ജ','ച','ച്ച','ല','ണ്','','ന്ന','പ','','പ്പ','ഷ','ശ','വ'], strObj)))
		save_name=save_name+'CPDownload'
		if radio == 'video':
			print('inside video block')
			
			yt.streams.filter(type = 'video').first().download(output_path = save_path, filename = save_name)
			print('download completed')
			save_name=save_name+'.mp4'
			return render(request, "index.html",{'yt' : yt,'save_name' : save_name,'save_path' : save_path})

		elif radio == 'audio':
			print('inside audio block')
			#save_name=save_name
			yt.streams.filter(mime_type= 'audio/webm').first().download(output_path = save_path, filename = save_name)
			print('download completed')
			save_name=save_name+'.webm'
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