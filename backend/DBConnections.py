from decimal import localcontext
import pymysql

#db connection
#connection = pymysql.connect(
#        host='10.254.254.25', 
#        user='skp', 
#        passwd='SKP2017!', 
#        database='skp_servicedesk', 
#        port=3306, 
#        charset='utf8'
#)

#change with own DB
localConnection = pymysql.connect(
        host='localhost', 
        user='root', 
        database='skp_servicedesk', 
        port=3307, 
        charset='utf8'
)
cursor = localConnection.cursor()

def getAll():
        cursor.execute("SELECT * FROM ervicedesk_bruger")
        result = cursor.fetchall()
        printResult = ""

        for row in result:
                printResult += f"{row}\n\n"
        return printResult


def GetLoginUser(username):
        cursor.execute(f"SELECT brugernavn, password FROM servicedesk_bruger WHERE brugernavn = '{username}' ")
        queryResult = cursor.fetchone()
        cursor.close
        return queryResult

def CreateUser(username, passw, firstname):
        sql = f'''INSERT INTO servicedesk_bruger 
                (navn, brugernavn, password, user_level, education, edu_id) 
                VALUES ('{firstname}', '{username}', '{passw}', 1, 'Test', 1)'''

        cursor.execute(sql)
        localConnection.commit()
