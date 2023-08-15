import os, re
from typing import Optional
from pytube import YouTube, Playlist
from pytube.exceptions import AgeRestrictedError

# folder = r'download\\'


# download_path = 'C:\\Users\\ravik\\Downloads\\venky\\movies\\'
download_path = os.environ['USERPROFILE'] + '\\OneDrive\\Documents\\youtube\\'


# play_lists = [  ['English Dubbed Movies',                'https://www.youtube.com/playlist?list=PL17vMTOwlYVM606zpRWkUSvLuiDTsowdC']]

missed_urls = [ ]

def youtube_downloader(url, destination_folder, id, total_videos):
    
    err_count = 0
    
    while err_count<=3:
        try:
            ytv = YouTube(url)
            file_name = f'video_{id} {ytv.title}'
            file_name = re.sub(r'[^a-zA-Z0-9]', ' ', file_name)
            file_name = file_name.replace('  ', ' ').replace('  ',' ') + '.mp4'
            
            # import time
            
            # print(ytv.streams.get_highest_resolution().download)
            
            # time.sleep(60)
            
            # ytv.streams.get_highest_resolution().download(output_path=destination_folder, 
            #                             filename=file_name)
            
            ytv.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(output_path=destination_folder, 
                                        filename=file_name)
            
            if os.path.exists(destination_folder+file_name):
                print(f'\tVideo {id} of {total_videos} done.')
                break
            else:
                raise ValueError
        
        except:
            if err_count == 3:
                missed_urls.append(url)
                break
            
            err_count = err_count + 1


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
            # ytv = YouTube(video)
            
            # file_name = f'video_{id} {ytv.title}'
            # file_name = re.sub(r'[^a-zA-Z0-9]', ' ', file_name)
            # file_name = file_name.replace('  ', ' ') + '.mp4'
            
        
            # try:
            #     if ytv.streams.get_by_resolution("720p") != None:
            #         ytv_streams = ytv.streams.get_by_resolution("720p")
            #         ytv_streams.download(output_path=destination_folder, filename= file_name)
                
                
            #     elif ytv.streams.get_by_resolution("480p") != None:
            #         ytv_streams = ytv.streams.get_by_resolution("480p")
            #         ytv_streams.download(output_path=destination_folder, filename= file_name)
                

            #     else:
            #         ytv_streams = ytv.streams.get_by_resolution("360p")
            #         ytv_streams.download(output_path=destination_folder, filename= file_name)
                        
            # except:
            #     with open('missed_downloads.txt', 'a') as f:
            #         f.write(f'{play_list[0]} : video_{id}: {video}\n')
                    
            
            youtube_downloader(video, destination_folder, id, total_videos )
            # print(f'\tVideo {id} of {total_videos} done.')
                            
            id += 1
        
        
        
        print(f'{play_list[0]} done')
        print('********************************************************')
    with open('missed_downloads.txt', 'a') as f:
        f.write(missed_urls)
