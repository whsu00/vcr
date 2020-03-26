import os
default_URL = ["a", "b", "c", "d", "e", "f"];

def download_video(URL_list): #used to download lists of specific videos
	for URL in URL_list:
		print("downloading "+ URL)
		if("youtube.com/watch" in URL):
			os.system('cmd /c ' + 'youtube-dl ' + URL + ' -x --no-playlist --write-sub --sub-lang en')
		else:
			print(URL + " is not a valid youtube URL.")

def download_playlist(playlist_link): 
	for URL in playlist_link:
		print("downloading "+ URL)
		if("youtube.com/playlist" in playlist_link):
			os.system('cmd /c ' + 'youtube-dl ' + URL + '  -x --yes-playlist --write-sub --sub-lang en')
		else:
			print(URL + " is not a valid youtube URL.")

if __name__ == "__main__":
	download_video(default_URL)