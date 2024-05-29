from googleapiclient.discovery import build

youtubeApiKey = "AIzaSyD2w-ddoLfBS0MXHdk4BijQg2Sbhq9daXg"

youtube = build('youtube', 'v3', developerKey=youtubeApiKey)

playlistId = 'PLTlOEu19cJGRHNu_WJ4jlOFaAQElptF5-'
playlistName = 'Reflexão'
next_Page_token = None

playlist_videos = []

res = youtube.playlistItems().list(part='snippet', playlistId=playlistId, maxResults=15).execute()

playlist_videos = res['items']

videoIds = list(map(lambda x:x['snippet']['resourceId']['videoId'], playlist_videos))

stats = []
for video in playlist_videos:
    videoId = video['snippet']['resourceId']['videoId']
    res = youtube.videos().list(part='statistics', id=videoId).execute()
    
    video_title = video['snippet']['title']
    video_description = video['snippet']['description']
    liked = res['items'][0]['statistics']['likeCount']
    favorite = res['items'][0]['statistics']['favoriteCount']
    views = res['items'][0]['statistics']['viewCount']
    comment = res['items'][0]['statistics']['commentCount']
    print('video : ' + video_title)
    print('description : ' + video_description)
    print(' liked : ' + liked + '  -  favorited : ' + favorite + '  -   views : ' + views + '  -   comments : ' + comment)    