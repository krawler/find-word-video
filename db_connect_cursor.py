import mysql.connector

class Db_connect_cursor:
    
    def get():
        mysql_db = mysql.connector.Connect(
             host = "findwordvideo.mysql.dbaas.com.br",
             user = "findwordvideo",
             password = "Locaweb@2",
             database = "findwordvideo"
           )
        
        return mysql_db.cursor()