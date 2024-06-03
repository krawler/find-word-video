import requests
import mysql.connector

mysql_db = mysql.connector.Connect(
             host = "findwordvideo.mysql.dbaas.com.br",
             user = "findwordvideo",
             password = "Locaweb@2",
             database = "findwordvideo"
           )
data_cursor = mysql_db.cursor()

url_base = 'https://www.googleapis.com/youtube/v3/search'
channelId = 'UCFFurfgqfhSLu5DHbF0bjRQ'
key = 'AIzaSyD2w-ddoLfBS0MXHdk4BijQg2Sbhq9daXg'

requestStr = f'{url_base}?part=id%2Csnippet&channelId={channelId}&key={key}&maxResults=20&type=video&order=date'

response = requests.get(requestStr)

json = response.json()

videos = []
for item in json['items']:
    if item['id'].get('channelId') == None:
        video_item = {
            "kind" : item['kind'],
            "etag" : item['etag'], 
            "videoId" : item['id']['videoId'],            
            "title" : item['snippet']['title'],
            "description" : item['snippet']['description'],
           # "publishedAt" : item['snippet']['publishedAt'], NAO APARECEU EM ALGUNS INTENS
            "publishTime" : item['snippet']['publishTime'],
            "thumbnail_default" : item['snippet']['thumbnails']['default']['url']
        } 
        videos.append(video_item)

rows_vals = []
for video_dic in videos:
    val = (video_dic['kind'], video_dic['etag'], video_dic['videoId'], video_dic['title'], 
                video_dic['description'], video_dic['publishTime'], video_dic['thumbnail_default']) 
    rows_vals.append(val)
    #for key, val in video_dic.items():
        

#TODO: mudar nome de campo para ingles
sql = "INSERT INTO video_inf(kind, etag, videoId, title, description, data_publicacao, thumbnail_default)"
sql += " VALUES(%s, %s, %s, %s, %s, %s, %s)"

try:
    data_cursor.executemany(sql, rows_vals)
    mysql_db.commit()    
except e:
    print(f'uma excecao ocorreu {e}')             