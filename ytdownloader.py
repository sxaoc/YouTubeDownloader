# Moduls مكتبات
import time
from pytube import YouTube
from sys import platform, argv
from os import system
clear = 'clear'
if platform == 'win32':
	init()
	clear = 'cls'	
	
# Finish Arabic
def finishar():
	print(' ')
	print('تم التحميل بنجاح.\nالفيديو او الاغنيه تم حفظه في ملف.')
	
# Finish Engilsh	
def finishen():
	print(' ')
	print('Downlaod is done.\nVideo or Audio saved in File')	

# Finish Dutch
def finishnl():
	print(' ')
	print('Het downloaden is voltooid.\nVideo of Audio is opgeslagen in bestand')	
	
# Return Arabic	
def returnqar():
	print('\n')
	print('\n')
	back = input('(تريد الرجوع: (اي) او (لا)\n\n==> ')
	print('\n')
	if back == 'اي':
		startar()
	else:
		exit()
		
# Return Engilsh		
def returnqen():
	print('\n')
	print('\n')
	back = input('Do you want back: (yes) or (no)\n\n==> ')
	print('\n')
	if back == 'yes':
		starten()
	else:
		exit()
		
# Return Dutch		
def returnqnl():
	print('\n')
	print('\n')
	back = input('Wil je terug: (ja) of (nee)\n\n==> ')
	print('\n')
	if back == 'ja':
		startnl()
	else:
		exit()
		
# My Logo			
def logo():
	system(clear)
	print('''
	
-----------------------------------------	
░██████╗██╗░░██╗░█████╗░░█████╗░░█████╗░
██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔══██╗
╚█████╗░░╚███╔╝░███████║██║░░██║██║░░╚═╝
░╚═══██╗░██╔██╗░██╔══██║██║░░██║██║░░██╗
██████╔╝██╔╝╚██╗██║░░██║╚█████╔╝╚█████╔╝
╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░░╚════╝░

𝗜𝗻𝘀𝘁𝗮𝗴𝗿𝗮𝗺: www.instagram.com/sxaoc
𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺: t.me/sxaoc
Developer: .🇷🇺 انس
-----------------------------------------

	''')
	print('\n')
	
# Download Arabic	
def downlaodar():
	print('\n')
	link = input('رابط المقطع : ')
	va = YouTube(link)
	filename1 = input('\nاسم لي المقطع او الصوت :  ')
	print('''
	
	(1) مقطع
	
	(2) صوت
	
	(3) مقطع وصوت
	
	''')
	ans1 = input('==>  ')
	if ans1 == '1':
		va.streams.get_highest_resolution().download(output_path='videos', filename=filename1)
		va.register_on_complete_callback(finishar())
		returnqar()	
	elif ans1 == '2':
		va.streams.get_audio_only().download(output_path='audios', filename=filename1)
		va.register_on_complete_callback(finishar())
		returnqar()		
	elif ans1 == '3':
		va.streams.get_highest_resolution().download(output_path='videos', filename=filename1)
		va.register_on_complete_callback(finishar())
		
		va.streams.get_audio_only().download(output_path='audios', filename=filename1)
		va.register_on_complete_callback(finishar())
		returnqar()
	else:
		downlaodar()
		
# Download English				
def downlaoden():
	print('\n')
	link = input('Video link : ')
	va = YouTube(link)
	filename1 = input('\nName for video or sound :  ')
	print('''
	
	(1) Video
	
	(2) Sound
	
	(3) Video and Sound
	
	''')	
	ans1 = input('==>  ')
	if ans1 == '1':
		va.streams.get_highest_resolution().download(output_path='videos', filename=filename1)
		va.register_on_complete_callback(finishen())
		returnqen()					
	elif ans1 == '2':
		va.streams.get_audio_only().download(output_path='audios', filename=filename1)
		va.register_on_complete_callback(finishen())
		returnqen()						
	elif ans1 == '3':
		va.streams.get_highest_resolution().download(output_path='videos', filename=filename1)
		va.register_on_complete_callback(finishen())
		va.streams.get_audio_only().download(output_path='audios', filename=filename1)
		va.register_on_complete_callback(finishen())
		returnqen()
	else:
		downlaoden()	

