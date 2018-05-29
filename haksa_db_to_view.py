
#########수정 하지 마세요######################

import pymysql

def haksa_db (info) :
    conn = pymysql.connect(
        host="13.209.7.120",
        user = "ubuntu",
        asswd = "1q2w3e4r",
        db = "ajou",
        charset = "utf8",
        use_unicode=True
    )

    cur = conn.cursor()
  
    #방학
    if info == '방학':
        conn.close()

    #1학기 중간/기말/성적
    elif info == '1학기':
        conn.close()

    #2학기 중간/기말/성적            
    elif info == '2학기':
        conn.close()

    #1/2학기 전부
    elif info in ('중간','중간고사','기말','기말고사','성적','성적입력','성적정정','공고'):
        conn.close()

    #전체 학사 일정
    elif info in ('일정')

    return result