

#이 파일은 view.py가 아니라 haksa_db_to_view.py 테스트용 입니다.
#info로 값이 들어오고 if문으로 들어갈 때 
# 서로 안 겹치도록 다른 사람이 어떻게 짤지 조금 주의해서 코딩해주세요.
# 짜기 전에 views.py 형식 다 지정해 놨으니까 한번 확인해보세요.
# view.py 참고해서 짜면 코드 덜 겹칠꺼에요.

import pymysql

conn = pymysql.connect(
    host="localhost",
    user = "root",
    passwd = "1q2w3e4r",
    db = "ajou",
    charset = "utf8",
    use_unicode=True
)



cur = conn.cursor()

print('hello')

info = '전체'
#info = '1학기'

#밑에 있는 식으로 하면 
# ('\n2017.12.27(수)~2018.1.3(수)', '\n\n복학생 전과신청\n')
#이런식으로 결과값 나와요
#참고해서 코딩하고 결과값 원하는대로 나오는지 확인해주세요.
#이쁘게 결과값 나오게 다듬는거는 나중에 추합한후에 
#카톡에서 테스트 하고 수정할게요.


sentence1 = 'date'
sentence2 = 'info'
sentence3 = 'ajou.haksa'
sentence4 = 'idhaksa'
numarray = [39,72]
vacationarray = [14,21,24,25,26,31,33,56,58,59,70]

#전체 학사 일정
if info == '전체':
    sql = "select date, info from haksa"
    cur.execute(sql)
    result = cur.fetchall()
    print('전체 학사 일정')
    for row in result:
        print(row)

#방학관련 일정 
elif info == '방학':
    querys = "SELECT " + sentence1 +", "+ sentence2 + " from " + sentence3 + "where " + sentence4 + "= " + numarray[0] + "or " + sentence4 + "= " + numarray[1]
    cur.execute(querys)
    result = cur.fetchall()
    print('방학') 
    for row in result: 
        print(row)

#방학관련 일정 
elif info == '여름방학':
    querys = "SELECT " + sentence1 +", "+ sentence2 + " from " + sentence3 + "where " + sentence4 + "= " + numarray[0]
    cur.execute(querys)
    result = cur.fetchall()
    print('여름방학') 
    for row in result: 
        print(row)


#방학관련 일정 
elif info == '겨울방학':
    querys = "SELECT " + sentence1 +", "+ sentence2 + " from " + sentence3 + "where " + sentence4 + "= " + numarray[1]
    cur.execute(querys)
    result = cur.fetchall()
    print('겨울방학') 
    for row in result: 
        print(row)

#휴일관련 일정 
elif info in ('휴일','공휴일','쉬는날'):
    querys = "SELECT " + sentence1 +", "+ sentence2 + " from " + sentence3 + "where " + sentence4 + "= " + vacationarray[0] + "or " + sentence4 + "= " + vacationarray[1] + "or " + sentence4 + "= " + vacationarray[2] + "or " + sentence4 + "= " + vacationarray[3] + "or " + sentence4 + "= " + vacationarray[4] + "or " + sentence4 + "= " + vacationarray[5] + "or " + sentence4 + "= " + vacationarray[6] + "or " + sentence4 + "= " + vacationarray[7] + "or " + sentence4 + "= " + vacationarray[8] + "or " + sentence4 + "= " + vacationarray[9] + "or " + sentence4 + "= " + vacationarray[10]
    cur.execute(querys)
    result = cur.fetchall()
    print('휴일') 
    for row in result: 
        print(row)

#행정관련 일정
elif info in('전과','전과신청','전과 신청'):
    querys = "SELECT " + sentence1 +", "+ sentence2 + " from " + sentence3 + "where " + sentence2 + "LIKE " + "'%" + "전과" + "%'"
    cur.execute(querys)
    result = cur.fetchall()
    print('전과') 
    for row in result: 
        print(row)

#행정관련 일정
elif info in('학기등록','등록','학기 등록'):

    querys = "SELECT " + sentence1 +", "+ sentence2 + " from " + sentence3 + "where " + sentence2 + "LIKE " + "'%" + "등록" + "%'"
    cur.execute(querys)
    result = cur.fetchall()
    print('등록') 
    for row in result: 
        print(row)

#행정관련 일정
elif info in('전공/졸업 신청','졸업유예','졸업연기','졸업 유예','졸업 연기','전공 변경','전공 취소','복수전공','부전공','연계전공'):
    querys = "SELECT " + sentence1 +", "+ sentence2 + " from " + sentence3 + "where " + sentence2 + "LIKE " + "'%" + "졸업" + "%'"
    cur.execute(querys)
    result = cur.fetchall()
    print('전공') 
    for row in result: 
        print(row)

#입학/졸업 관련 일정
elif info == '입학식':
    querys = "SELECT " + sentence1 +", "+ sentence2 + " from " + sentence3 + "where (" + sentence2 + " LIKE '%" + "입학식" + "%') or (" + sentence2 + " LIKE '%" + "오리엔테이션" + "%')"
    cur.execute(querys)
    result = cur.fetchall()
    print('입학식') 
    for row in result: 
        print(row)

#입학/졸업 관련 일정
elif info == '졸업식':
    querys = "SELECT " + sentence1 +", "+ sentence2 + " from " + sentence3 + "where " + sentence2 + "LIKE " + "'%" + "학위" + "%'"
    cur.execute(querys)
    result = cur.fetchall()
    print('졸업식') 
    for row in result: 
        print(row)

#1학기 중간/기말/성적  
elif info == '1학기':
    sql = '''
    SELECT date, info 
    FROM haksa 
    where (info LIKE '%1학기%' and info LIKE '%시험%') or (info LIKE '%1학기%' and info LIKE '%성적%')
    '''
    cur.execute(sql)
    result = cur.fetchall()
    print('1학기 중간/기말/성적')
    for row in result:
        print(row)

elif info in ('중간','중간고사','기말','기말고사','성적','성적입력','성적정정','공고'):
    sql = '''
    '''
    cur.execute(sql)
    result = cur.fetchall()
    print('아주봇으로 입력받을때')
    for row in result:
        print(row)


print("end")        
conn.close()
