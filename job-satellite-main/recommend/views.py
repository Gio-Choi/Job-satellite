from django.shortcuts import render
import pandas as pd
import csv

from .models import jobdict, recruit_info, company, skill
import os
import warnings
from ast import literal_eval
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from django.shortcuts import redirect
warnings.filterwarnings('ignore')


def index(request):
    context = {
        'skillData': {
            '언어': {
                'id': 'Languages',
                'skills':
                [
                    ['Java', 'Java'],
                    ['Python', 'Python'],
                    ['C', 'Clang'],
                    ['C#', 'CSlang'],
                    ['C++', 'Cpp'],
                    ['Go', 'Go'],
                    ['Kotlin', 'Kotlin'],
                    ['JavaScript', 'JavaScript'],
                    ['HTML', 'HTML'],
                    ['CSS', 'CSS'],
                    ['PHP', 'PHP'],
                    ['JSP', 'JSP'],
                    ['TypeScript', 'TypeScript'],
                    ['Ruby', 'Ruby'],
                    ['Scala', 'Scala'],
                ]
            },
            '웹 개발': {
                'id': 'WEB',
                'skills':
                [
                    ['Spring', 'Spring'],
                    ['Django', 'Django'],
                    ['Vue.js', 'VueDotJS'],
                    ['Angular.js', 'AngularJS'],
                    ['.NET', 'DotNet'],
                    ['ASP.NET', 'ASPDotNet'],
                    ['Rails', 'Rails'],
                    ['jQuery', 'JQuery'],
                    ['React.js', 'ReactDotJS'],
                    ['Redux', 'Redux'],
                    ['Node.js', 'NodeDotJS'],
                    ['ASP', 'ASP'],
                    ['Webpack', 'Webpack'],
                    ['Ajax', 'Ajax'],
                ]
            },
            '앱 개발': {
                'id': 'APPS',
                'skills': [
                    ['IOS', 'IOS'],
                    ['Android', 'Android'],
                    ['Swift', 'Swift'],
                ]
            },
            'DB': {
                'id': 'DB',
                'skills': [
                    ['Oracle', 'Oracle'],
                    ['MySQL', 'MySQL'],
                    ['MsSQL', 'MsSQL'],
                    ['NoSQL', 'NoSQL'],
                    ['MariaDB', 'MariaDB'],
                    ['PostgreSQL', 'PostgreSQL'],
                    ['MongoDB', 'MongoDB'],
                    ['Redis', 'Redis'],
                    ['GraphQL', 'GraphQL'],
                ]
            },
            'AI': {
                'id': 'AI',
                'skills': [
                    ['Machine Learning', 'ML'],
                    ['Deep Learning', 'DL'],
                    ['CV', 'CV'],
                    ['PyTorch', 'Pytorch'],
                    ['TensorFlow', 'TensorFlow'],
                ]
            },
            '빅데이터, 서버': {
                'id': 'BigSer',
                'skills': [
                    ['Linux', 'Linux'],
                    ['Docker', 'Docker'],
                    ['Kubernetes', 'Kubernetes'],
                    ['Hadoop', 'Hadoop'],
                    ['Spark', 'Spark'],
                    ['Zeplin', 'Zeplin'],
                    ['Kafka', 'Kafka'],
                    ['WAS', 'WAS'],
                    ['AWS', 'AWS'],
                    ['GCP', 'GCP'],
                    ['Azure', 'Azure'],
                ]
            },
            '협업 툴': {
                'id': 'Coll',
                'skills': [
                    ['Git', 'Git'],
                    ['JIRA', 'JIRA'],
                    ['Jenkins', 'Jenkins'],
                    ['Slack', 'Slack'],
                ]
            },
            '기타': {
                'id': 'ETC',
                'skills': [
                    ['Photoshop', 'Photoshop'],
                    ['Sketch', 'Sketch'],
                    ['Illustrator', 'Illustrator'],
                    ['Unity3D', 'Unity3D'],
                    ['Maya', 'Maya'],
                ]
            }
        },
        'jobData': [
            ['CRM', 'CRM'],
            ['DBA', 'DBA'],
            ['ERP', 'ERP'],
            ['UI/UX/GUI디자인', 'UIUX'],
            ['게임개발', 'Game'],
            ['광고/시각디자인', 'Adver'],
            ['그래픽디자인', 'Graphic'],
            ['네트워크/보안/운영', 'Network'],
            ['데이터분석', 'Data'],
            ['모바일앱개발', 'Mobile'],
            ['반도체/디스플레이', 'Semicon'],
            ['소프트웨어아키텍트', 'Archi'],
            ['소프트웨어엔지니어', 'Engineer'],
            ['시스템엔지니어', 'System'],
            ['시장조사/분석', 'Market'],
            ['애니메이션디자인', 'Anim'],
            ['영상/모션디자인', 'Video'],
            ['온라인마케팅', 'OnMarket'],
            ['웹개발', 'WEB'],
            ['웹디자인', 'WebDe'],
            ['웹퍼블리셔', 'WebPu'],
            ['유지/수리/정비', 'Mainte'],
            ['일러스트레이터', 'Illust'],
            ['컨설팅', 'Consult'],
            ['프로젝트매니저', 'ProMana'],
            ['하드웨어엔지니어', 'Hardw'],
        ]
    }
    return render(request, 'recommend/index.html', context)


