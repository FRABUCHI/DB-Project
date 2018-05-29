from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import pymysql
from . import haksa_db_to_view
from . import haksa_sugang


def keyboard(request):
        return JsonResponse({
                'type' : 'buttons',
                'buttons' : ['학사 일정','도서 열람','동아리','아주봇']
        })

@csrf_exempt
def message(request):

        json_str = ((request.body).decode('utf-8'))
        json_data = json.loads(json_str)
        content_name = json_data['content']
        

        if content_name == '학사 일정' :
                return JsonResponse({
                        'message' : {
                                'text' : '어떤 일정이 궁금하세요?'
                        },
                        'keyboard' : {
                                'type' : 'buttons',
                                'buttons' : ['시험','방학','휴일','수강신청 관련','행정신청','입학/졸업','개강','아주봇','처음으로']
                        }
                })
            
        elif content_name == '시험' :
                return JsonResponse({
                        'message' : {
                                'text' : '학기를 선택해주세요.'
                        },
                        'keyboard' : {
                                'type' : 'buttons',
                                'buttons' : ['1학기','2학기','아주봇','처음으로']
                        }
                })
           
        #시험 및 성적 관련 일정
        elif content_name in ('1학기','2학기','중간','중간고사','기말','기말고사','성적','성적입력','성적정정','공고','방학'):
                info = str(haksa_db_to_view.haksa_db(content_name))
                return JsonResponse({
                        'message' : {
                                'text' : info
                        },
                        'keyboard' : {
                                'type' : 'buttons',
                                'buttons' : ['아주봇','처음으로']
                        }
                })

        #수강신청 관련 일정
        elif content_name in ('1학기','2학기','계절학기','예비수강','수강신청','수강정정','수강신청 포기','취득학점 포기'):
                info = str(haksa_db_to_view.haksa_db(content_name))
                return JsonResponse({
                        'message' : {
                                'text' : info
                        },
                        'keyboard' : {
                                'type' : 'buttons',
                                'buttons' : ['아주봇','처음으로']
                        }
                })

        elif content_name == '도서 열람' :
                return JsonResponse({
                        'message' : {
                                'text' : '무슨 책을 찾으십니까?'
                        },
                        'keyboard' : {
                                'type' : 'text'
                        }
                })

        elif content_name == '동아리' :
                return JsonResponse({
                        'message' : {
                                'text' : '중앙동아리 / 소학회 / 분류별 중 선택'
                        },
                        'keyboard' : {
                                'type' : 'buttons',
                                'buttons' : ['중앙동아리','소학회','분류별','처음으로']
                        }
                })

        elif content_name == '아주봇' :
                return JsonResponse({
                        'message' : {
                                'text' : '아주대에 관해 모르는거 빼고 다 알아요!'
                        },
                        'keyboard' : {
                                'type' : 'text'
                        }
                })


        elif content_name == '처음으로' :
                return JsonResponse({
                	'message' : {
                		'text' : '처음으로 돌아갑니다.'
                	},
                        'keyboard' : {
                                'type' : 'buttons',
                                'buttons' : ['학사 일정','도서 열람','도서관 여석','오늘의 메뉴','동아리','아주봇']
                        }
                })              

        else :
                return JsonResponse({
                        'message' : {
                                'text' : '아주봇이 알아듣지 못 했습니다. 다시 입력해주세요.'
                        },
                        'keyboard' : {
                                'type' : 'buttons',
                                'buttons' : ['학사 일정','도서 열람','도서관 여석','오늘의 메뉴','동아리','아주봇']
                        }
                })


