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
    #1학기 중간/기말/성적
    if info == '1학기':
        try:
	        with conn.cursor() as cur:
                sql = 'SELECT date, info FROM ajou.haksa where info LIKE '%중간시험%' or info LIKE '%기말시험%' or info like'%성적%'' 
		        cur.execute(sql)
	    	    result = cur.fetchall()
        finally:
	        conn.close()
    #2학기 중간/기말/성적            
    elif info == '2학기':
        try:
	        with conn.cursor() as cur:
                sql = 'SELECT date, info FROM ajou.haksa where info LIKE '%중간시험%' or info LIKE '%기말시험%' or info like'%성적%'' 
		        cur.execute(sql)
	    	    result = cur.fetchall()
        finally:
	        conn.close()

    #1/2학기 전부
    elif info in ('중간','중간고사','기말','기말고사','성적','성적입력','성적정정','공고'):
        try:
	        with conn.cursor() as cur:
                sql = 'SELECT date, info FROM ajou.haksa where info LIKE '%시험%' or info like'%성적%'' 
		        cur.execute(sql)
	    	    result = cur.fetchall()
        finally:
	        conn.close()

    return result