testJobData1 = [
    ['(주)아이패밀리에스씨', '서울', '기술연구소 NodeJS 개발자', '웹개발', 'MYSQL, nodejs, 백엔드 개발'],
    ['(주)아이패밀리에스씨', '서울', '기술연구소 NodeJS 개발자', '웹개발', 'MYSQL, nodejs, 백엔드 개발'],
    ['(주)아이패밀리에스씨', '서울', '기술연구소 NodeJS 개발자', '웹개발', 'MYSQL, nodejs, 백엔드 개발'],
    ['(주)아이패밀리에스씨', '서울', '기술연구소 NodeJS 개발자', '웹개발', 'MYSQL, nodejs, 백엔드 개발'],
    ['(주)아이패밀리에스씨', '서울', '기술연구소 NodeJS 개발자', '웹개발', 'MYSQL, nodejs, 백엔드 개발'],
]
testJobData2 = [
    ['에이알텍(주)', '서울', 'Windows 기반 어플리케이션 연구개발 분야 채용',
     '모바일앱개발, 소프트웨어엔지니어, 하드웨어엔지니어', 'C#, c, C++, TCP, IP, Visual studio'],
    ['에이알텍(주)', '서울', 'Windows 기반 어플리케이션 연구개발 분야 채용',
     '모바일앱개발, 소프트웨어엔지니어, 하드웨어엔지니어', 'C#, c, C++, TCP, IP, Visual studio'],
    ['에이알텍(주)', '서울', 'Windows 기반 어플리케이션 연구개발 분야 채용',
     '모바일앱개발, 소프트웨어엔지니어, 하드웨어엔지니어', 'C#, c, C++, TCP, IP, Visual studio'],
    ['에이알텍(주)', '서울', 'Windows 기반 어플리케이션 연구개발 분야 채용',
     '모바일앱개발, 소프트웨어엔지니어, 하드웨어엔지니어', 'C#, c, C++, TCP, IP, Visual studio'],
    ['에이알텍(주)', '서울', 'Windows 기반 어플리케이션 연구개발 분야 채용',
     '모바일앱개발, 소프트웨어엔지니어, 하드웨어엔지니어', 'C#, c, C++, TCP, IP, Visual studio'],
]
testJobData3 = [
    ['에이알텍(주)', '서울', 'Windows 기반 어플리케이션 연구개발 분야 채용',
     '모바일앱개발, 소프트웨어엔지니어, 하드웨어엔지니어', 'C#, c, C++, TCP, IP, Visual studio'],
    ['에이알텍(주)', '서울', 'Windows 기반 어플리케이션 연구개발 분야 채용',
     '모바일앱개발, 소프트웨어엔지니어, 하드웨어엔지니어', 'C#, c, C++, TCP, IP, Visual studio'],
    ['에이알텍(주)', '서울', 'Windows 기반 어플리케이션 연구개발 분야 채용',
     '모바일앱개발, 소프트웨어엔지니어, 하드웨어엔지니어', 'C#, c, C++, TCP, IP, Visual studio'],
    ['에이알텍(주)', '서울', 'Windows 기반 어플리케이션 연구개발 분야 채용',
     '모바일앱개발, 소프트웨어엔지니어, 하드웨어엔지니어', 'C#, c, C++, TCP, IP, Visual studio'],
    ['에이알텍(주)', '서울', 'Windows 기반 어플리케이션 연구개발 분야 채용',
     '모바일앱개발, 소프트웨어엔지니어, 하드웨어엔지니어', 'C#, c, C++, TCP, IP, Visual studio'],
]


