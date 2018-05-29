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

    #개강
    if info == '개강':
        querys = "SELECT " + sentence1 + ", " + sentence2 + " from " + sentence3 + " where " + sentence2 + " like " + "'%" + "개강" + "%'"
        cur.execute(querys)
        result = cur.fetchall()
        conn.close()

    #예비수강
    elif info == '예비수강':
        querys = "SELECT " + sentence1 + ", " + sentence2 + " from " + sentence3 + " where " + sentence2 + " like " + "'%" + "책가방식" + "%'"
        cur.execute(querys)
        result = cur.fetchall()
        conn.close()

    #수강신청
    elif info == '수강신청':
        querys = "SELECT " + sentence1 + ", " + sentence2 + " from " + sentence3 + " where " + sentence2 + " like " + "'%" + "수강신청" + "%'"
        cur.execute(querys)
        result = cur.fetchall()
        conn.close()

    #수강정정
    elif info == '수강정정':
        querys = "SELECT " + sentence1 + ", " + sentence2 + " from " + sentence3 + " where " + sentence2 + " like " + "'%" + "수강정정" + "%'"
        cur.execute(querys)
        result = cur.fetchall()
        conn.close()

    #수강신청 포기
    elif info == '수강신청 포기':
        querys = "SELECT " + sentence1 + ", " + sentence2 + " from " + sentence3 + " where " + sentence2 + " like " + "'%" + "수강신청포기" + "%'"
        cur.execute(querys)
        result = cur.fetchall()
        conn.close()

    #취득학점 포기
    elif info == '취득학점 포기':
        querys = "SELECT " + sentence1 + ", " + sentence2 + " from " + sentence3 + " where " + sentence2 + " like " + "'%" + "취득학점포기" + "%'"
        cur.execute(querys)
        result = cur.fetchall()
        conn.close()

    #계절학기
    elif info == '계절학기':
        querys = "SELECT " + sentence1 + ", " + sentence2 + " from " + sentence3 + " where " + sentence2 + " like " + "'%" + "계절" + "%'"
        cur.execute(querys)
        result = cur.fetchall()
        conn.close()


    return result