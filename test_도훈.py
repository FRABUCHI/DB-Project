

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

sentence1 = 'date'
sentence2 = 'info'
sentence3 = 'ajou.haksa'

print('hello')
info = '수강정정'
#info = '1학기'
#밑에 있는 식으로 하면 
# ('\n2017.12.27(수)~2018.1.3(수)', '\n\n복학생 전과신청\n')
#이런식으로 결과값 나와요
#참고해서 코딩하고 결과값 원하는대로 나오는지 확인해주세요.
#이쁘게 결과값 나오게 다듬는거는 나중에 추합한후에 
#카톡에서 테스트 하고 수정할게요.

# 개강
if info == '개강':
    querys = "SELECT " + sentence1 + ", " + sentence2 + " from " + sentence3 + " where " + sentence2 + " like " + "'%" + "개강" + "%'"
    cur.execute(querys)
    result = cur.fetchall()
    print('개강')
    for row in result:
        print(row)

# 예비수강
if info == '예비수강':
    querys = "SELECT " + sentence1 + ", " + sentence2 + " from " + sentence3 + " where " + sentence2 + " like " + "'%" + "책가방식" + "%'"
    cur.execute(querys)
    result = cur.fetchall()
    print('예비수강')
    for row in result:
        print(row)

# 수강신청
if info == '수강신청':
    querys = "SELECT " + sentence1 + ", " + sentence2 + " from " + sentence3 + " where " + sentence2 + " like " + "'%" + "수강신청" + "%'"
    cur.execute(querys)
    result = cur.fetchall()
    print('수강신청')
    for row in result:
        print(row)

# 수강정정
if info == '수강정정':
    querys = "SELECT " + sentence1 + ", " + sentence2 + " from " + sentence3 + " where " + sentence2 + " like " + "'%" + "수강정정" + "%'"
    cur.execute(querys)
    result = cur.fetchall()
    print('수강정정')
    for row in result:
        print(row)

# 수강신청포기
if info == '수강신청포기':
    querys = "SELECT " + sentence1 + ", " + sentence2 + " from " + sentence3 + " where " + sentence2 + " like " + "'%" + "수강신청포기" + "%'"
    cur.execute(querys)
    result = cur.fetchall()
    print('수강신청포기')
    for row in result:
        print(row)

# 취득학점포기
if info == '취득학점포기':
    querys = "SELECT " + sentence1 + ", " + sentence2 + " from " + sentence3 + " where " + sentence2 + " like " + "'%" + "취득학점포기" + "%'"
    cur.execute(querys)
    result = cur.fetchall()
    print('취득학점포기')
    for row in result:
        print(row)

# 계절학기
if info == '계절학기':
    querys = "SELECT " + sentence1 + ", " + sentence2 + " from " + sentence3 + " where " + sentence2 + " like " + "'%" + "계절학기" + "%'"
    cur.execute(querys)
    result = cur.fetchall()
    print('계절학기')
    for row in result:
        print(row)

#전체 학사 일정
if info == '전체':
    sql = "select date, info from haksa"
    cur.execute(sql)
    result = cur.fetchall()
    print('전체 학사 일정')
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

elif info in ('중간', '중간고사', '기말', '기말고사', '성적', '성적입력', '성적정정', '공고'):
    sql = '''
    '''
    cur.execute(sql)
    result = cur.fetchall()
    print('아주봇으로 입력받을때')
    for row in result:
        print(row)

print("end")		
conn.close()