import pymysql

def haksa_db (info) :
    conn = pymysql.connect(
        host="localhost",
        user = "root",
        asswd = "1q2w3e4r",
        db = "ajou",
        charset = "utf8",
        use_unicode=True
    )

    cur = conn.cursor()
    sentence1 = 'date'
    sentence2 = 'info'
    sentence3 = 'ajou.haksa'

    if info == '방학':
        numarray = [39, 72]
        result = ''

        querys = "SELECT " + sentence1 +", "+ sentence2 + " from " + sentence3 + " where " + sentence4 + " = " + numarray[0] + " or " + sentence4 + " = " + numarray[1]
        cur.execute(querys)
        date = cur.fetchall()
        for row in date :
            result = result + str(row[0]) +"    "+str(row[1])+ "\n"

        conn.close()

    elif info == '전체학사일정':
        sentence1 = 'date'
        sentence2 = 'info'
        sentence3 = 'ajou.haksa'
        result = ''

        querys = "SELECT " + sentence1 +", "+ sentence2 + " from " + sentence3
        cur.execute(querys)
        date = cur.fetchall()
        for row in date :
            result = result + str(row[0]) +"    "+str(row[1])+ "\n"

        conn.close()

    #1학기 중간/기말/성적
    elif info == '1학기':
        semester = '1'+'학기'
        test = '시험'
        point = '성적'
        sql = 'SELECT date, info FROM ajou.haksa where (info LIKE %s and info LIKE %s) or (info LIKE %s and info LIKE %s)'
        arg = [semester + '%', test +'%', semester + '%', point + '%']
        cur.execute(sql,arg)
        result = cur.fetchall()
        conn.close()

    #2학기 중간/기말/성적            
    elif info == '2학기':
        semester = '2'+'학기'
        test = '시험'
        point = '성적'
        sql = 'SELECT date, info FROM ajou.haksa where (info LIKE %s and info LIKE %s) or (info LIKE %s and info LIKE %s)'
        arg = [semester + '%', test + '%', semester + '%', point + '%']
        cur.execute(sql,arg)
        result = cur.fetchall()
        conn.close()

    #1/2학기 전부
    elif info in ('중간','중간고사','기말','기말고사','성적','성적입력','성적정정','공고'):
        test = '시험'
        point = '성적'
        sql = 'SELECT date, info FROM ajou.haksa where info LIKE %s and info LIKE %s'
        arg = [test +'%', point + '%']
        cur.execute(sql,arg)
        result = cur.fetchall()
        conn.close()





    return result