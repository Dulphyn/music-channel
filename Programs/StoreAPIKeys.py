# Nicolas Valdez Sat Jul 19 14:14:27 2025
# StoreAPIKeys
# Write to file last.fm and Spotify API keys 
# Input(s)
# None
# Output
# CSV file containing last.fm and Spotify API keys

import csv

# Welcoming Statement
print('Write to file last.fm and Spotify API keys.')

# Export file info
file_name='APIKeys.csv'
delimiter='%'
col1='lastfm'
col2='spotify'
header=(col1,col2)
# API Keys manual input
lastfm_public=
lastfm_secret=
spotify_public=
spotify_secret=


public_keys=(lastfm_public,spotify_public)
secret_keys=(lastfm_secret,spotify_secret)

with open(file_name,'w',newline='') as in_file:
    writer=csv.writer(in_file,delimiter=delimiter)
    writer.writerow(header)
    writer.writerow(public_keys)
    writer.writerow(secret_keys)

print(f'API Keys successfully written to {file_name}')
# Ending Note

print('Program Ends')
