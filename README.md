# music-channel
Welcome to my data analysis project. This is a project I have spent a month or so working on. 

- What was the purpose of this project?
I made this project in an attempt to satisfy a few questions my friends and I had about our collective music taste. These four questions were:
1. What genres of music is most commonly shared?
2. What genres do each person share the most of?
3. Has the collective music taste changed over time?
4. Can we create a playlist of every song?

- How was the data collected?
I used an external tool to scrape messages off a Discord text channel designated for posting and discussing music. The messages are exported to a CSV file and imported into a Microsoft Excel document.

- How was the data cleaned?
The raw data that was scraped off of the Discord text channel contained a lot of additional bloat that was necessary to clean before doing anything useful with the data. I decided that using Excel's Power Query feature to make and record every change would be my best bet for most parts of the project.

- What was done with the data?
I split up the dataset based on the domain of the link each message contained. The dataset mostly comprised of Youtube links and Spotify links.

For the Youtube links, I used the Python API library ytmusicapi to grab the title of the video link and the Youtube channel it was posted from.

After some additional work with the new data in Excel, I then had to associate each youtube video with a song registered on last.fm, a music tracking website. This was done with Python by using last.fm's API to make a search using the data I previously found to get the highest relevance song found on last.fm's library.

After that, the next step was fairly simple. I used another one of last.fm's API functions to get the top three tags (genres) that were most closely associated with the artist. I decided to not use the individual song's tags because getting an artist's tags yielded a significantly higher number of successful results.

For the Spotify links, I used the Python API library Spotipy to directly grab the top three genres associated with the artist.

In regards to making the playlist, I tried for quite a while to write my own program, however I simply did not have the necessary knowledge to make anything functioning. So after some searching, I found a wonderful program to do all the hard parts for me and I modified the program as necessary to accomplish what I needed it to do. The original code is linked in the program.

- What did we find out from the data?
The following makes conlusions from the PivotChart with the name, "Simplified Filtered": The most popular genre by a sizeable margin was unsurprisingly pop. In terms of the cumulative average by yearly quarter (Q1-24 to Q3-25), pop has consistently reigned supreme. However, when taking a closer look at the individual rankings for each quarter, we can see that pop's dominance is not unbeatable. Q2-25 and Q3-25 see rock and hip hop taking the top spot. The all time rankings show pop music at number one making up a staggering 28% of all music posted. Second place goes to rock music at 14% of all music posted, only half the number that pop music has. Electronic music takes third place with 12%, just barely behind second place's 14%. Lastly, hip hop, metal, and rap music tie for forth, each comprising exactly 6% of the music.

On another note, we can see that user posts linking Spotify have dwindled as time has gone on. I am unsure whether or not this is due to people using YouTube more often to listen to their music or perhaps people just found it convenient to have all of the music posted to be from the same domain. The other domains very occassionally seen (Bandcamp, Twitter, etc.) make up such a small percentage that there isn't particularly anything noteworthy to say about them.

- What problems did I encounterduring this project?
There were countless problems I had to deal with while working on this project. As someone who has only taken one course on Python and has only vaguely interacted with APIs in the past, I had to figure out most of the critical componenents on the fly. As to be expected, everything API related 

- How to update the data:
1. Open DiscordChatExporter.exe
2. Select music text channel and export to CSV (You are finished using this program)
3. Open MusicChannelMaster.xlsx
4. From the Data tab, get data from Text/CSV
5. Select the scraped CSV (from step 2)
6. After importing the new CSV creates a new worksheet with a table, create a query from the new table
7. Delete the old Raw Data query
8. Rename newly created query to "Raw Data"
9. Press the "Close & Load" button
10. Rename the new table from "Raw_Data_" to "Raw_Data"
11. Press the "Refresh All" button
12. Save MusicChannelMaster.xlsx (You are finished using Excel until step 15)
13. Open the python program GetChannelAndTrack.py
14. Run the program GetChannelAndTrack.py (You are finished using this program)
15. Open MusicChannelMaster.xlsx if not already open from previous steps
16. Open the TrackAndChannel query
17. In Power Query, press the "Refresh All" Button
18. Press the "Close & Load" button
19. Save MusicChannelMaster.xlsx (You are finished using Excel until step 24)
20. Open the python program MusicNamesCleaned.py
21. Run the program MusicNamesCleaned.py (You are finished using this program)
22. Open the python program AutoFindTrackGenre.py
23. Run the program AutoFindTrackGenre.py (You are finished using this program)
24. Open MusicChannelMaster.xlsx if not already open from previous steps
25. Open the YTMusicGenres query
26. In Power Query, press the "Refresh All" Button
27. Press the "Close & Load" button
28. Save MusicChannelMaster.xlsx (You are finished using Excel until step 24)
29. If there are new Spotify links since the last update, continue to step 30. If there are no new Spotify links since the last update, skip to step 36. 
30. Open the python program SpotifyFindGenre.py
31. Run the program SpotifyFindGenre.py (You are finished using this program)
32. Open MusicChannelMaster.xlsx if not already open from previous steps
33. Open the SpotifyMusicGenres query
34. In Power Query, press the "Refresh All" Button
35. Press the "Close & Load" button
36. Press the "Refresh All" button (Not the one in power query. This is to refresh all tables, not just the query. Same button as in step 11 and step 28)
37. Save MusicChannelMaster.xlsx (You are finished using Excel)
38. Open youtube_playlist_creator.py
39. Verify the value assigned to the "progress" variable
40. Run the program youtube_playlist_creator.py (You are finished using this program)
41. Update the progress variable accordingly
42. You are finished.
