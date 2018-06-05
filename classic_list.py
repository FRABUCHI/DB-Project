import pymysql

conn = pymysql.connect(
        host="13.209.43.217",
        user = "soyeon",
        passwd = "1q2w3e4r",
        db = "ajou",
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
    
    conne.close()


def pull():

    #상위 10개 키워드 가져옴.
    sql = 'select keyword from classic_keyword_list limit 10'
    cur.execute(sql)
    result = cur.fetchall()
    for row in result:
        print(row)

    conn.close()

    return result
