

#이 파일은 view.py가 아니라 haksa_db_to_view.py 테스트용 입니다.
#info로 값이 들어오고 if문으로 들어갈 때 
# 서로 안 겹치도록 다른 사람이 어떻게 짤지 조금 주의해서 코딩해주세요.
# 짜기 전에 views.py 형식 다 지정해 놨으니까 한번 확인해보세요.
# view.py 참고해서 짜면 코드 덜 겹칠꺼에요.

import pymysql

conn = pymysql.connect(
    host="localhost",
    user = "root",
    passwd = "alffpsldja1!",
    db = "ajou",
    charset = "utf8",
    use_unicode=True
)

cur = conn.cursor()

print('hello')

info = '광고 '
#info = '1학기'

sentence1 = 'date'
sentence2 = 'info'
sentence3 = 'ajou.haksa'
sentence4 = 'idhaksa'

sentence5 = 'club_univ'
sentence6 = 'club_name'
sentence7 = 'club_category'
sentence8 = 'club_major'
sentence9 = 'ajou.club'

# 동아리 전체
if info == '동아리':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9

        cur.execute(querys)
        result = cur.fetchall()
        print('동아리')
        for row in result:
            print(row)

# 중앙동아리 전체
if info == '중앙동아리 전체':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('중앙동아리')
        for row in result:
            print(row)

# 중앙동아리 관심사 별 분류

if info == 'MIDI ':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
            " AND " + sentence7 + " like " + "'%" + "MIDI" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('MIDI')
        for row in result:
            print(row)

if info == '검도 ':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
            " AND " + sentence7 + " like " + "'%" + "검도" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('검도')
        for row in result:
            print(row)

if info == '광고 ':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
            " AND " + sentence7 + " like " + "'%" + "광고" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('광고')
        for row in result:
            print(row)

if info == '권투 ':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
            " AND " + sentence7 + " like " + "'%" + "권투" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('권투')
        for row in result:
            print(row)

if info == '기타 ':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
            " AND " + sentence7 + " like " + "'%" + "기타" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('기타')
        for row in result:
            print(row)

if info == '농구 ':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
            " AND " + sentence7 + " like " + "'%" + "농구" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('농구')
        for row in result:
            print(row)

if info == '등산 ':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
            " AND " + sentence7 + " like " + "'%" + "등산" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('등산')
        for row in result:
            print(row)

if info == '로봇 ':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
            " AND " + sentence7 + " like " + "'%" + "로봇" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('로봇')
        for row in result:
            print(row)

if info == '록 ':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
            " AND " + sentence7 + " like " + "'%" + "록" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('록')
        for row in result:
            print(row)

if info == '미술 ':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
            " AND " + sentence7 + " like " + "'%" + "미술" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('미술')
        for row in result:
            print(row)

if info == '바둑 ':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
            " AND " + sentence7 + " like " + "'%" + "바둑" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('바둑')
        for row in result:
            print(row)

if info == '발명 ':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
            " AND " + sentence7 + " like " + "'%" + "발명" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('발명')
        for row in result:
            print(row)

if info == '발표 ':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
            " AND " + sentence7 + " like " + "'%" + "발표" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('발표')
        for row in result:
            print(row)

if info == '배드민턴 ':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
            " AND " + sentence7 + " like " + "'%" + "배드민턴" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('배드민턴')
        for row in result:
            print(row)

if info == '볼링 ':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
            " AND " + sentence7 + " like " + "'%" + "볼링" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('볼링')
        for row in result:
            print(row)

if info == '봉사 ':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
            " AND " + sentence7 + " like " + "'%" + "봉사" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('봉사')
        for row in result:
            print(row)

if info == '사진 ':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
            " AND " + sentence7 + " like " + "'%" + "사진" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('사진')
        for row in result:
            print(row)

if info == '서예 ':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
            " AND " + sentence7 + " like " + "'%" + "서예" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('서예')
        for row in result:
            print(row)

if info == '스노우보드 ':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
            " AND " + sentence7 + " like " + "'%" + "스노우보드" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('스노우보드')
        for row in result:
            print(row)

if info == '스쿼시 ':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
            " AND " + sentence7 + " like " + "'%" + "스쿼시" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('스쿼시')
        for row in result:
            print(row)

