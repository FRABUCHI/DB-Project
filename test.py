import pymysql
  
print(haksa_db('1학기'))
    
def haksa_db (info) :
    conn = pymysql.connect(
        host="13.209.43.217",
        user = "soyeon",
        passwd = "1q2w3e4r",
        db = "ajou",
        charset = "utf8",
        use_unicode=True
    )

    cur = conn.cursor()
  
    sentence1 = 'date'
    sentence2 = 'info'
    sentence3 = 'ajou.haksa'
    sentence4 = 'idhaksa'

    #전체 학사 일정
    if info in ('전체','전체학사일정','학사력'):
        sql = "select date, info from haksa"
        cur.execute(sql)
        result = cur.fetchall()


    #########################################################################################3
    #1학기 중간/기말/성적  
    elif info == '1학기':
        sql = '''
        SELECT date, info 
        FROM haksa 
        where (info LIKE '%1학기%' and info LIKE '%시험%') or (info LIKE '%1학기%' and info LIKE '%성적%')
        '''
        cur.execute(sql)
        result = cur.fetchall()
        
    #2학기 중간/기말/성적  
    elif info == '2학기':
        sql = '''
        SELECT date, info 
        FROM haksa 
        where (info LIKE '%2학기%' and info LIKE '%시험%') or (info LIKE '%2학기%' and info LIKE '%성적%')
        '''
        cur.execute(sql)
        result = cur.fetchall()

    #1학기/2학기 중간/기말/성적
    elif info in ('중간','중간고사','기말','기말고사','성적','성적입력','성적정정','공고'):
        sql = '''
        SELECT date, info 
        FROM haksa 
        where (info LIKE '%1학기%' and info LIKE '%시험%') or (info LIKE '%1학기%' and info LIKE '%성적%') or (info LIKE '%2학기%' and info LIKE '%시험%') or (info LIKE '%2학기%' and info LIKE '%성적%')
        '''
        cur.execute(sql)
        result = cur.fetchall()
    
    #########################################################################################3
    # 개강
    if info == '개강':
        querys = \
            "SELECT " + sentence1 + ", " + sentence2 + \
            " FROM " + sentence3 + \
            " WHERE " + sentence2 + " like " + "'%" + "개강" + "%'"

        cur.execute(querys)
        result = cur.fetchall()

    #########################################################################################3
    # 예비수강
    if info == '예비수강':
        querys = \
            "SELECT " + sentence1 + ", " + sentence2 + \
            " FROM " + sentence3 + \
            " WHERE " + sentence2 + " like " + "'%" + "책가방식" + "%'"

        cur.execute(querys)
        result = cur.fetchall()

    # 수강신청
    if info == '수강신청':
        querys = \
            "SELECT " + sentence1 + ", " + sentence2 + \
            " FROM " + sentence3 + \
            " WHERE " + sentence2 + \
            " like " + "'%" + "수강신청" + "%'" + \
            " and " + " not info like " + "'%" + "포기" + "%'" + \
            " and " + " not info like " + "'%" + "예비" + "%'"

        cur.execute(querys)
        result = cur.fetchall()

    # 수강정정
    if info == '수강정정':
        querys = \
            "SELECT " + sentence1 + ", " + sentence2 + \
            " FROM " + sentence3 + \
            " WHERE " + sentence2 + " like " + "'%" + "수강정정" + "%'"

        cur.execute(querys)
        result = cur.fetchall()

    # 수강신청포기
    if info == '수강신청 포기':
        querys = \
            "SELECT " + sentence1 + ", " + sentence2 + \
            " FROM " + sentence3 + \
            " WHERE " + sentence2 + " like " + "'%" + "수강신청포기" + "%'"

        cur.execute(querys)
        result = cur.fetchall()

    # 취득학점포기
    if info == '취득학점 포기':
        querys = \
            "SELECT " + sentence1 + ", " + sentence2 + \
            " FROM " + sentence3 + \
            " WHERE " + sentence2 + " like " + "'%" + "취득학점포기" + "%'"

        cur.execute(querys)
        result = cur.fetchall()

