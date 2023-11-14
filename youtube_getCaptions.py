# This script collects French captions from videos posted by a list of YouTube channels (must collect video URLs from a separate script first)

from yt_dlp import YoutubeDL
import re, os, webvtt

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

for channel in channels:
    print("\nCollecting captions from channel "+channel)
    videos = open('ytURLs_'+channel+'.txt', 'r', encoding="UTF-8").readlines()
    for index,video in enumerate(videos):
        print("- Working on video #" + str(index + 1) + " of " + str(len(videos)) + ": " + re.sub('\n','',video) + " (" + channel + ")")
        vtt_label = "subs_"+channel+str(index+1)
        with YoutubeDL({'quiet':True, 'cookiesfrombrowser':('firefox', )}) as ydl:
            info = ydl.extract_info(video, download=False)
        if 'fr' in list(info['subtitles'].keys()): # If there are French subtitles, use those
            subs_report = '     French subtitles found and written to file.'
            subs_opts = {'outtmpl':vtt_label, 'subtitleslangs': ['fr'], 'writesubtitles': True, 'skip_download':True, 'quiet':True, 'cookiesfrombrowser':('firefox', )}
            vtt_file = vtt_label+'.fr.vtt'
        elif 'fr-orig' in list(info['automatic_captions'].keys()): # Or else if there are at least original French auto-generated captions, use those
            subs_report = '     French auto-generated captions found and written to file.'
            subs_opts = {'outtmpl':vtt_label, 'subtitleslangs': ['fr-orig'], 'writeautomaticsub': True, 'skip_download':True, 'quiet':True, 'cookiesfrombrowser':('firefox', )}
            vtt_file = vtt_label+'.fr-orig.vtt'
        else:
            print('     No French subtitles or auto-generated captions found.')
            continue # If no French subtitles or auto-generated captions, skip to the next video
        with YoutubeDL(subs_opts) as ydl: # Download the subtitles/captions as a .vtt file
            ydl.download(video)
        with open('ytCaptions_'+channel+'.txt', 'a+', encoding='UTF-8') as output: # Append the .vtt file to channel's .txt file, removing timestamps
            for caption in webvtt.read(vtt_file):
                output.write(re.sub('&nbsp;',' ',caption.text) + '\n')
        print(subs_report)
        os.remove(vtt_file) # Remove the now-obsolete .vtt file
        
