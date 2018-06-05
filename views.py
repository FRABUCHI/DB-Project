from django.shortcuts import render
from django.template.response import TemplateResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import pymysql
from . import haksa_db_to_view
#from . import haksa_sugang

startButton = ['학사일정','음식점','동아리','아주봇']
endButton = ['아주봇','처음으로']
clubButton = ['중앙동아리','소학회']


def keyboard(request):
        return JsonResponse({
                'type' : 'buttons',
                'buttons' : startButton
        })

@csrf_exempt
def message(request):

        json_str = ((request.body).decode('utf-8'))
        json_data = json.loads(json_str)
        content_name = json_data['content']
        
#############################################################################################################
        if content_name == '학사일정' :
                return JsonResponse({
                        'message' : {
                                'text' : '어떤 일정이 궁금하세요?'
                        },
                        'keyboard' : {
                                'type' : 'buttons',
                                'buttons' : ['전체','시험','방학','휴일','수강신청 관련','행정신청','입학/졸업','개강','아주봇','처음으로']
                        }
                })
#############################################################################################################

        #전체 학사 일정
        if content_name in ('전체','전체학사일정','학사력'): 
              info = str(haksa_db_to_view.haksa_db(content_name))
              return JsonResponse({
                      'message' : {
                              'text' : info
                      },
                      'keyboard' : {
                              'type' : 'buttons',
                              'buttons' : endButton
                      }
              })
#############################################################################################################

        #시험 및 성적 관련 일정    
        if content_name == '시험' :
                return JsonResponse({
                        'message' : {
                                'text' : '학기를 선택해주세요.'
                        },
                        'keyboard' : {
                                'type' : 'buttons',
                                'buttons' : ['1학기','2학기','아주봇','처음으로']
                        }
                })

        # 시험 및 성적 관련 일정 
        if content_name in ('1학기','2학기','중간','중간고사','기말','기말고사','성적','성적입력','성적정정','공고'):
              info = str(haksa_db_to_view.haksa_db(content_name))
              return JsonResponse({
                      'message' : {
                              'text' : info
                      },
                      'keyboard' : {
                              'type' : 'buttons',
                              'buttons' : endButton
                      }
              })
#############################################################################################################

        #수강신청 관련 일정
        elif content_name == '수강신청 관련':
                return JsonResponse({
                        'message' : {
                                'text' : '수강 관련 목록입니다.'
                        },
                        'keyboard' : {
                                'type' : 'buttons',
                                'buttons' : ['예비수강','수강신청','수강정정','수강신청 포기','취득학점 포기','아주봇','처음으로']
                        }
                })
           
        #수강신청 관련 일정
        elif content_name in ('예비수강','수강신청','수강정정','수강신청 포기','취득학점 포기'):
                info = str(haksa_db_to_view.haksa_db(content_name))
                return JsonResponse({
                        'message' : {
                                'text' : info
                        },
                        'keyboard' : {
                                'type' : 'buttons',
                                'buttons' : endButton
                        }
                })
#############################################################################################################
        # 방학
        elif content_name in ('방학','여름방학','겨울방학'):
                info = str(haksa_db_to_view.haksa_db(content_name))
                return JsonResponse({
                        'message' : {
                                'text' : info
                        },
                        'keyboard' : {
                                'type' : 'buttons',
                                'buttons' : endButton
                        }
                })
#############################################################################################################
        # 휴일
        elif content_name in ('휴일','공휴일','쉬는날'):
                info = str(haksa_db_to_view.haksa_db(content_name))
                return JsonResponse({
                        'message' : {
                                'text' : info
                        },
                        'keyboard' : {
                                'type' : 'buttons',
                                'buttons' : endButton
                        }
                })