if info == '시사 ':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
            " AND " + sentence7 + " like " + "'%" + "시사" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('시사')
        for row in result:
            print(row)

if info == '실용음악 ':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
            " AND " + sentence7 + " like " + "'%" + "실용음악" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('실용음악')
        for row in result:
            print(row)

if info == '야구 ':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
            " AND " + sentence7 + " like " + "'%" + "야구" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('야구')
        for row in result:
            print(row)

if info == '야학 ':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
            " AND " + sentence7 + " like " + "'%" + "야학" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('야학')
        for row in result:
            print(row)

if info == '연극 ':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
            " AND " + sentence7 + " like " + "'%" + "연극" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('연극')
        for row in result:
            print(row)

if info == '영상 ':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
            " AND " + sentence7 + " like " + "'%" + "영상" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('영상')
        for row in result:
            print(row)

if info == '영어 ':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
            " AND " + sentence7 + " like " + "'%" + "영어" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('영어')
        for row in result:
            print(row)

if info == '영화 ':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
            " AND " + sentence7 + " like " + "'%" + "영화" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('영화')
        for row in result:
            print(row)

if info == '유도 ':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
            " AND " + sentence7 + " like " + "'%" + "유도" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('유도')
        for row in result:
            print(row)

if info == '음악 ':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
            " AND " + sentence7 + " like " + "'%" + "음악" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('음악')
        for row in result:
            print(row)

if info == '자전거 ':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
            " AND " + sentence7 + " like " + "'%" + "자전거" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('자전거')
        for row in result:
            print(row)

if info == '종교 ':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
            " AND " + sentence7 + " like " + "'%" + "종교" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('종교')
        for row in result:
            print(row)

if info == '천문 ':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
            " AND " + sentence7 + " like " + "'%" + "천문" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('천문')
        for row in result:
            print(row)

if info == '축구 ':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
            " AND " + sentence7 + " like " + "'%" + "축구" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('축구')
        for row in result:
            print(row)

if info == '컴퓨터 ':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
            " AND " + sentence7 + " like " + "'%" + "컴퓨터" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('컴퓨터')
        for row in result:
            print(row)

if info == '탁구 ':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
            " AND " + sentence7 + " like " + "'%" + "탁구" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('탁구')
        for row in result:
            print(row)

if info == '태권도 ':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
            " AND " + sentence7 + " like " + "'%" + "태권도" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('태권도')
        for row in result:
            print(row)

if info == '테니스 ':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
            " AND " + sentence7 + " like " + "'%" + "테니스" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('테니스')
        for row in result:
            print(row)

if info == '패러글라이딩 ':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
            " AND " + sentence7 + " like " + "'%" + "패러글라이딩" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('패러글라이딩')
        for row in result:
            print(row)

if info == '풍물 ':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
            " AND " + sentence7 + " like " + "'%" + "풍물" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('풍물')
        for row in result:
            print(row)

if info == '합창 ':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
            " AND " + sentence7 + " like " + "'%" + "합창" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('합창')
        for row in result:
            print(row)

if info == '흑인음악 ':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
            " AND " + sentence7 + " like " + "'%" + "흑인음악" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('흑인음악')
        for row in result:
            print(row)

if info == '힙합 ':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence5 + " like " + "'%" + "중앙동아리" + "%'" + \
            " AND " + sentence7 + " like " + "'%" + "힙합" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('힙합')
        for row in result:
            print(row)


# 소학회
if info == '소학회':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence7 + " like " + "'%" + "소학회" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('소학회')
        for row in result:
            print(row)

# 각 학과별 검색
if info == 'e-비즈니스 학과':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence8 + " like " + "'%" + "e-비즈니스 학과" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('e-비즈니스 학과')
        for row in result:
            print(row)

if info == '건설시스템공학과':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence8 + " like " + "'%" + "건설시스템공학과" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('건설시스템공학과')
        for row in result:
            print(row)

if info == '건축학과':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence8 + " like " + "'%" + "건축학과" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('건축학과')
        for row in result:
            print(row)

if info == '경영학과':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence8 + " like " + "'%" + "경영학과" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('경영학과')
        for row in result:
            print(row)

