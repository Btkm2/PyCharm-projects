from pytube import YouTube
# link = input("Enter link to the video:")
video = YouTube('https://www.youtube.com/watch?v=-UpRqeCMi98')
# video = video.get('mp4','720p')
# video.download('/Downloads')
video = video.streams.get_highest_resolution()
video.download()
#YouTube('https://www.youtube.com/watch?v=-UpRqeCMi98').streams.first().download()