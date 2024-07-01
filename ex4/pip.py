from pytube import Playlist

# Prompt the user to enter the playlist URL
playlist_url = input('Enter playlist URL: ')

# Create a Playlist object
playlist = Playlist(playlist_url)

# Iterate through each video in the playlist and download it
for video in playlist.videos:
    print(f'Downloading {video.title}...')
    video.streams.get_highest_resolution().download()
    print(f'Downloaded {video.title} successfully.')

print('All videos have been downloaded.')