########################################################################################################
    #방학관련 일정 
    elif info == '방학':
        querys = \
            "SELECT " + sentence1 + ", " + sentence2 + \
            " from " + sentence3 + \
            " where " + sentence2 + " LIKE " + "'%" + "방학" + "%'"
        cur.execute(querys)
        result = cur.fetchall()

    #방학관련 일정 
    elif info == '여름방학':
        querys = \
            "SELECT " + sentence1 + ", " + sentence2 + \
            " from " + sentence3 + \
            " where " + sentence2 + " LIKE " + "'%" + "방학" + "%'" + \
            " and " + " not info like " + "'%" + "동계" + "%'"

        cur.execute(querys)
        result = cur.fetchall()


    #방학관련 일정 
    elif info == '겨울방학':
        querys = \
            "SELECT " + sentence1 + ", " + sentence2 + \
            " from " + sentence3 + \
            " where " + sentence2 + " LIKE " + "'%" + "날" + "%'" + \
            " and " + " not info like " + "'%" + "하계" + "%'"

        cur.execute(querys)
        result = cur.fetchall()

########################################################################################################
    #휴일관련 일정 
    elif info in ('휴일', '공휴일', '쉬는날'):
        querys = \
            "SELECT " + sentence1 + ", " + sentence2 + \
            " from " + sentence3 + \
            " where " + sentence2 + " LIKE " + "'%" + "날" + "%'" + \
            " UNION ALL " + \
            "SELECT " + sentence1 + ", " + sentence2 + \
            " from " + sentence3 + \
            " where " + sentence2 + " LIKE " + "'%" + "절" + "%'" + \
            " and " + " not info like " + "'%" + "계절" + "%'" + \
            " UNION ALL " + \
            "SELECT " + sentence1 + ", " + sentence2 + \
            " from " + sentence3 + \
            " where " + sentence2 + " LIKE " + "'%" + "일" + "%'" + \
            " and " + " not info like " + "'%" + "수업" + "%'" + \
            " and " + " not info like " + "'%" + "일절" + "%'" + \
            " and " + " not info like " + "'%" + "보강" + "%'" + \
            " and " + " not info like " + "'%" + "학위" + "%'" + \
            " UNION ALL " + \
            "SELECT " + sentence1 + ", " + sentence2 + \
            " from " + sentence3 + \
            " where " + sentence2 + " LIKE " + "'%" + "연휴" + "%'" + \
            " UNION ALL " + \
            "SELECT " + sentence1 + ", " + sentence2 + \
            " from " + sentence3 + \
            " where " + sentence2 + " LIKE " + "'%" + "선거" + "%'"

        cur.execute(querys)
        result = cur.fetchall()

########################################################################################################
    #행정관련 일정
    elif info in('전과', '전과신청', '전과 신청'):
        querys = \
            "SELECT " + sentence1 + ", " + sentence2 + \
            " from " + sentence3 + \
            " where " + sentence2 + " LIKE " + "'%" + "전과" + "%'"
        cur.execute(querys)
        result = cur.fetchall()

    #행정관련 일정
    elif info in('학기등록', '등록', '학기 등록'):
        querys = \
            "SELECT " + sentence1 + ", " + sentence2 + \
            " from " + sentence3 + \
            " where " + sentence2 + " LIKE " + "'%" + "등록" + "%'"
        cur.execute(querys)
        result = cur.fetchall()

    #행정관련 일정
    elif info in('전공/졸업 신청', '졸업유예', '졸업연기', '졸업 유예', '졸업 연기', '전공 변경', '전공 취소', '복수전공', '부전공', '연계전공'):
        querys = \
            "SELECT " + sentence1 + ", " + sentence2 + \
            " from " + sentence3 + \
            " where " + sentence2 + " LIKE " + "'%" + "졸업" + "%'"
        cur.execute(querys)
        result = cur.fetchall()

########################################################################################################
    #입학/졸업 관련 일정
    elif info in ('입학식','입학식(신·편입)'):
        querys = \
            "SELECT " + sentence1 + ", " + sentence2 + \
            " from " + sentence3 + \
            " where (" + sentence2 + " LIKE '%" + "입학식" + "%') or (" + sentence2 + " LIKE '%" + "오리엔테이션" + "%')"

        cur.execute(querys)
        result = cur.fetchall()

    #입학/졸업 관련 일정
    elif info in ('졸업식','졸업식(학위 수여식)'):
        querys = \
            "SELECT " + sentence1 + ", " + sentence2 + \
            " from " + sentence3 + \
            " where " + sentence2 + " LIKE " + "'%" + "학위" + "%'"
        
        cur.execute(querys)
        result = cur.fetchall()

    conn.close()

    return result
