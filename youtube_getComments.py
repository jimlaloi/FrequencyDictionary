# This script collects comments from videos posted by a list of YouTube channels (must collect video URLs from a separate script first)

from yt_dlp import YoutubeDL
import re

channels = {
    'Cyprien':'https://www.youtube.com/c/cyprien',
    'Squeezie':'https://www.youtube.com/channel/UCWeg2Pkate69NFdBeuRFTAw',
    'Tibo InShape':'https://www.youtube.com/channel/UCpWaR3gNAQGsX48cIlQC0qw',
    'Lama Faché':'https://www.youtube.com/channel/UCH0XvUpYcxn4V0iZGnZXMnQ',
    'Michou':'https://www.youtube.com/channel/UCo3i0nUzZjjLuM7VjAVz4zA',
    'Amixem':'https://www.youtube.com/channel/UCgvqvBoSHB1ctlyyhoHrGwQ',
    'Rémi Gaillard':'https://www.youtube.com/channel/UCmPSwsooZq8an7xOLQQhAdw',
    'Mcfly et Carlito':'https://www.youtube.com/channel/UCDPK_MTu3uTUFJXRVcTJcEw',
    'Inoxtag':'https://www.youtube.com/channel/UCL9aTJb0ur4sovxcppAopEw',
    'Mister V':'https://www.youtube.com/channel/UC8Q0SLrZLiTj5s4qc9aad-w',
    'Swan et Néo':'https://www.youtube.com/c/swanthevoice',
    'Kevin Tran':'https://www.youtube.com/channel/UCTt2AnK--mnRmICnf-CCcrw'
}

print('There are '+str(len(channels))+' channels provided')

maxvideos = 100 # How many videos per channel to collect comments from.
maxcomments = ['100'] # ['all'] = all comments; ['100'] = max 100 comments; ['1000','all','100','10'] = max 1000 comments, max all parents, max 100 replies total, max 10 replies per thread

for channel in channels:
    print("\nCollecting comments from channel "+channel)
    videos = open('ytURLs_'+channel+'.txt', 'r', encoding="UTF-8").readlines()
    videos = videos[:maxvideos]
    for index,video in enumerate(videos):
        print("- Collecting comments from video #" + str(index + 1) + " of " + str(len(videos[:maxvideos])) + ": " + re.sub('\n','',video) + " (" + channel + ")")
        comments_opts = {'getcomments':True, 'quiet':True, 'extractor_args': {'youtube': {'max_comments': maxcomments}}, 'cookiesfrombrowser':('firefox', )}
        with YoutubeDL(comments_opts) as ydl:
            info = ydl.extract_info(video, download=False)
        if info['comments'] is None:
            print('     No comments found for video '+video)
        else:
            comments_count = len(info['comments'])
            for comment in info['comments']:
                if comment['text'] is not None:
                    with open('ytComments_'+channel+'.txt', 'a+', encoding='UTF-8') as output:
                        output.write(comment['text']+'\n')
            print('     '+str(comments_count)+' comments found and written to file')