def resultJob(request, kind):
    skills = request.GET.getlist('skills', None)
    first = request.GET.get('first', None)
    second = request.GET.get('second', None)
    third = request.GET.get('third', None)
    job1 = request.GET.get('job1', None)
    job2 = request.GET.get('job2', None)
    job3 = request.GET.get('job3', None)
    if kind == 'job':
        skillPerJobColumns = '''['skill', '웹개발', '네트워크/보안/운영', '시스템엔지니어', '소프트웨어엔지니어', 'QA', '기획', '데이터분석',
        '모바일앱개발', '프로젝트매니저', '게임개발', 'DBA', '컨설팅', '하드웨어엔지니어', '캐릭터디자인',
        '그래픽디자인', '애니메이션디자인', '마케팅', '시장조사/분석', '소프트웨어아키텍트', '웹퍼블리셔',
        'UI/UX/GUI디자인', '상품개발/기획/MD', '경영기획/전략', '광고/시각디자인', '영상/모션디자인',
        '영업기획/관리/지원', '경영지원', 'ERP', '일러스트레이터', '웹디자인', '기계', '전자/반도체', '제어',
        '전기', '반도체/디스플레이', '전기/전자/제어', '국내영업', '음악/음향/사운드', 'IT/솔루션영업',
        '온라인마케팅', '전략마케팅', '브랜드디자인', '브랜드마케팅', '출판/편집디자인', '방송연출/PD/감독',
        '고객지원/CS', '조직문화', 'CRM', '유지/수리/정비', '기술영업', '제품/산업디자인']'''
        skillPerJobStr = '''[['App', 62, 7, 34, 72, 12, 29, 9, 104, 14, 8, 3, 2, 0, 0, 5, 1, 2, 2, 8, 10, 37, 1, 3, 1, 0, 0, 2, 0, 0, 9, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 2], ['Kubernetes', 9, 7, 23, 24, 0, 0, 8, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['Hadoop', 11, 0, 7, 11, 0, 0, 31, 1, 1, 1, 5, 1, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['PyTorch', 1, 0, 14, 18, 0, 1, 12, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['C샵', 25, 4, 44, 83, 1, 0, 4, 10, 1, 19, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['TypeScript', 48, 0, 21, 39, 1, 0, 1, 13, 0, 4, 1, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['MongoDB', 11, 2, 9, 17, 0, 0, 2, 2, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['Unity3D', 2, 0, 16, 7, 0, 7, 0, 5, 1, 29, 0, 0, 1, 1, 11, 3, 0, 0, 0, 1, 11, 0, 0, 0, 2, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['Swift', 12, 2, 14, 20, 0, 0, 0, 51, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['Scala', 5, 0, 3, 14, 0, 0, 21, 1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['TensorFlow', 4, 0, 16, 24, 0, 1, 15, 1, 0, 0, 3, 1, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['Spring', 101, 9, 53, 88, 1, 0, 5, 21, 2, 1, 5, 1, 4, 0, 0, 0, 0, 0, 12, 4, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['Jenkins', 6, 2, 10, 13, 2, 0, 1, 5, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['NoSQL', 20, 3, 25, 28, 0, 0, 12, 9, 0, 2, 8, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['MySQL', 82, 8, 55, 62, 0, 1, 11, 9, 2, 3, 10, 0, 0, 0, 0, 0, 0, 0, 4, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['Java', 165, 16, 136, 230, 3, 4, 25, 61, 14, 14, 11, 1, 6, 0, 0, 0, 0, 0, 19, 5, 4, 0, 0, 0, 0, 0, 0, 3, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['Linux', 53, 20, 84, 104, 1, 2, 18, 10, 0, 6, 5, 1, 8, 0, 1, 0, 0, 0, 8, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['Docker', 23, 6, 36, 35, 1, 1, 9, 2, 3, 0, 1, 0, 1, 0, 0, 0, 0, 0, 8, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['NET', 15, 3, 12, 39, 0, 0, 0, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['Redux', 14, 0, 12, 16, 1, 0, 0, 7, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['ASPNET', 15, 0, 6, 18, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['PHP', 53, 2, 19, 29, 0, 4, 2, 3, 2, 2, 3, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['CSS', 83, 1, 35, 59, 0, 4, 1, 12, 1, 3, 0, 1, 1, 0, 0, 0, 0, 0, 2, 30, 11, 0, 0, 1, 0, 0, 0, 1, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['AWS', 91, 20, 74, 86, 1, 5, 25, 19, 6, 13, 16, 1, 0, 0, 1, 1, 0, 0, 11, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['Android', 27, 4, 33, 47, 19, 4, 4, 74, 5, 11, 0, 1, 1, 0, 0, 0, 0, 0, 4, 5, 11, 0, 0, 0, 0, 0, 1, 1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['WAS', 12, 9, 9, 8, 0, 0, 1, 3, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['MariaDB', 12, 3, 10, 9, 0, 0, 1, 1, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['MsSQL', 24, 2, 23, 33, 0, 0, 7, 3, 1, 0, 6, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['PostgreSQL', 11, 1, 7, 16, 0, 0, 4, 2, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['Django', 11, 0, 10, 14, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ['Python', 51, 13, 78, 102, 5, 10, 76, 15, 6, 12, 13, 2, 1, 0, 8, 1, 1, 0, 9, 2, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 3, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], ['HTML', 90, 2, 43, 71, 0, 4, 2, 15, 1, 5, 1, 1, 1, 0, 0, 0, 0, 0, 3, 30, 12, 0, 0, 1, 0, 0, 0, 1, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['Spark', 8, 1, 7, 15, 0, 1, 33, 2, 1, 1, 7, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['JSP', 41, 3, 17, 42, 0, 1, 1, 7, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['JIRA', 8, 3, 19, 21, 17, 1, 0, 4, 3, 1, 1, 0, 4, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['jQuery', 55, 0, 14, 32, 1, 0, 0, 3, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 19, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['Go', 13, 5, 23, 20, 1, 1, 5, 4, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['C언어', 16, 8, 72, 117, 1, 0, 5, 13, 4, 22, 2, 0, 5, 0, 1, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 7, 1, 2, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], ['Kotlin', 12, 1, 16, 27, 0, 0, 4, 34, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['Ruby', 8, 1, 16, 16, 1, 0, 4, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['GCP', 11, 5, 15, 24, 0, 1, 12, 2, 0, 2, 4, 0, 0, 0, 1, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['Data', 13, 4, 25, 33, 2, 3, 75, 3, 13, 3, 5, 2, 0, 0, 0, 0, 0, 0, 5, 1, 5, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0], ['IOS', 31, 4, 40, 44, 18, 5, 3, 85, 8, 19, 0, 0, 1, 0, 1, 0, 0, 0, 4, 5, 14, 0, 1, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], ['C쁠쁠', 22, 9, 90, 157, 3, 2, 7, 10, 2, 37, 3, 0, 3, 0, 3, 0, 0, 0, 6, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 9, 2, 1, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['Rails', 7, 0, 8, 15, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [
            'Webpack', 21, 0, 6, 13, 1, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['JavaScript', 118, 5, 41, 91, 1, 3, 2, 20, 2, 3, 0, 0, 2, 0, 0, 0, 0, 0, 5, 35, 5, 0, 0, 0, 0, 0, 0, 1, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['Azure', 10, 6, 11, 13, 0, 2, 5, 4, 0, 1, 2, 0, 0, 0, 1, 1, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['Vuejs', 58, 0, 18, 45, 0, 0, 0, 10, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 2, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['ASP', 18, 3, 9, 19, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['Oracle', 29, 2, 38, 43, 0, 2, 9, 2, 2, 0, 6, 2, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['Git', 72, 7, 61, 76, 6, 2, 4, 34, 2, 6, 5, 1, 5, 0, 0, 0, 0, 0, 11, 8, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['GraphQL', 13, 0, 12, 12, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['AngularJS', 50, 0, 18, 40, 0, 0, 0, 9, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 2, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['Ajax', 18, 0, 7, 10, 0, 0, 0, 4, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['DL', 1, 0, 20, 17, 0, 0, 12, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['ML', 2, 0, 17, 20, 0, 1, 22, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['DB', 59, 20, 79, 92, 2, 4, 39, 17, 5, 14, 19, 2, 2, 0, 0, 0, 1, 0, 7, 2, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['Redis', 25, 2, 17, 29, 0, 0, 2, 3, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['Slack', 12, 1, 17, 12, 1, 0, 1, 3, 2, 1, 2, 0, 1, 0, 0, 0, 0, 0, 2, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ['Zeplin', 1, 0, 10, 4, 1, 0, 0, 5, 2, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 21, 0, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['Nodejs', 77, 4, 44, 62, 2, 1, 1, 15, 2, 6, 1, 0, 1, 0, 0, 0, 0, 0, 3, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['Sketch', 1, 0, 5, 0, 1, 1, 0, 0, 2, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 1, 27, 0, 0, 1, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['ReactJS', 110, 0, 41, 79, 3, 2, 1, 30, 4, 2, 1, 0, 1, 0, 0, 0, 0, 0, 6, 17, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['Kafka', 5, 2, 10, 18, 0, 0, 12, 2, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['CV', 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ['Illustrator', 0, 0, 1, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0, 8, 1, 0, 0, 0, 1, 15, 0, 0, 2, 2, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 3, 1, 0, 2, 0, 0, 0, 0, 0, 0], ['Photoshop', 0, 0, 1, 0, 0, 3, 0, 0, 2, 6, 0, 0, 0, 1, 16, 4, 0, 0, 0, 3, 19, 0, 0, 2, 1, 0, 0, 0, 2, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 3, 1, 0, 3, 0, 0, 0, 0, 0, 0], ['Maya', 0, 0, 1, 0, 0, 0, 1, 0, 4, 2, 0, 0, 0, 0, 21, 8, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 4, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]'''
        df = pd.DataFrame(eval(skillPerJobStr))
        df.columns = eval(skillPerJobColumns)

        wordDict = {
            'skill': 'needSkill',
            '웹개발': 'web',
            '네트워크/보안/운영': 'network',
            '시스템엔지니어': 'se',
            '소프트웨어엔지니어': 'soft',
            'QA': 'qa',
            '기획': 'plan',
            '데이터분석': 'da',
            '모바일앱개발': 'app',
            '프로젝트매니저': 'pm',
            '게임개발': 'game',
            'DBA': 'dba',
            '컨설팅': 'consulting',
            '하드웨어엔지니어': 'he',
            '캐릭터디자인': 'cd',
            '그래픽디자인': 'gd',
            '애니메이션디자인': 'ad',
            '마케팅': 'marketing',
            '시장조사/분석': 'market',
            '소프트웨어아키텍트': 'sa',
            '웹퍼블리셔': 'wp',
            'UI/UX/GUI디자인': 'ud',
            '상품개발/기획/MD': 'md',
            '경영기획/전략': 'strategy',
            '광고/시각디자인': 'advertise',
            '영상/모션디자인': 'video',
            '영업기획/관리/지원': 'sales',
            '경영지원': 'support',
            'ERP': 'erp',
            '일러스트레이터': 'iu',
            '웹디자인': 'wd',
            '기계': 'machine',
            '전자/반도체': 'esemi',
            '제어': 'control',
            '전기': 'elec',
            '반도체/디스플레이': 'dsemi',
            '전기/전자/제어': 'econtrol',
            '국내영업': 'domsales',
            '음악/음향/사운드': 'sound',
            'IT/솔루션영업': 'itsol',
            '온라인마케팅': 'emarketing',
            '전략마케팅': 'smarketing',
            '브랜드디자인': 'bd',
            '브랜드마케팅': 'bmarketing',
            '출판/편집디자인': 'publish',
            '방송연출/PD/감독': 'pd',
            '고객지원/CS': 'cs',
            '조직문화': 'culture',
            'CRM': 'crm',
            '유지/수리/정비': 'maintenance',
            '기술영업': 'tech',
            '제품/산업디자인': 'product',
        }
        # df = pd.DataFrame(list(skill.objects.all().values()))
        targetList = []
        if job1 != '':
            targetList.append(job1)
        if job2 != '':
            targetList.append(job2)
        if job3 != '':
            targetList.append(job3)
        returnValue = []
        for item in targetList:
            temp = df[['skill', item]].sort_values(
                by=[item], ascending=False)[:5]
            temp = temp[temp[item] != 0]
            returnValue.append(temp.values.tolist())
        cotext = {
            'context': {
                'kind': kind,
                'job1': job1,
                'job2': job2,
                'job3': job3,
                'returnData': returnValue,
            }
        }
    elif kind == 'skill':
        df = pd.DataFrame(list(jobdict.objects.all().values()))
        df = df.dropna(axis=0)
        wordDict2 = {
            '복지 및 급여': 'salary',
            '업무와 삶의 균형': 'wlb',
            '사내문화': 'culture',
            '승진 기회 및 가능성': 'possibility',
            '경영진': 'management',
        }
        vectorizer = CountVectorizer()  # 피쳐 벡터화
        feature_vector_job = vectorizer.fit_transform(df['skill'])  # 피쳐 벡터 행렬
        feature_job = vectorizer.get_feature_names()
        person_vec = np.zeros((1, 70))
        person = skills
        for skill in person:
            newSkill = skill.replace('Cpp', 'C쁠블').replace(
                'CSlang', 'C샵')
            newSkill = newSkill.replace(
                'lang', '언어').replace('Dot', '닷').lower()
            index = feature_job.index(newSkill)
            person_vec[0][index] = 1
        # 코사인 유사도 계산
        skill_sim = cosine_similarity(feature_vector_job, person_vec)
        df['similarity'] = ''
        df['similarity'] = skill_sim
        df.sort_values(by='similarity', ascending=False).head(10)
        job_sim_result = df.sort_values(
            by='similarity', ascending=False).head(3)
        job_sim_result = job_sim_result['job'].values.tolist()
        # 공고 추천
        # total 공고 파일 업로드
        df_total = pd.DataFrame(list(recruit_info.objects.all().values()))
        df_total = df_total.dropna(axis=0, subset=["total_skill_literal"])
        vectorizer = CountVectorizer()  # 피쳐 벡터화
        feature_vector_title = vectorizer.fit_transform(
            df_total['total_skill_literal'])  # 피쳐 벡터 행렬
        feature_title = vectorizer.get_feature_names()
        person_vec_title = np.zeros((1, 70))
        for skill in person:
            newSkill = skill.replace('Cpp', 'C쁠블').replace(
                'CSlang', 'C샵')
            newSkill = newSkill.replace(
                'lang', '언어').replace('Dot', '닷').lower()
            index = feature_title.index(newSkill)
            person_vec[0][index] = 1
        person_vec
        # 코사인 유사도 계산
        skill_sim = cosine_similarity(feature_vector_title, person_vec)
        df_total['similarity'] = ''
        df_total['similarity'] = skill_sim
        df_total_new_sorting = df_total.sort_values(
            by='similarity', ascending=False)
        df_finals = []
        df_finals.append(df_total_new_sorting[df_total_new_sorting.job.str.find(
            job_sim_result[0]) > -1][:30])
        df_finals.append(df_total_new_sorting[df_total_new_sorting.job.str.find(
            job_sim_result[1]) > -1][:30])
        df_finals.append(df_total_new_sorting[df_total_new_sorting.job.str.find(
            job_sim_result[2]) > -1][:30])
        df_finals[0] = df_finals[0][df_finals[0]['similarity'] != 0]
        df_finals[1] = df_finals[1][df_finals[1]['similarity'] != 0]
        df_finals[2] = df_finals[2][df_finals[2]['similarity'] != 0]
        returnPosts = []
        for idx, df in enumerate(df_finals):
            totalScroe = []
            for (index, item) in df.iterrows():
                reviewScore = round(
                    0.2 * (item['reviewCount'] if item['reviewCount'] < 10 else 10), 1)
                totalScroe.append(round((item['similarity'] * 20) + reviewScore + item['average'] + ((item[wordDict2[first]] if first != None else 0) * 0.6) + (
                    (item[wordDict2[second]] if second != None else 0) * 0.4) + ((item[wordDict2[third]] if third != None else 0) * 0.2), 2))
            df_finals[idx]['totalScore'] = totalScroe
            df_finals[idx].sort_values(
                by=['totalScore'], axis=0, ascending=False, inplace=True)
            replaceItems = []
            for item in df_finals[idx]['total_skill_literal']:
                replaceItems.append(item.replace('닷', '.').replace(
                    ' ', ', ').replace('쁠블', '++').replace('샵', '#'))
            df_finals[idx]['total_skill_literal'] = replaceItems
            returnPosts.append(df_finals[idx][:10].values.tolist())
        cotext = {
            'context': {
                'kind': kind,
                'skills': skills,
                'first': first,
                'second': second,
                'third': third,
                'jobs': job_sim_result,
                'returnValue': returnPosts,
            }
        }
    return render(request, 'recommend/result_job.html', cotext)