#############################################################################################################
        # 입학식/졸업식
        elif content_name == '입학/졸업':
                return JsonResponse({
                        'message' : {
                                'text' : '입학/졸업 관련 목록입니다.'
                        },
                        'keyboard' : {
                                'type' : 'buttons',
                                'buttons' : ['입학식(신·편입)','졸업식(학위 수여식)','아주봇','처음으로']
                        }
                })
        # 입학식/졸업식
        elif content_name in ('입학식','졸업식','입학식(신·편입)','졸업식(학위 수여식)'):
                info = str(haksa_db_to_view.haksa_db(content_name))
                return JsonResponse({
                        'message' : {
                                'text' : info
                        },
                        'keyboard' : {
                                'type' : 'buttons',
                                'buttons' : endButton
                        }
                })           
#############################################################################################################
        #개강 일정
        elif content_name in ('개강','개강날짜','개강일정'): 
                info = str(haksa_db_to_view.haksa_db(content_name))
                return JsonResponse({
                        'message' : {
                                'text' : info
                        },
                        'keyboard' : {
                                'type' : 'buttons',
                                'buttons' : endButton
                        }
        })
#############################################################################################################
        #행정신청 관련 일정
        elif content_name == '행정신청':
                return JsonResponse({
                        'message' : {
                                'text' : '행정신청 관련 목록입니다.'
                        },
                        'keyboard' : {
                                'type' : 'buttons',
                                'buttons' : ['전과','학기등록','전공/졸업 신청','아주봇','처음으로']
                        }
                })
      
        #행정신청 관련 일정
        elif content_name in ('전과','전과신청','전과 신청'):
                info = str(haksa_db_to_view.haksa_db(content_name))
                return JsonResponse({
                        'message' : {
                                'text' : info
                        },
                        'keyboard' : {
                                'type' : 'buttons',
                                'buttons' : endButton
                        }
                })

        #행정신청 관련 일정
        elif content_name in('학기등록','등록','학기 등록'):
                info = str(haksa_db_to_view.haksa_db(content_name))
                return JsonResponse({
                        'message' : {
                                'text' : info
                        },
                        'keyboard' : {
                                'type' : 'buttons',
                                'buttons' : endButton
                        }
                })

        elif content_name in ('전공/졸업 신청','졸업유예','졸업연기','졸업 유예','졸업 연기','전공 변경','전공 취소','복수전공','부전공','연계전공'):
                info = str(haksa_db_to_view.haksa_db(content_name))
                return JsonResponse({
                        'message' : {
                                'text' : info
                        },
                        'keyboard' : {
                                'type' : 'buttons',
                                'buttons' : endButton
                        }
                })
#############################################################################################################
        if content_name == '동아리' :
                return JsonResponse({
                        'message' : {
                                'text' : '동아리를 선택해주세요.'
                        },
                        'keyboard' : {
                                'type' : clubButton
                        }
                })

        if content_name == '중앙동아리' :
                return JsonResponse({
                        'message' : {
                                'text' : '아주대에 관해 모르는거 빼고 다 알아요!'
                        },
                        'keyboard' : {
                                'type' : startButton
                        }
                })

        if content_name == '소학회' :
                return JsonResponse({
                        'message' : {
                                'text' : '아주대에 관해 모르는거 빼고 다 알아요!'
                        },
                        'keyboard' : {
                                'type' : startButton
                        }
                })
#############################################################################################################
        
        if content_name == '아주봇' :
                return JsonResponse({
                        'message' : {
                                'text' : '아주대에 관해 모르는거 빼고 다 알아요!'
                        },
                        'keyboard' : {
                                'type' : 'text'
                        }
                })


        if content_name == '처음으로' :
                return JsonResponse({
                	'message' : {
                		'text' : '처음으로 돌아갑니다.'
                	},
                        'keyboard' : {
                                'type' : 'buttons',
                                'buttons' : startButton
                        }
                })              

        else :
                return JsonResponse({
                        'message' : {
                                'text' : '아주봇이 알아듣지 못 했습니다. 다시 입력해주세요.'
                        },
                        'keyboard' : {
                                'type' : 'buttons',
                                'buttons' : startButton
                        }
                })


