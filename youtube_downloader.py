import os, re
from typing import Optional
from pytube import YouTube, Playlist
from pytube.exceptions import AgeRestrictedError

# folder = r'download\\'


# download_path = 'C:\\Users\\ravik\\Downloads\\venky\\movies\\'
download_path = 'C:\\Users\\thota\\Downloads\\'



# play_lists = [  ['English Dubbed Movies',                'https://www.youtube.com/playlist?list=PL17vMTOwlYVM606zpRWkUSvLuiDTsowdC']]

def downloader(play_lists):

    if os.path.exists('missed_downloads.txt'):
        os.unlink('missed_downloads.txt')

    for play_list in play_lists:
        
        pl_url = play_list[1]
        
        folder_name = re.sub(r'[^a-zA-Z0-9& ]', '', play_list[0].strip())
        
        if folder_name.endswith('  ') or folder_name.endswith(' '):
            if folder_name.endswith('  '):
                folder_name = folder_name[:-2]
            if folder_name.endswith(' '):
                folder_name = folder_name[:-1]
        
        if folder_name.startswith('  ') or folder_name.startswith(' '):
            if folder_name.startswith('  '):
                folder_name = folder_name[2:]
            if folder_name.startswith(' '):
                folder_name = folder_name[1:]
        
        destination_folder = download_path + f'{folder_name}\\'
        # os.mkdir(destination_folder)
        os.makedirs(destination_folder, exist_ok=True)
        
        playlist = Playlist(pl_url)
        id = 1

        total_videos = len(playlist.video_urls)
        print(f'Total videos on playlist: {total_videos}')

        for video in playlist.video_urls:
            ytv = YouTube(video)
            
            file_name = f'video_{id} {ytv.title}'
            file_name = re.sub(r'[^a-zA-Z0-9]', ' ', file_name)
            file_name = file_name.replace('  ', ' ') + '.mp4'
        
            try:
                if ytv.streams.get_by_resolution("720p") != None:
                    ytv_streams = ytv.streams.get_by_resolution("720p")
                    ytv_streams.download(output_path=destination_folder, filename= file_name)
                
                
                elif ytv.streams.get_by_resolution("480p") != None:
                    ytv_streams = ytv.streams.get_by_resolution("480p")
                    ytv_streams.download(output_path=destination_folder, filename= file_name)
                

                else:
                    ytv_streams = ytv.streams.get_by_resolution("360p")
                    ytv_streams.download(output_path=destination_folder, filename= file_name)
                        
            except:
                with open('missed_downloads.txt', 'a') as f:
                    f.write(f'{play_list[0]} : video_{id}: {video}\n')
                    
            print(f'\tVideo {id} of {total_videos} done.')
                            
            id += 1
        print(f'{play_list[0]} done')
        print('********************************************************')
