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
# API Keys
lastfm_public='fe81b64975b837f106e6997c9b67573b'
lastfm_secret='f32a9fec5220445fdebeaa6862fe313b'
spotify_public='a39851851cfb494399cc9131fa97f835'
spotify_secret='c9b060e76f08423eada8fe2c0e8b26dd'


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