def dbsetupView(request):
    return render(request, 'recommend/dbsetup/dbsetup.html')


def insertDataFromCSV(request):
    response = redirect('/reco/dbsetup/')
    frontPath = 'recommend/db/'
    CSV_PATH = frontPath + 'job_dict_final.csv'
    with open(CSV_PATH, newline='', encoding="utf-8")as csvfile:
        data_reader = csv.DictReader(csvfile)
        for row in data_reader:
            try:
                jobdict.objects.create(job=row['job'], skill=row['skill'])
            except:
                continue

    CSV_PATH2 = frontPath + 'job_rating.csv'
    with open(CSV_PATH2, newline='', encoding="utf-8")as csvfile:
        data_reader = csv.DictReader(csvfile)
        for row in data_reader:
            try:
                recruit_info.objects.create(jobId=row['jobId'], company=row['company'],
                                            title=row['title'], job=row['job'], region=row['region'],
                                            jobUrl=row['jobUrl'], total_skill=row['total_skill'],
                                            total_skill_literal=row['total_skill_literal'], reviewCount=row['reviewCount'],
                                            average=row['average'], salary=row['salary'], wlb=row['wlb'], culture=row['culture'],
                                            possibility=row['possibility'], management=row['management'])
            except:
                continue

    # CSV_PATH3 = frontPath + 'company_rating_list.csv'
    # with open(CSV_PATH3, newline='', encoding="utf-8")as csvfile:
    #     data_reader = csv.DictReader(csvfile)

    #     for row in data_reader:
    #         try:
    #             company.objects.create(companyId=row['companyId'], company_name=row['company'], reviewCount=row['reviewCount'],
    #                                    average=row['average'], salary=row['salary'], wlb=row['wlb'], culture=row['culture'],
    #                                    possibility=row['possibility'], management=row['management'])
    #             print(row['companyId'])
    #         except:
    #             continue

    # CSV_PATH4 = frontPath + 'skillPerJob.csv'
    # with open(CSV_PATH4, newline='', encoding="utf-8")as csvfile:
    #     data_reader = csv.DictReader(csvfile)
    #     for row in data_reader:
            # try:
            # skill.objects.create(needSkill=row['skill'], web=row['웹개발'], network=row['네트워크/보안/운영'], se=row['시스템엔지니어'],
            #                     soft=row['소프트웨어엔지니어'], qa=row['QA'], plan=row['기획'],
            #                     da=row['데이터분석'], app=row['모바일앱개발'], pm=row['프로젝트매니저'],
            #                     game=row['게임개발'], dba=row['DBA'], consulting=row['컨설팅'],
            #                     he=row['하드웨어엔지니어'], cd=row['캐릭터디자인'],
            #                     gd=row['그래픽디자인'], ad=row['애니메이션디자인'], marketing=row['마케팅'],
            #                     market=row['시장조사/분석'], sa=row['소프트웨어아키텍트'], wp=row['웹퍼블리셔'],
            #                     ud=row['UI/UX/GUI디자인'], md=row['상품개발/기획/MD'], strategy=row['경영기획/전략'],
            #                     advertise=row['광고/시각디자인'], video=row['영상/모션디자인'], sales=row['영업기획/관리/지원'],
            #                     support=row['경영지원'], erp=row['ERP'], iu=row['일러스트레이터'],
            #                     wd=row['웹디자인'], machine=row['기계'], esemi=row['전자/반도체'],
            #                     control=row['제어'], elec=row['전기'], dsemi=row['반도체/디스플레이'],
            #                     econtrol=row['전기/전자/제어'], domsales=row['국내영업'],
            #                     sound=row['음악/음향/사운드'], itsol=row['IT/솔루션영업'], emarketing=row['온라인마케팅'],
            #                     smarketing=row['전략마케팅'], bd=row['브랜드디자인'], bmarketing=row['브랜드마케팅'],
            #                     publish=row['출판/편집디자인'], pd=row['방송연출/PD/감독'], cs=row['고객지원/CS'],
            #                     culture=row['조직문화'],
            #                     crm=row['CRM'], maintenance=row['유지/수리/정비'], tech=row['기술영업'], product=row['제품/산업디자인'])
            # print(row['skill'])
            # except:
            #     continue

    return response


