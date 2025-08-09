# Nicolas Valdez Tue Jul  1 17:53:42 2025
# AutoFindTrackGenre
# Automatically call last.fm API to find the genres associated with
# a track for all music posts in CleanedTracks.csv
# Input(s)
# CleanedTracks.csv
# Output
# MusicGenres.csv
# FailedSongs.csv
# Main Resources
# https://www.dataquest.io/blog/last-fm-api-python/
# https://www.last.fm/api/show/artist.getTopTags
# https://docs.python.org/3/library/json.html

import requests
import csv
import time

# Welcoming Statement
print('Automatically call last.fm API to find track genre for all music posts in MusicChannelMaster.xlsx\n')

# Import csv
file_name='CleanedTracks.csv'

# Base URL
base_url='https://ws.audioscrobbler.com/2.0/'

# Headers
user_agent='Dataquest'
headers={'user-agent':user_agent}

# Delimiter
delimiter='%'

# Auth manager
keys=[]
keys_file_name='APIKeys.csv'
with open(keys_file_name,'r',newline='') as in_file:
    reader=csv.reader(in_file,delimiter=delimiter)
    for row in reader:
        keys.append(row)

# Payload constants
api_key='fe81b64975b837f106e6997c9b67573b'
method='artist.gettoptags'
format_='json'
autocorrect=1

# Set payload variables
def payload_info(api_key,method,format_,song):
    track=song['Track']
    artist=song['Artist']
    payload={
        'api_key':api_key,
        'method':method,
        'format':format_,
        'autocorrect':autocorrect,
        'track':track,
        'artist':artist,
        }
    return(payload)

# Create API request
def get_request(payload,header=headers,base_url=base_url):
    response=requests.get(base_url,headers=header,params=payload)
    return(response) 

# Place csv contents into a list as a tuple
track_and_artist=[]
with open(file_name,'r') as in_file:
    csvreader=csv.DictReader(in_file,delimiter='%')
    for row in csvreader:
        track_and_artist.append(row)

# Get and print API call status
def API_status(r,payload):
    status=r.status_code
    t=payload['track']
    c=payload['artist']
    print(f'Status Code: {status}')
    print(f'Track: {t}')
    print(f'Artist: {c}')
    return(t,c)

# Check for zero tags
def no_tags_error(tags):
    if len(tags)==0:
        raise ZeroDivisionError
        
# Get top tags
def get_top_tags(r,num_tags):
    tags=r.json()['toptags']
    song_tags=[]
    for t in tags['tag'][:num_tags]:
        name=t['name'].title()
        song_tags.append(name)
    no_tags_error(song_tags)
    print(f'{song_tags}\n')
    return(song_tags)
    
# API call constants
num_tags=3
rate_limit=0.3 # In seconds

# Genre export files
export_file_1='MusicGenres.csv'
export_file_2='FailedToFindGenres.csv'
col1='Date'
col2='Track'
col3='Artist'
col4='Tags'

# Write headers
with open(export_file_1,'w',encoding='utf-8') as in_file:
    in_file.write(f'{col1}{delimiter}{col2}{delimiter}{col3}{delimiter}{col4}\n')
with open(export_file_2,'w',encoding='utf-8') as in_file:
    in_file.write(f'{col1}{delimiter}{col2}{delimiter}{col3}\n')

# Append songs to export_file_2
def write_to_failed(song,export_file=export_file_2,delimiter=delimiter,col1=col1,col2=col2):
    with open(export_file,'a') as in_file:
        in_file.write(f'{d}{delimiter}{t}{delimiter}{c}\n')

progress=0
total=len(track_and_artist)
for song in track_and_artist:
    try:
        # Show progress
        progress+=1
        print(f'{progress}/{total}')
        
        # Make API call
        payload=payload_info(api_key,method,format_,song)
        r=get_request(payload)
        
        # Call status
        info=API_status(r,payload)
        d=song['Date']
        t=info[0]
        c=info[1]
        song_info=f'{c} - {t}'
        
        # Get top tags only
        song_tags=get_top_tags(r,num_tags)
        
        # Append track and artist to export_file_1
        with open(export_file_1,'a') as in_file:
            in_file.write(f'{d}{delimiter}{t}{delimiter}{c}{delimiter}{song_tags}\n')

        pass
    except KeyError:
        write_to_failed(song)
        print('Song failed to parse.\n')
        pass
    except ZeroDivisionError:
        write_to_failed(song)
        print('No tags exist.\n')
        pass 
    except:
        write_to_failed(song)
        print('Unknown Error Occurred.\n')
        pass
    time.sleep(rate_limit)

# Ending Note
print('Program Ends')