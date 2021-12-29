from pytube import YouTube
path = "D:"
link = input("Enter the link of the Youtube Video :")
ob = YouTube(link)
c = int(input("Enter 1 for best quality..\
\nEnter 2 for low quality..\
\nEnter your choice :"))
if (c ==1):
    quality = ob.streams.get_highest_resolution()
elif (c==2):
    quality = ob.streams.get_lowest_resolution()
print("Fetching video...Please Wait !!")
file_size = quality.filesize
ab = file_size/(1024*1024)
print(f"Video Length :{ab}")
print("Downloading Video...Please Wait !!")
quality.download(path)
print("Video Downloaded Successfully")
