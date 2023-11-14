# This script collects URLs for all videos posted by a list of YouTube channels

import scrapetube

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

print('There are '+str(len(channels))+' channels provided\n')

for index,channel in enumerate(channels): # Loop through each channel on the list
    print('- Collecting video URLs from '+channel+' (channel #'+str(index+1)+" of "+str(len(channels))+")")
    videos = scrapetube.get_channel(channel_url=channels[channel], content_type="videos")
    streams = scrapetube.get_channel(channel_url=channels[channel], content_type="streams")
    videolist=[]
    for video in videos:
        videolist.append(video['videoId'])
    for stream in streams:
        videolist.append(stream['videoId'])
    with open('ytURLs_'+channel+'.txt', 'w') as file:
        for i in videolist:
            file.write("https://www.youtube.com/watch?v="+i+'\n')
    print('     Found '+str(len(videolist))+' videos on the channel '+channel+'. URLs written to file.')