def fir_result(request):
    context = {}

    df = pd.DataFrame(list(jobdict.objects.all().values()))
    df = df.dropna(axis=0)
    # context={'df':df}

    df['job'][4] = 'QA'
    df['job'][10] = 'DBA'

    vectorizer = CountVectorizer()  # 피쳐 벡터화

    feature_vector_job = vectorizer.fit_transform(df['skill'])  # 피쳐 벡터 행렬
    feature_job = vectorizer.get_feature_names()

    person_vec = np.zeros((1, 70))
    # person 임의로 줌 input값!!
    # person=['vue닷js','redux','ruby','닷net']
    person = ['python']
    for skill in person:
        index = feature_job.index(skill)
        person_vec[0][index] = 1
    person_vec

    # 코사인 유사도 계산

    skill_sim = cosine_similarity(feature_vector_job, person_vec)

    df['similarity'] = ''
    df['similarity'] = skill_sim
    df.sort_values(by='similarity', ascending=False).head(10)

    job_sim_result = df.sort_values(by='similarity', ascending=False).head(3)
    job_sim_result = job_sim_result['job'].values

    # 공고 추천

    # total 공고 파일 업로드
    df_total = pd.DataFrame(list(recruit_info.objects.all().values()))

    df_total_new = df_total.copy()

    df_total_new = df_total_new.dropna(axis=0, subset=["total_skill_literal"])

    vectorizer = CountVectorizer()  # 피쳐 벡터화

    feature_vector_title = vectorizer.fit_transform(
        df_total_new['total_skill_literal'])  # 피쳐 벡터 행렬
    feature_title = vectorizer.get_feature_names()

    person_vec_title = np.zeros((1, 70))

    for skill in person:
        index = feature_title.index(skill)
        person_vec[0][index] = 1
    person_vec

    # 코사인 유사도 계산

    skill_sim = cosine_similarity(feature_vector_title, person_vec)

    df_total_new['similarity'] = ''
    df_total_new['similarity'] = skill_sim
    df_total_new_sorting = df_total_new.sort_values(
        by='similarity', ascending=False)
    df_total_new_sorting[:]

    # 나온 공고중에 직무를 만족시키는 공고 5개 뽑기

    job_1 = job_sim_result[0]
    df_final_1 = df_total_new_sorting[df_total_new_sorting.job.str.find(
        job_1) > -1]

    job_2 = job_sim_result[1]
    df_final_2 = df_total_new_sorting[df_total_new_sorting.job.str.find(
        job_2) > -1]

    job_3 = job_sim_result[2]
    df_final_3 = df_total_new_sorting[df_total_new_sorting.job.str.find(
        job_3) > -1]
    context = {'job1': job_1, 'df': df_final_1, 'job2': job_2,
               22: df_final_2, 'job3': job_3, 33: df_final_3}
    return render(request, 'result1.html', context)


