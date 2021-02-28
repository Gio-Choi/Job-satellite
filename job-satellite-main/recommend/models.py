from django.db import models
# 공고모델 공고정보 pk

# 회사모델

# 직무 스킬 통계
# 스킬 id 매핑 테이블


# 다른테이블 속성가져와야하는 클래스는 Model-> Foreign으로 바꾸기
# recruit_info에 포린키 추가함
# jobid는 어떻게?


class recruit_info(models.Model):
    jobId = models.IntegerField(primary_key=True)
    company = models.CharField(max_length=50)
    title = models.CharField(max_length=300)
    job = models.CharField(max_length=300)
    region = models.CharField(max_length=50)
    jobUrl = models.CharField(max_length=1000)
    total_skill = models.CharField(max_length=300)
    total_skill_literal = models.CharField(max_length=300)
    reviewCount = models.IntegerField(default=0)
    average = models.FloatField(default=0)
    salary = models.FloatField(default=0)
    wlb = models.FloatField(default=0)
    culture = models.FloatField(default=0)
    possibility = models.FloatField(default=0)
    management = models.FloatField(default=0)


class company(models.Model):
    companyId = models.IntegerField(primary_key=True, default=0)
    company_name = models.CharField(max_length=30, default='', null=True)
    reviewCount = models.IntegerField(default=0)
    average = models.FloatField(default=0)
    salary = models.FloatField(default=0)
    wlb = models.FloatField(default=0)
    culture = models.FloatField(default=0)
    possibility = models.FloatField(default=0)
    management = models.FloatField(default=0)

# jobdict db저장 완료


class jobdict(models.Model):
    job = models.CharField(max_length=50, primary_key=True, unique=True)
    skill = models.CharField(max_length=100, default='')

# mainpage에 쓰일 스킬 대분류소분류 테이블 필요하면 엑셀에 정리해서 모델링
# 작업하고 사용하기


class skill(models.Model):
    needSkill = models.CharField(max_length=50, primary_key=True)
    web = models.IntegerField(default=0)
    network = models.IntegerField(default=0)
    se = models.IntegerField(default=0)
    soft = models.IntegerField(default=0)
    qa = models.IntegerField(default=0)
    plan = models.IntegerField(default=0)
    da = models.IntegerField(default=0)
    app = models.IntegerField(default=0)
    pm = models.IntegerField(default=0)
    game = models.IntegerField(default=0)
    dba = models.IntegerField(default=0)
    consulting = models.IntegerField(default=0)
    he = models.IntegerField(default=0)
    cd = models.IntegerField(default=0)
    gd = models.IntegerField(default=0)
    ad = models.IntegerField(default=0)
    marketing = models.IntegerField(default=0)
    market = models.IntegerField(default=0)
    sa = models.IntegerField(default=0)
    wp = models.IntegerField(default=0)
    ud = models.IntegerField(default=0)
    md = models.IntegerField(default=0)
    strategy = models.IntegerField(default=0)
    advertise = models.IntegerField(default=0)
    video = models.IntegerField(default=0)
    sales = models.IntegerField(default=0)
    support = models.IntegerField(default=0)
    erp = models.IntegerField(default=0)
    iu = models.IntegerField(default=0)
    wd = models.IntegerField(default=0)
    machine = models.IntegerField(default=0)
    esemi = models.IntegerField(default=0)
    control = models.IntegerField(default=0)
    elec = models.IntegerField(default=0)
    dsemi = models.IntegerField(default=0)
    econtrol = models.IntegerField(default=0)
    domsales = models.IntegerField(default=0)
    sound = models.IntegerField(default=0)
    itsol = models.IntegerField(default=0)
    emarketing = models.IntegerField(default=0)
    smarketing = models.IntegerField(default=0)
    bd = models.IntegerField(default=0)
    bmarketing = models.IntegerField(default=0)
    publish = models.IntegerField(default=0)
    pd = models.IntegerField(default=0)
    cs = models.IntegerField(default=0)
    culture = models.IntegerField(default=0)
    crm = models.IntegerField(default=0)
    maintenance = models.IntegerField(default=0)
    tech = models.IntegerField(default=0)
    product = models.IntegerField(default=0)
# col=index,jobid,company,title,job,skill,region,experience,intro
# task,require,prefer,jobUrl


class test(models.Model):
    titleId = models.IntegerField(default=0)
    company = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    job = models.CharField(max_length=50)
    skill = models.CharField(max_length=50)