if info == '경제학과':
    querys = \
        "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
        " FROM " + sentence9 + \
        " WHERE " + sentence8 + " like " + "'%" + "경제학과" + "%'"

    cur.execute(querys)
    result = cur.fetchall()
    print('경제학과')
    for row in result:
        print(row)

if info == '교통시스템공학과':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence8 + " like " + "'%" + "교통시스템공학과" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('교통시스템공학과')
        for row in result:
            print(row)

if info == '국어국문학과':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence8 + " like " + "'%" + "국어국문학과" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('국어국문학과')
        for row in result:
            print(row)

if info == '금융공학과':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence8 + " like " + "'%" + "금융공학과" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('금융공학과')
        for row in result:
            print(row)

if info == '기계공학과':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence8 + " like " + "'%" + "기계공학과" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('기계공학과')
        for row in result:
            print(row)

if info == '문화컨텐츠학과':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence8 + " like " + "'%" + "문화컨텐츠학과" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('문화컨텐츠학과')
        for row in result:
            print(row)

if info == '물리학과':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence8 + " like " + "'%" + "물리학과" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('물리학과')
        for row in result:
            print(row)

if info == '미디어학과':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence8 + " like " + "'%" + "미디어학과" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('미디어학과')
        for row in result:
            print(row)

if info == '불어불문학과':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence8 + " like " + "'%" + "불어불문학과" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('불어불문학과')
        for row in result:
            print(row)

if info == '사이버보안학과':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence8 + " like " + "'%" + "사이버보안학과" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('사이버보안학과')
        for row in result:
            print(row)

if info == '사학과':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence8 + " like " + "'%" + "사학과" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('사학과')
        for row in result:
            print(row)

if info == '사회학과':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence8 + " like " + "'%" + "사회학과" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('사회학과')
        for row in result:
            print(row)

if info == '산업공학과':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence8 + " like " + "'%" + "산업공학과" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('산업공학과')
        for row in result:
            print(row)

if info == '생명과학과':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence8 + " like " + "'%" + "생명과학과" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('생명과학과')
        for row in result:
            print(row)

if info == '소프트웨어학과':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence8 + " like " + "'%" + "소프트웨어학과" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('소프트웨어학과')
        for row in result:
            print(row)

if info == '수학과':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence8 + " like " + "'%" + "수학과" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('수학과')
        for row in result:
            print(row)

if info == '스포츠레저학과':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence8 + " like " + "'%" + "스포츠레저학과" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('스포츠레저학과')
        for row in result:
            print(row)

if info == '신소재공학과':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence8 + " like " + "'%" + "신소재공학과" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('신소재공학과')
        for row in result:
            print(row)

if info == '심리학과':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence8 + " like " + "'%" + "심리학과" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('심리학과')
        for row in result:
            print(row)

if info == '영어영문학과':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence8 + " like " + "'%" + "영어영문학과" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('영어영문학과')
        for row in result:
            print(row)

if info == '응용화학생명공학과':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence8 + " like " + "'%" + "응용화학생명공학과" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('응용화학생명공학과')
        for row in result:
            print(row)

if info == '전자공학과':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence8 + " like " + "'%" + "전자공학과" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('전자공학과')
        for row in result:
            print(row)

if info == '정치외교학과':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence8 + " like " + "'%" + "정치외교학과" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('정치외교학과')
        for row in result:
            print(row)

if info == '행정학과':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence8 + " like " + "'%" + "행정학과" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('행정학과')
        for row in result:
            print(row)

if info == '화학공학과':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence8 + " like " + "'%" + "화학공학과" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('화학공학과')
        for row in result:
            print(row)

if info == '화학과':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence8 + " like " + "'%" + "화학과" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('화학과')
        for row in result:
            print(row)

if info == '환경안전공학과':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence8 + " like " + "'%" + "환경안전공학과" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('환경안전공학과')
        for row in result:
            print(row)

# 각 대학별 분류

if info == '간호대학':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence5 + " like " + "'%" + "간호대학" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('간호대학')
        for row in result:
            print(row)

if info == '경영대학':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence5 + " like " + "'%" + "경영대학" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('경영대학')
        for row in result:
            print(row)

