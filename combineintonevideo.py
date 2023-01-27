import moviepy.editor as mpe
import video 
import audio
import quote
import os

IMAGEMAGICK_BINARY = os.getenv ('IMAGEMAGICK_BINARY', 'C:\Program Files\ImageMagick-7.0.8-Q16\convert.exe')
VIDEO_QUERY = "nature"
MUSIC_FILES_LOCATION = r'C:\Users\birdl\Desktop\Year_2\Programming\Python\Praise_God\music_samples'

def combine():
    filename = video.getvideo(VIDEO_QUERY)[0]

    my_clip = mpe.VideoFileClip(filename)

    audio_background = mpe.AudioFileClip(os.path.join(MUSIC_FILES_LOCATION,audio.getaudio()))
    
    my_clip = my_clip.set_audio(audio_background)

    '''Positon key text'''

    key_text = quote.get_chapter_from_dictionary(quote.load())

    txt_clip = mpe.TextClip(key_text, fontsize=160,color='white',font="Gabriola", stroke_color="white", stroke_width = 2)
    txt_clip = txt_clip.set_position((0.1,0.15), relative=True).set_duration(video.DURATION)

    '''Position value text'''

    txt_clip2 = mpe.TextClip(quote.spliceloadedquote(key_text,quote.load()), fontsize=80,color='white',font="Aharoni", stroke_color='white', stroke_width = 2)
    txt_clip2 = txt_clip2.set_position('center').set_duration(video.DURATION)


    my_clip = mpe.CompositeVideoClip([my_clip,txt_clip,txt_clip2])

    my_clip = my_clip.subclip(0,video.DURATION)

    my_clip.ipython_display()
combine()