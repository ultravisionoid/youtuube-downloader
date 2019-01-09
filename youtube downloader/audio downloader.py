from pytube import YouTube
import time
while True:
	try:	
		yt = YouTube(str(input("Enter the video link: ")))
	except:
		print("Invalid URL or copyrighted")
		print("Try Again kyon darr k age jeet hai")
	else:
		break

print("Loading")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
videos = yt.streams.filter(only_audio=True).all()
s = 1
for v in videos:
    print(str(s)+". "+str(v))
    s += 1

n = int(input("Enter the number of the video: "))
vid = videos[n-1]
destination = str(input("Enter the destination: "))
print("downloading")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
a=vid.download(destination)
print(str(yt)+"\nHas been successfully downloaded")
print("Thanks for using this wonderful program")