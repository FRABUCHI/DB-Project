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
        querys = "SELECT " + sentence1 +", "+ sentence2 + " from " + sentence3 + " where " + sentence2 + " = " + numarray[0] + " or " + sentence2 + " = " + numarray[1]
        cur.execute(querys)
        date = cur.fetchall()
        result = date[0][0] +"    "+date[0][1]+ "\n" + date[1][0] +"    "+date[1][1]

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

    #개강
    elif info == '개강':
        querys = "SELECT " + sentence1 + ", " + sentence2 + " from " + sentence3 + " where " + sentence2 + " like " + "'%" + "개강" + "%'"
        cur.execute(querys)
        date = cur.fetchall()
        result = date[0][0] + "    " + date[0][1] + "\n" + date[1][0] + "    " + date[1][1]
        conn.close()

    #수강신청
    elif info == '수강신청':
        querys = "SELECT " + sentence1 + ", " + sentence2 + " from " + sentence3 + " where " + sentence2 + " like " + "'%" + "수강신청" + "%'"
        cur.execute(querys)
        result = cur.fetchall()
        conn.close()

    #1학기 예비수강
    elif info in ('1학기','예비수강'):
        semester = '1'+'학기'
        apply = '예비수강'
        sql = 'SELECT date, info FROM ajou.haksa where (info LIKE %s and info LIKE %s)'
        arg = [semester + '%', apply + '%']
        cur.execute(sql,arg)
        result = cur.fetchall()
        conn.close()

    #2학기 예비수강
    elif info in ('2학기','예비수강'):
        semester = '2'+'학기'
        apply = '예비수강'
        sql = 'SELECT date, info FROM ajou.haksa where (info LIKE %s and info LIKE %s)'
        arg = [semester + '%', apply + '%']
        cur.execute(sql,arg)
        result = cur.fetchall()
        conn.close()

    #계절학기 예비수강
    elif info in ('계절학기','예비수강'):
        semester = '계절'+'학기'
        apply = '예비수강'
        sql = 'SELECT date, info FROM ajou.haksa where (info LIKE %s and info LIKE %s)'
        arg = [semester + '%', apply + '%']
        cur.execute(sql,arg)
        result = cur.fetchall()
        conn.close()


    #1학기 수강신청
    elif info in ('1학기','수강신청'):
        semester = '1'+'학기'
        apply = '수강신청'
        sql = 'SELECT date, info FROM ajou.haksa where (info LIKE %s and info LIKE %s)'
        arg = [semester + '%', apply + '%']
        cur.execute(sql,arg)
        result = cur.fetchall()
        conn.close()

    #2학기 수강신청
    elif info in ('2학기','수강신청'):
        semester = '2'+'학기'
        apply = '수강신청'
        sql = 'SELECT date, info FROM ajou.haksa where (info LIKE %s and info LIKE %s)'
        arg = [semester + '%', apply + '%']
        cur.execute(sql,arg)
        result = cur.fetchall()
        conn.close()

    #계절학기 수강신청
    elif info in ('계절학기','수강신청'):
        semester = '계절'+'학기'
        apply = '수강신청'
        sql = 'SELECT date, info FROM ajou.haksa where (info LIKE %s and info LIKE %s)'
        arg = [semester + '%', apply + '%']
        cur.execute(sql,arg)
        result = cur.fetchall()
        conn.close()

    #1학기 수강정정
    elif info in ('1학기','수강정정'):
        semester = '1'+'학기'
        apply = '수강정정'
        sql = 'SELECT date, info FROM ajou.haksa where (info LIKE %s and info LIKE %s)'
        arg = [semester + '%', apply + '%']
        cur.execute(sql,arg)
        result = cur.fetchall()
        conn.close()

    #2학기 수강정정
    elif info in ('2학기','수강정정'):
        semester = '2'+'학기'
        apply = '수강정정'
        sql = 'SELECT date, info FROM ajou.haksa where (info LIKE %s and info LIKE %s)'
        arg = [semester + '%', apply + '%']
        cur.execute(sql,arg)
        result = cur.fetchall()
        conn.close()

    #1학기 수강신청 포기
    elif info in ('1학기','수강신청 포기'):
        semester = '1'+'학기'
        apply = '수강신청 포기'
        sql = 'SELECT date, info FROM ajou.haksa where (info LIKE %s and info LIKE %s)'
        arg = [semester + '%', apply + '%']
        cur.execute(sql,arg)
        result = cur.fetchall()
        conn.close()

    #2학기 수강신청 포기
    elif info in ('2학기','수강신청 포기'):
        semester = '2'+'학기'
        apply = '수강신청 포기'
        sql = 'SELECT date, info FROM ajou.haksa where (info LIKE %s and info LIKE %s)'
        arg = [semester + '%', apply + '%']
        cur.execute(sql,arg)
        result = cur.fetchall()
        conn.close()

    #1학기 취득학점 포기
    elif info in ('1학기','취득학점 포기'):
        semester = '1'+'학기'
        apply = '취득학점 포기'
        sql = 'SELECT date, info FROM ajou.haksa where (info LIKE %s and info LIKE %s)'
        arg = [semester + '%', apply + '%']
        cur.execute(sql,arg)
        result = cur.fetchall()
        conn.close()

    #2학기 취득학점 포기
    elif info in ('2학기','취득학점 포기'):
        semester = '2'+'학기'
        apply = '취득학점 포기'
        sql = 'SELECT date, info FROM ajou.haksa where (info LIKE %s and info LIKE %s)'
        arg = [semester + '%', apply + '%']
        cur.execute(sql,arg)
        result = cur.fetchall()
        conn.close()


    return result