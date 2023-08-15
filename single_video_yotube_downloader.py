import os, re
from typing import Optional
from pytube import YouTube, Playlist
from pytube.exceptions import AgeRestrictedError

# folder = r'download\\'



# download_path = 'C:\\Users\\VENKY\\Documents\\youtube\\'
download_path = 'C:\\Users\\thota\\Downloads\\'

def downloader(video_urls, resolution='h'):

    if os.path.exists('missed_downloads.txt'):
        os.unlink('missed_downloads.txt')

    for video_url in video_urls:
        
        ytv = YouTube(video_url)
        file_name = f'{ytv.title}'
        file_name = re.sub(r'[^a-zA-Z0-9]', ' ', file_name)
        file_name = file_name.replace('  ', ' ') + '.mp4'
    
        try:
            
            if ytv.streams.get_by_resolution("1080p") != None and resolution == 'hd':
                # print('1080')
                ytv_streams = ytv.streams.get_by_resolution("1080p")
                ytv_streams.download(output_path=download_path, filename= file_name)
            
            elif ytv.streams.get_by_resolution("720p") != None:
                # print('720')
                ytv_streams = ytv.streams.get_by_resolution("720p")
                ytv_streams.download(output_path=download_path, filename= file_name)
            
            
            elif ytv.streams.get_by_resolution("480p") != None:
                ytv_streams = ytv.streams.get_by_resolution("480p")
                ytv_streams.download(output_path=download_path, filename= file_name)
            

            else:
                ytv_streams = ytv.streams.get_by_resolution("360p")
                ytv_streams.download(output_path=download_path, filename= file_name)
                    
        except:
            print(video_url)
        
        
        print(f'{file_name} done.')
        
        
        
