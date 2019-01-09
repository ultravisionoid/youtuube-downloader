from pytube import YouTube
import time
while True:
	try:	
		yt = YouTube(str(input("Enter the video link: ")))
	except:
		print("Try again with a valid URL")
	else:
		break

print("Loading")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
videos = yt.streams.all()
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
vid.download(destination)
print(str(yt)+"\nHas been successfully downloaded")
