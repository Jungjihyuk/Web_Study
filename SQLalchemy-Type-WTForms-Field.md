# 2019-05-23 2nd

## SQLalchemy

> SQLarlchemy는 Python 언어를 위한 ORM이다. 
SQL문법을 사용하지 않고 Python class로 스키마를 작성하면 Create table을 한것 처럼 DB table을 생성해준다. 


### Type 

#### SQLarlchemy 일반 데이터 타입 

1. 정수형 
- BigInteger 
- SmallInteger 
- Integer  
2. 실수형 
- Float 
3. 논리형 
- Boolean
4. 문자형 
- String
- Text 
- Unicode : 유니코드
- UnicodeText : 
5. 기간형(시간, 날짜)
- Date  : yyyy.mm.dd
- DateTime : Date + Time
- Time : hh:mm:ss
- Interval : 기간
6. 열거형 
- Enum 
7. 이진데이터형
- LargeBinary
8. MatchType
9. Numeric 

#### 타사의 데이터 타입 

1. 정수형 
- Integer
- Int
- BigInt
- SmallInt
2. 실수형
- Float
- Real 
3. 문자형 
- Char : 고정 문자열
- Varchar : 가변 문자열(메모리를 효율적으로 사용할 수 있다) 
- ex) varchar(10)일 때 test를 저장하면 4byte 영역만 차지한다
- nChar : 고정 문자열 + 유니코드 문자열 (char의 2배공간 사용)
- nVarchar : 가변 문자열 + 유니코드 문자열
4. 이진데이터형
- Binary
- VarBinary
5. 기간형(시간,날짜)
- Date
- DateTime
- TimeStamp
6. 파일형 
- BLOB
- CLOB
- JSON
7. 리스트형(배열)
- Array


## WTForms

> 클라이언트로부터 입력받을 Form을 제공하는 API. 
필드의 정의, 유효성 검사, 입력 가져오기, 오류 집계를 포함하는 기능을 제공한다.

### Field

> 일반적으로 데이터베이스 테이블에서 타입을 지정해주는 열을 말한다.
입력 받는 값의 타입.


### 기본 필드 

1. 숫자 필드
- FloatField : 실수를 받는 필드
- IntegerField : 정수를 받는 필드

2. 문자 필드
- StringField : 문자열을 받는 필드

3. 논리형 필드
- BooleanField : True, False를 받는 필드

4. 파일 필드
- FileField : 파일을 받는 필드
- MutipleFileField : 여러 파일을 받을 수 있는 필드

5. 날짜 필드
- DateField : 날짜를 받는 필드
- DatetimeField : 날짜, 시간을 같이 받는 필드

6. 선택형 필드
- RadioField : SelectField와 비슷하지만, 라디오 버튼을의 목록을 보여준다.
- SelectField : 값과 레이블로 이루어진 선택들을 쌍으로 가진다. 값은 어떤것이 와도 된다.
- SelectMultipleField : SelectField와 같지만 여러 선택을 가질 수 있다.

7. 버튼형 필드 
- SubmitField : Submit 버튼이 눌리는 것을 체크하는 필드

8. DecimalField 


### 편리한 필드
HiddenField : 입력 폼이 보이지 않는 필드 
PasswordField : 비밀번호를 입력할때 값이 보이지 않도록 하는 필드
TextAreaField : 텍스트를 자유롭고 길게 받을 수 있는 필드

### Field Enclosures
FormField : Form을 받는 필드
FieldList : 필드의 인스턴스를 list형태로 받는 필드 

### 커스텀 필드
필요시 직접 필드를 수정해서 사용한다 