def wanna_job(request):
    context2 = {'job': [
        {'id': 'web', 'name': '웹개발'}, {'id': 'network',
                                       'name': '네트워크/보안/운영'}, {'id': 'se', 'name': '시스템엔지니어'},
        {'id': 'soft', 'name': '소프트웨어엔지니어'}, {
            'id': 'qa', 'name': 'Quality Assurance'},
        {'id': 'plan', 'name': '기획'}, {'id': 'da', 'name': '데이터분석'}, {
            'id': 'app', 'name': '모바일앱개발'},
        {'id': 'pm', 'name': '프로젝트매니저'}, {'id': 'game', 'name': '게임개발'},
        {'id': 'dba', 'name': 'Database Admin'}, {'id': 'consulting',
                                                  'name': '컨설팅'}, {'id': 'he', 'name': '하드웨어엔지니어'},
        {'id': 'cd', 'name': '캐릭터디자인'},
        {'id': 'gd', 'name': '그래픽디자인'}, {'id': 'ad', 'name': '애니메이션디자인'}, {
            'id': 'marketing', 'name': '마케팅'},
        {'id': 'market', 'name': '시장조사/분석'},
        {'id': 'sa', 'name': '소프트웨어아키텍트'}, {'id': 'wp', 'name': '웹퍼블리셔'}, {
            'id': 'ud', 'name': 'UI/UX/GUI디자인'},
        {'id': 'md', 'name': '상품개발/기획/MD'},
        {'id': 'strategy', 'name': '경영기획/전략'}, {'id': 'advertise', 'name': '광고/시각디자인'},
        {'id': 'video', 'name': '영상/모션디자인'}, {'id': 'sales', 'name': '영업기획/관리/지원'},
        {'id': 'support', 'name': '경영지원'}, {'id': 'erp',
                                            'name': 'ERP'}, {'id': 'iu', 'name': '일러스트레이터'},
        {'id': 'wd', 'name': '웹디자인'}, {'id': 'machine', 'name': '기계'},
        {'id': 'esemi', 'name': '전자/반도체'}, {'id': 'control',
                                            'name': '제어'}, {'id': 'elec', 'name': '전기'},
        {'id': 'dsemi', 'name': '반도체/디스플레이'},
        {'id': 'econtrol', 'name': '전기/전자/제어'}, {'id': 'domsales', 'name': '국내영업'},
        {'id': 'sound', 'name': '음악/음향/사운드'}, {'id': 'itsol', 'name': 'IT/솔루션영업'},
        {'id': 'emarketing', 'name': '온라인마케팅'}, {'id': 'smarketing',
                                                 'name': '전략마케팅'}, {'id': 'bd', 'name': '브랜드디자인'},
        {'id': 'bmarketing', 'name': '브랜드마케팅'},
        {'id': 'publish', 'name': '출판/편집디자인'}, {'id': 'pd',
                                                'name': '방송연출/PD/감독'}, {'id': 'cs', 'name': '고객지원/CS'},
        {'id': 'culture', 'name': '조직문화'},
        {'id': 'crm', 'name': 'CRM'}, {'id': 'maintenance', 'name': '유지/수리/정비'}, {'id': 'tech', 'name': '기술영업'}, {'id': 'product', 'name': '제품/산업디자인'}]}
    return render(request, 'infojob.html', context2)


# def sec_result(requese):
#     return render(requese, 'result2.html')


# def readCsv(address):
#     df = pd.read_csv(address)
#     return df
# # address 파라미터 적어줄때  => r'절대주소'


# test_df = readCsv(r'C:\Users\네리\Desktop\sba_re\4조\job_data_list_final.csv')
# print(test_df.columns)
# # col=index,jobId,company,title,job,skill,region,experience,intro
# # task,require,prefer,jobUrl
# test_df = test_df.fillna('')

# print(type(test_df['jobId'][0]))

# # test => titleId,company,title,job,skill


# def create():
#     for i in range(len(test_df)):
#         test.objects.create(titleId=test_df['jobId'][i], company=test_df['company'][i],
#                             title=test_df['title'][i], job=test_df['job'][i], skill=test_df['skill'][i])


# print(len(test_df))
# # model.objects.all()
# # print(jobdict.objects.all())'
# # django.core.exceptions.ImproperlyConfigured: Requested setting INSTALLED_APPS, but settings are not configured.
# # You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.