if info == '공과대학':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence5 + " like " + "'%" + "공과대학" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('공과대학')
        for row in result:
            print(row)

if info == '국제학부':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence5 + " like " + "'%" + "국제학부" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('국제학부')
        for row in result:
            print(row)

if info == '사회과학대학':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence5 + " like " + "'%" + "사회과학대학" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('사회과학대학')
        for row in result:
            print(row)

if info == '약학대학':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence5 + " like " + "'%" + "약학대학" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('약학대학')
        for row in result:
            print(row)

if info == '의과대학':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence5 + " like " + "'%" + "의과대학" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('의과대학')
        for row in result:
            print(row)

if info == '인문대학':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence5 + " like " + "'%" + "인문대학" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('인문대학')
        for row in result:
            print(row)

if info == '자연과학대학':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence5 + " like " + "'%" + "자연과학대학" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('자연과학대학')
        for row in result:
            print(row)

if info == '정보통신대학':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence5 + " like " + "'%" + "정보통신대학" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('정보통신대학')
        for row in result:
            print(row)

# 각 동아리 관심사 별 분류

if info == 'MIDI':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence7 + " like " + "'%" + "MIDI" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('MIDI')
        for row in result:
            print(row)

if info == '검도':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence7 + " like " + "'%" + "검도" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('검도')
        for row in result:
            print(row)

if info == '게임개발':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence7 + " like " + "'%" + "게임개발" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('게임개발')
        for row in result:
            print(row)

if info == '경제':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence7 + " like " + "'%" + "경제" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('경제')
        for row in result:
            print(row)

if info == '공연':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence7 + " like " + "'%" + "공연" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('공연')
        for row in result:
            print(row)

if info == '광고':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence7 + " like " + "'%" + "광고" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('광고')
        for row in result:
            print(row)

if info == '권투':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence7 + " like " + "'%" + "권투" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('권투')
        for row in result:
            print(row)

if info == '기타':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence7 + " like " + "'%" + "기타" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('기타')
        for row in result:
            print(row)

if info == '농구':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence7 + " like " + "'%" + "농구" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('농구')
        for row in result:
            print(row)

if info == '독서토론':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence7 + " like " + "'%" + "독서토론" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('독서토론')
        for row in result:
            print(row)

if info == '등산':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence7 + " like " + "'%" + "등산" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('등산')
        for row in result:
            print(row)

if info == '로봇':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence7 + " like " + "'%" + "로봇" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('로봇')
        for row in result:
            print(row)

if info == '록':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence7 + " like " + "'%" + "록" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('록')
        for row in result:
            print(row)

if info == '만화':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence7 + " like " + "'%" + "만화" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('만화')
        for row in result:
            print(row)

if info == '문예창작':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence7 + " like " + "'%" + "문예창작" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('문예창작')
        for row in result:
            print(row)

if info == '미술':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence7 + " like " + "'%" + "미술" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('미술')
        for row in result:
            print(row)

if info == '바둑':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence7 + " like " + "'%" + "바둑" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('바둑')
        for row in result:
            print(row)

if info == '발명':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence7 + " like " + "'%" + "발명" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('발명')
        for row in result:
            print(row)

if info == '발표':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence7 + " like " + "'%" + "발표" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('발표')
        for row in result:
            print(row)

if info == '배드민턴':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence7 + " like " + "'%" + "배드민턴" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('배드민턴')
        for row in result:
            print(row)

if info == '볼링':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence7 + " like " + "'%" + "볼링" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('볼링')
        for row in result:
            print(row)

if info == '봉사':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence7 + " like " + "'%" + "봉사" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('봉사')
        for row in result:
            print(row)

if info == '분자생물학':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence7 + " like " + "'%" + "분자생물학" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('분자생물학')
        for row in result:
            print(row)

if info == '사물놀이':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence7 + " like " + "'%" + "사물놀이" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('사물놀이')
        for row in result:
            print(row)

if info == '사진':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence7 + " like " + "'%" + "사진" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('사진')
        for row in result:
            print(row)

if info == '사회과학':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence7 + " like " + "'%" + "사회과학" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('사회과학')
        for row in result:
            print(row)

