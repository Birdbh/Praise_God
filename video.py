from pexelsapi.pexels import Pexels
import urllib.request
import random

DURATION = 25
API_KEY = "563492ad6f91700001000001fad60931680547f0a8399fd0e62a8a6f"
NUMBER_OF_PAGES = 25

VIDEO_WIDTH = 1080
VIDEO_HEIGHT = 1920

def getvideo(video_string):

    '''Use Pexels API to Videos With Search Query'''
    pexels = Pexels(API_KEY)
    raw_API_data = pexels.search_videos(query=video_string, orientation='portrait', page=1, per_page=80).get("videos")
    for i in range(2,NUMBER_OF_PAGES):
        raw_API_data += pexels.search_videos(query=video_string, orientation='portrait', page=i, per_page=80).get("videos")

    while True:

        '''Select random video file in the pulled Video Files'''
        random_all_video_entry = random.choice(raw_API_data)
        
        '''Loop through all videos for that video and find until one is found that matches the size and duration requriments'''
        for vid in random_all_video_entry.get("video_files"):
            
            if vid.get("width") == VIDEO_WIDTH and vid.get("height") == VIDEO_HEIGHT and random_all_video_entry.get("duration") >= DURATION:

                return(urllib.request.urlretrieve(vid.get("link"), video_string+".mp4"))
