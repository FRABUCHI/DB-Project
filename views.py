from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import pymysql
from . import haksa_db_to_view
#from . import haksa_sugang


def keyboard(request):
        return JsonResponse({
                'type' : 'buttons',
                'buttons' : ['학사일정','음식점','동아리','아주봇']
        })

@csrf_exempt
def message(request):

        json_str = ((request.body).decode('utf-8'))
        json_data = json.loads(json_str)
        content_name = json_data['content']
        

        if content_name == '학사일정' or '일정' :
                return JsonResponse({
                        'message' : {
                                'text' : '어떤 일정이 궁금하세요?'
                        },
                        'keyboard' : {
                                'type' : 'buttons',
                                'buttons' : ['전체','시험','방학','휴일','수강신청 관련','행정신청','입학/졸업','개강','아주봇','처음으로']
                        }
                })

        #시험 및 성적 관련 일정    
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
                return JsonResponse({
                        'message' : {
                                'text' : info
                        },
                        'keyboard' : {
                                'type' : 'buttons',
                                'buttons' : ['아주봇','처음으로']
                        }
                })
        #휴일 관련 일정
        elif content_name == '휴일' or '공휴일' or '쉬는날': 
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
        #전체 학사 일정
        elif content_name == '전체' or '전체학사일정' or '전체일정': 
                info = str(haksa_db_to_view.haksa_db(content_name))
                return JsonResponse({
                        'message' : {
                                'text' : info
                        },
                        'keyboard' : {
                                'type' : 'buttons',
                                'buttons' : ['예비수강','수강신청','수강정정','수강신청 포기','취득학점 포기','아주봇','처음으로']
                        }
                })
        
        #입학/졸업 관련 일정
        elif content_name == '입학/졸업': 
                info = str(haksa_db_to_view.haksa_db(content_name))
                return JsonResponse({
                        'message' : {
                                'text' : info
                        },
                        'keyboard' : {
                                'type' : 'buttons',
                                'buttons' : ['입학식(신·편입)','졸업식(학위 수여식)','아주봇','처음으로']
                        }
                })

        #입학/졸업 관련 일정
        elif content_name == '입학식': 
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
        
        #입학/졸업 관련 일정
        elif content_name == '졸업식': 
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
                

        #개강 일정
        elif content_name == '개강' or '개강날짜' or '개강일정': 
        info = str(haksa_db_to_view.haksa_db(content_name))
        return JsonResponse({
                'message' : {
                        'text' : info
                },
                'keyboard' : {
                        'type' : 'buttons',
                        'buttons' : ['예비수강','수강신청','수강정정','수강신청 포기','취득학점 포기','아주봇','처음으로']
                }
        })
        
        #수강신청 관련 일정
        elif content_name == '수강신청 관련':
                info = str(haksa_db_to_view.haksa_db(content_name))
                return JsonResponse({
                        'message' : {
                                'text' : info
                        },
                        'keyboard' : {
                                'type' : 'buttons',
                                'buttons' : ['예비수강','수강신청','수강정정','수강신청 포기','취득학점 포기','아주봇','처음으로']
                        }
                })

        #방학 일정
        elif content_name == '방학' or '여름방학' or '겨울방학':
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
        #행정신청 관련 일정
        elif content_name == '행정신청':
                info = str(haksa_db_to_view.haksa_db(content_name))
                return JsonResponse({
                        'message' : {
                                'text' : info
                        },
                        'keyboard' : {
                                'type' : 'buttons',
                                'buttons' : ['전과','학기등록','전공/졸업 신청','아주봇','처음으로']
                        }
                })
      
        #행정신청 관련 일정
        elif content_name == '전과' or '전과신청' or '전과 신청':
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

        #행정신청 관련 일정
        elif content_name == '학기등록' or '등록' or '학기 등록':
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

        #행정신청 관련 일정
        #이 부분은 영준씨가 추가로 수정해도 됩니다. 분류가 많아서
        #major = [전공신청,전공변경,전공취소]
        #submajor = [부전공신청,부전공변경,부전공취소]
        #elif content_name == major or submajor
        #elif content_name == in(major,submajor)
        #이런식으로 정리될수 있을거 같은데 파이썬 문법 찾아서 조금 더 깔끔하게 할 수 있으면 그렇게 해주세요.
        elif content_name == in('전공/졸업 신청','졸업유예','졸업연기','졸업 유예','졸업 연기','전공 변경','전공 취소','복수전공','부전공','연계전공'):
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


