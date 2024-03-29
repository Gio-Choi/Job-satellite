# Job-satellite
## IT 직군 취준생을 위한 직무/공고 CBF추천시스템 구현
### 서울산업진흥원, 아시아경제 주관 ‘4차산업 SW기초역량 아카데미’ 빅데이터 특화 분야 최종 프로젝트 최우수상 

### 프로젝트 핵심
취준생이 본인이 보유한 기술(ex. Java, C++)을 입력하면

그에 적합한 1)직무와 2)해당 직무의 공고를 추천해주는 서비스를 만들었습니다. 

또 가치관(ex. 워라밸, 복지)을 입력하면

앞서 기술 기반으로 추천된 직무와 공고 5개가 
그 안에서 순서가 바뀌도록 했습니다.

#### 1. 데이터 수집
    1) 출처 : Jobplanet  
       내용 : a) IT 직군 2021.01.25 기준 채용중인 공고 1882개
              b) IT기업 재직자의 평가 데이터(가치관)                       
    2) 수집 방법
             •크롤링(Selenium 라이브러리 사용)

#### 2. 전처리 (기술 용어 사전)
      1)필요성
        추천시스템 구현에 앞서, 각 직무 별로 요구하는 기술을 추출하기 위하여 
        기술 용어를 카테고리별로 표준화한 사전이 필요했습니다. 
        따라서, 먼저 크롤링한 채용 공고를 바탕으로 기술 사전 제작을 진행했습니다. 
        해당 사전을 기반으로 다시 공고에서 직무-기술 행렬, 공고-기술 행렬을 추출하였습니다. 
        이 두 행렬은 추천시스템에서 사용자가 입력한 기술과 코사인 유사도로 비교됩니다.
      2)사전 제작과정
           •전처리 규칙 설정 (어미, 조사, 특수문자 제외 처리/특정 규칙 단어 추출)
           •전처리 규칙 및 유사 단어 추출 함수화
           •결과값 검토 후, 불용어 추가
           •35개 이상 카운팅된 단어만 추출
           
#### 3. 직무/공고 추천시스템 구현
       •	Sklearn 패키지의 CountVectorizer() 함수를 사용해서 
            18개 직무-70개 기술 행렬, 1882개 공고- 70개 기술 행렬을 추출했습니다 
       •	사용자가 입력한 보유 기술과 위 두 행렬의 기술 간의 유사도를 Cosine_Similarity()를 통해 측정 
       •	직무와 공고를 5개씩 추천, 이후 최종 추천된 공고 내에서 가치관(잡플래닛 기업평가 데이터)을 기반으로 순위 조정.
#### 4. 기대효과                                                              
       IT직군 취준생은 추천 받은 직무/공고를 통해 선택과 집중 가능.
           
