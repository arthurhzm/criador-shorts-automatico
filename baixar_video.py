import os
from yt_dlp import YoutubeDL

def baixar_video(url, pasta='videos'):

    if not os.path.exists(pasta):
        os.makedirs(pasta)

    ydl_opts = {
        'format': 'best',
        'outtmpl': f'{pasta}/%(title)s.%(ext)s',
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def main():
    url = 'https://www.youtube.com/watch?v=3QNbk0TVDa8'
    baixar_video(url)

if __name__ == '__main__':
    main()