# Download Dutch				
def downlaodnl():
	print('\n')
	link = input('Video link : ')
	va = YouTube(link)
	filename1 = input('\nNaam voor video of geluid :  ')
	print('''
	
	(1) Video
	
	(2) Geluid
	
	(3) Video en Geluid
	
	''')	
	ans1 = input('==>  ')
	if ans1 == '1':
		va.streams.get_highest_resolution().download(output_path='videos', filename=filename1)
		va.register_on_complete_callback(finishen())
		returnqnl()					
	elif ans1 == '2':
		va.streams.get_audio_only().download(output_path='audios', filename=filename1)
		va.register_on_complete_callback(finishen())
		returnqnl()						
	elif ans1 == '3':
		va.streams.get_highest_resolution().download(output_path='videos', filename=filename1)
		va.register_on_complete_callback(finishen())
		va.streams.get_audio_only().download(output_path='audios', filename=filename1)
		va.register_on_complete_callback(finishen())
		returnqnl()
	else:
		downlaodnl()	
			
# Info Video Arabic							
def infovideoar():
	print('\n')
	link = input('رابط المقطع : ')
	va = YouTube(link)
	print('\n\n')
	print('\n\n')
	print(f'عنوان المقطع : \n\n\n\n {va.title} \n\n-----------------------------------------------')
	print(' ')
	print(f'وصف المقطع : \n\n\n\n {va.description} \n\n-----------------------------------------------')
	print(' ')
	print(f'مشاهدات المفطع : \n\n\n\n {va.views} \n\n-----------------------------------------------')
	print(' ')
	print(f'تقييم المقطع : \n\n\n\n {va.rating} \n\n-----------------------------------------------')	
	print(' ')
	print(f'ايدي المقطع : \n\n\n\n {va.video_id} \n\n-----------------------------------------------')
	returnqar()
	
# Info Video Engilsh	
def infovideoen():
	print('\n')
	link = input('Video link : ')
	va = YouTube(link)
	print('\n\n')
	print('\n\n')
	print(f'Video title : \n\n\n\n {va.title} \n\n-----------------------------------------------')
	print(' ')
	print(f'Video description : \n\n\n\n {va.description} \n\n-----------------------------------------------')
	print(' ')
	print(f'Video views : \n\n\n\n {va.views} \n\n-----------------------------------------------')
	print(' ')
	print(f'Video rating : \n\n\n\n {va.rating} \n\n-----------------------------------------------')	
	print(' ')
	print(f'Video id : \n\n\n\n {va.video_id} \n\n-----------------------------------------------')
	returnqen()	
						
# Info Video Dutch	
def infovideonl():
	print('\n')
	link = input('Video link : ')
	va = YouTube(link)
	print('\n\n')
	print('\n\n')
	print(f'Titel van de video : \n\n\n\n {va.title} \n\n-----------------------------------------------')
	print(' ')
	print(f'Video beschrijving : \n\n\n\n {va.description} \n\n-----------------------------------------------')
	print(' ')
	print(f'Video kijkers : \n\n\n\n {va.views} \n\n-----------------------------------------------')
	print(' ')
	print(f'Videobeoordeling : \n\n\n\n {va.rating} \n\n-----------------------------------------------')	
	print(' ')
	print(f'Video id : \n\n\n\n {va.video_id} \n\n-----------------------------------------------')
	returnqnl()	
	
# Taal Arabic
def startar():
	print('''
	
	(1) تحميل من اليوتيوب
	
	(2) معلومات عن المقطع

(3) تغيير اللغه
	
	''')
	sxaocyt = input('==>  ')
	if sxaocyt == '1':
		downlaodar()
	elif sxaocyt == '2':
		infovideoar()
	elif sxaocyt == '3':
		taal()
	else:
		startar()

# Taal English
def starten():
	print('''
	
	(1) Download video
	
	(2) Info about video
	
	(3) Change the language
	
	''')
	sxaocyt = input('==>  ')
	if sxaocyt == '1':
		downlaoden()
	elif sxaocyt == '2':
		infovideoen()
	elif sxaocyt == '3':
		taal()
	else:
		starten()	
		
# Taal Dutch
def startnl():
	print('''
	
	(1) Download video
	
	(2) Info over video
	
	(3) Verander de taal
	
	''')
	sxaocyt = input('==>  ')
	if sxaocyt == '1':
		downlaodnl()
	elif sxaocyt == '2':
		infovideonl()
	elif sxaocyt == '3':
		taal()
	else:
		startnl()	
		
# Taal
def taal():
	print('\n')
	print('''
	
	(1) Arabic
	
	(2) English
	
	(3) Dutch
	
	''')
	taala = input('==>  ')
	if taala == '1':
		startar()
		downlaodar()
	elif taala == '2':
		starten()
		downlaoden()
	elif taala == '3':
		startnl()
		downlaodnl()
	else:
		taal()	

# Start
logo()
time.sleep(1)
taal()
