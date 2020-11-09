import requests
import os

def Information(link):
    if 'https://v.triller.co/' in link:
        r = requests.get(link)
        if 'data-id' in r.text:
            username = r.text.split('<meta property="og:title" content="')[1].split('"')[0].split(' •')[0]
            video_id = r.text.split('data-id="')[1].split('"')[0]
            views = r.text.split('<div class="video-info-plays">')[1].split('\n                        ')[1].split('\n')[0]
            upload_date = r.text.split('<span id="time-posted">')[1].split('</span>')[0]
            author_id = r.text.split('/v1/uploads/')[1].split('/')[0]
            thumbnail = r.text.split('data-poster="//')[1].split('"')[0]
            download = r.text.split('data-no-hls="//')[1].split('"')[0]
            print(f'''
[~] Author Username: {username}
[~] Author ID: {author_id}
[~] Video ID: {video_id}
[~] Video Views: {views}
[~] Video Thumbnail: {thumbnail}
[~] Video Download: {download}
[~] Upload Date: {upload_date}
            ''')
            input()
        else:
            input('Unable To Fetch')
    else:
        input('Invalid URL')

while True:
    os.system('cls')
    link = input('> ')
    Information(link)