if info == '서예':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence7 + " like " + "'%" + "서예" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('서예')
        for row in result:
            print(row)

if info == '수화':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence7 + " like " + "'%" + "수화" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('수화')
        for row in result:
            print(row)

if info == '스노우보드':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence7 + " like " + "'%" + "스노우보드" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('스노우보드')
        for row in result:
            print(row)

if info == '스쿼시':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence7 + " like " + "'%" + "스쿼시" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('스쿼시')
        for row in result:
            print(row)

if info == '시사':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence7 + " like " + "'%" + "시사" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('시사')
        for row in result:
            print(row)

if info == '실용음악':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence7 + " like " + "'%" + "실용음악" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('실용음악')
        for row in result:
            print(row)

if info == '야구':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence7 + " like " + "'%" + "야구" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('야구')
        for row in result:
            print(row)

if info == '야학':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence7 + " like " + "'%" + "야학" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('야학')
        for row in result:
            print(row)

if info == '연극':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence7 + " like " + "'%" + "연극" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('연극')
        for row in result:
            print(row)

if info == '영상':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence7 + " like " + "'%" + "영상" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('영상')
        for row in result:
            print(row)

if info == '영어':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence7 + " like " + "'%" + "영어" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('영어')
        for row in result:
            print(row)

if info == '영화':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence7 + " like " + "'%" + "영화" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('영화')
        for row in result:
            print(row)

if info == '오케스트라':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence7 + " like " + "'%" + "오케스트라" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('오케스트라')
        for row in result:
            print(row)

if info == '유도':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence7 + " like " + "'%" + "유도" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('유도')
        for row in result:
            print(row)

if info == '음악':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence7 + " like " + "'%" + "음악" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('음악')
        for row in result:
            print(row)

if info == '임용고시':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence7 + " like " + "'%" + "임용고시" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('임용고시')
        for row in result:
            print(row)

if info == '자전거':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence7 + " like " + "'%" + "자전거" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('자전거')
        for row in result:
            print(row)

if info == '종교':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence7 + " like " + "'%" + "종교" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('종교')
        for row in result:
            print(row)

if info == '창업':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence7 + " like " + "'%" + "창업" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('창업')
        for row in result:
            print(row)

if info == '천문':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence7 + " like " + "'%" + "천문" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('천문')
        for row in result:
            print(row)

if info == '체육':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence7 + " like " + "'%" + "체육" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('체육')
        for row in result:
            print(row)

if info == '축구':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence7 + " like " + "'%" + "축구" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('축구')
        for row in result:
            print(row)

if info == '춤':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence7 + " like " + "'%" + "춤" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('춤')
        for row in result:
            print(row)

if info == '컴퓨터':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence7 + " like " + "'%" + "컴퓨터" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('컴퓨터')
        for row in result:
            print(row)

if info == '탁구':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence7 + " like " + "'%" + "탁구" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('탁구')
        for row in result:
            print(row)

if info == '태권도':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence7 + " like " + "'%" + "태권도" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('태권도')
        for row in result:
            print(row)

if info == '테니스':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence7 + " like " + "'%" + "테니스" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('테니스')
        for row in result:
            print(row)

if info == '토론':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence7 + " like " + "'%" + "토론" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('토론')
        for row in result:
            print(row)

if info == '패러글라이딩':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence7 + " like " + "'%" + "패러글라이딩" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('패러글라이딩')
        for row in result:
            print(row)

if info == '풍물':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence7 + " like " + "'%" + "풍물" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('풍물')
        for row in result:
            print(row)

if info == '합창':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence7 + " like " + "'%" + "합창" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('합창')
        for row in result:
            print(row)

if info == '흑인음악':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence7 + " like " + "'%" + "흑인음악" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('흑인음악')
        for row in result:
            print(row)

if info == '힙합':
        querys = \
            "SELECT " + sentence5 + ", " + sentence6 + ", " + sentence7 + ", " + sentence8 + \
            " FROM " + sentence9 + \
            " WHERE " + sentence7 + " like " + "'%" + "힙합" + "%'"

        cur.execute(querys)
        result = cur.fetchall()
        print('힙합')
        for row in result:
            print(row)



print("end")
conn.close()
