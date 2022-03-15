import moviepy.editor

video=moviepy.editor.VideoFileClip("C:/Users/CodeWithShani/Desktop/video.mp4")

audio=video.audio

audio.write_audiofile("C:/Users/CodeWithShani/Desktop/Extracted_audio.mp3")