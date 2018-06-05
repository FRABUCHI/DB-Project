import pymysql
from datetime import datetime

nowHour = datetime.today().hour
sentence1 = 'test.day'
sentence2 = 'num'
sentence3 = 'SQL_SAFE_UPDATES'

conn = pymysql.connect(
        host="localhost",
        user = "root",
        passwd = "dudwns",
        db = "test",
        charset = "utf8",
        use_unicode=True
    )

cur = conn.cursor()
    

#반환값 없음.
def push(keyword):

    #중복 되면 카운트 올리고 중복 아닌 키워드는 삽입하고 카운트 올림
    sql = '''
    INSERT INTO classic_keyword_list(keyword) VALUES' + '(' + search + ')'
    ON DUPLICATE UPDATE KEY num = num + 1
    '''
    cur.execute(sql)
    #검색 한번 될때마다 튜플 정리
    sql = 'select * from classic_keyword_list order by num'
    cur.execute(sql)
    
    conn.close()


def pull():

    #상위 10개 키워드 가져옴.
    sql = 'select keyword from classic_keyword_list limit 10'
    cur.execute(sql)
    result = cur.fetchall()
    for row in result:
        print(row)

    conn.close()

    return result

def init() :
    if nowHour == 0 :
        sql = 'SET SQL_SAFE_UPDATES =0'
        cur.execute(sql)
        sql = 'UPDATE day SET num = default'
        cur.execute(sql)
        conn.commit()
    conn.close()

init()