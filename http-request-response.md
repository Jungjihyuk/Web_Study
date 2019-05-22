## 웹 

> World Wide Web의 줄임말로 인터넷 상에서 이루어지는 서비스 중 하나로써, 공유 목적으로 개발되었다

Web: [naver blog](https://m.blog.naver.com/PostView.nhn?blogId=hot1455&logNo=60124258172&proxyReferer=https%3A%2F%2Fwww.google.com%2F)
<br>
## HTTP

> 웹 상에서 정보를 주고받을 수 있는 프로토콜, 이때 정보는 보통 HTML문서나, 이미지, 영상 등을 포함합니다  

HTTP: [MDN](https://developer.mozilla.org/ko/docs/Web/HTTP/Overview)
<br>
HTTP란? : [zerocho](https://www.zerocho.com/category/HTTP/post/5b344f3af94472001b17f2da)<br>

### HTTP protocol 특징 

Statusless | Connectless 
--------|-------
HTTP 프로토콜은 상태가 없다 | HTTP 프로토콜은 상태에 대한 지속적인 연결이 없다
이전에 했던 작업, 지금한 작업에 대한 정보를 갖고 있지 않다 | 웹 브라우저의 요청에 대한 응답을 하면 클라이언트와의 접속이 끊긴다


<span style="color: orange">연결이 계속되어 있으면 좋을텐데 왜 귀찮게 비연결방식으로 하고 쿠키라는 방식으로 저장을하는거야?</span><br>

```
HTTP는 인터넷 상에서 불특정 다수의 통신환경을 기반으로 설계되었다는 점이 포인트입니다
만약 불특정 다수의 클라이언트와 Google이라는 하나의 서버가 지속적으로 연결을 유지한다면 
많은 리소스가 발생하게 됩니다. 따라서 리소스 낭비를 줄여 더 많은 연결을 위해 비연결 지향으로 설계하게 된 것입니다
```

<span style="color: orange">많은 클라이언트와의 연결이 원활해지는 장점이 있다면 비연결 지향으로 생기는 단점도 있지 않을까?</span><br>

```
첫번째로 위에서 언급했듯이 쿠키라는 것을 따로 두고 클라이언트 정보를 임시로 저장하는 방법을 채용해야한다
그리고 두번째로 동일한 클라이언트의 모든 요청에 대해, 매번 새로운 연결시도/해제의 과정을 거쳐야 하므로
연결/해제에 대한 오버헤드가 발생한다는 단점이 있습니다

이에 대한 해결책으로 HTTP연결을 새로 생성할 때마다 발생되는 오버헤드를 줄이기 위해 
HTTP 1.1 부터 지원하는 기능인 KeepAlive 속성을 사용할 수 있습니다

그러나 KeepAlive 속성을 on상태로 바꾼다 해도, 서버가 나쁜 환경에서는 프로세스수가 기하급수적으로 늘어나기 때문에 
메모리를 많이 사용하게 되므로 주의해야 합니다 
```

HTTP Protocol : [tistory1](https://codedragon.tistory.com/5930), &nbsp; [tistory2](https://victorydntmd.tistory.com/286)

### Cookie 

> HTTP의 특성인 Connectless, Stateless의 문제점을 보완한 것이 바로 Cookie! 

Connectionless로 인해 서버는 클라이언트의 요청에 대한 응답을 한 후 연결을 끊기 때문에 <br>
다른 페이지로 이동하고 싶을 경우 서버에 재요청을 해야합니다. <br>
재요청시 서버는 클라이언트를 식별할 수가 없는 Stateless특징이 있기 때문에 <br>
같은 브라우저에서 요청을해도 서버는 같은 브라우저인지 알 수가 없고, 로그인과 같이 <br>
서버가 클라이언트를 기억해야 할 경우에 클라이언트 정보를 저장하지 못한다면  <br>
페이지 이동시을 하거나 리로딩같은 재요쳥을 하는 경우에 계속해서 로그인을 해야 하는 불편함이 있습니다.<br>

<span style="background-color:orange">이러한 불편함을 해결하기 위해 쿠키라는 것을 저장해서 서버가 클라이언트를 식별할 수 잇도록 합니다</span><br>

쿠키는 서버에서 생성하여, 클라이언트에서 보낸 특정 정보를 저장합니다. <br>
그리고 쿠키의 속성값은 서버에 요청할 때마다 참조 또는 변경하여 데이터 상태를 관리합니다.<br>

![cookie](https://user-images.githubusercontent.com/33630505/58149184-c5fdd580-7c9c-11e9-8371-4ad522105f38.JPG)

cookie : [github blog](https://nesoy.github.io/articles/2017-03/Session-Cookie)

### Session

> Cookie의 단점을 보완하기 위해 생긴 Session! Session은 서버단에서 사용자 정보를 기록할 수 있는 방법입니다 


#### Session?
HTTP session id를 식별자로 구별하여 데이터를 사용자의 브라우저에 쿠키형태가 아닌 접속한 DB에 정보를 저장합니다 <br>
클라이언트는 HTTP session id를 쿠키로 메모리 저장된 형태로 가지고 있습니다<br>
메모리에 저장하기 때문에 브라우저가 종료되면 사라지게 됩니다<br>

#### Session 절차 

```
1. 클라이언트가 서버에 Resource를 요청합니다 
2. 서버에서는 HTTP Request를 통해 쿠키에서 Session id를 확인 후 
   없으면 set-cookie를 통해 새로 발행한 session-id를 보냅니다
3. 새로 부여 받은 session-id를 클라이언트 쪽에서 HTTP request에 포함하여 원하는 
   Resource를 요청합니다
4. 서버는 session id를 통해 해당 세션을 찾아 클라이언트 상태 정보를 유지하며 
   적절한 응답을 합니다 
```

<span style="color: orange">뭐야 쿠키만 있음되지 세션은 또 뭐야?</span><br>

```
쿠키에 대한 정보를 HTTP Header에 추가하여 보내기 때문에 상당한 트래픽을 발생시키는 문제가 있습니다
또한 결제정보, 개인정보등을 쿠키에 저장했을때 쿠키가 유출되면 보안에 문제가 발생할 수도 있습니다

따라서 클라이언트측에 저장하는것이 아니라 서버 DB에 저장하는 방법을 사용해서 문제를 해결! 
```

![session](https://user-images.githubusercontent.com/33630505/58149406-c8146400-7c9d-11e9-9554-fa047a4bb388.JPG)

### Token

> 세션은 서버의 메모리를 차지하고 있기 때문에 동시 접속자 수가 많은 웹 사이트일 경우 서버 과부화의 원인이 되고, 세션 정보가 중간에 탈취 당할 수도 있기 때문에 완벽하다고 볼수는 없습니다. 그래서 쿠키와 세션의 문제점을 보완하기 위해 Token(토큰) 인증 방식 도입! 

<span style="background-color:orange">Token 인증방식은 보호할 데이터를 토큰으로 치환하여 원본 데이터 대신 토큰을 사용하는 기술</span><br>
```
토큰 방식 이외에 어떤 새로운 기술이 또 생길지 모릅니다 
그렇지만 현존하는 기술중 Token 방식이 가장 안전하다고해서 무조건 Token 방식을 써야 하는 가? 
꼭 그렇지만은 않아 보인다. 어떤 웹 서버를 운영할 것인가에 따라 해당 서버를 이용할 이용자의 숫자에 따라 
어떤 서비스를 제공할 것이냐에 따라 적절하게 사용해야 한다고 봅니다 
```

### HTTPs 

![https](https://user-images.githubusercontent.com/33630505/58152246-02ceca00-7ca7-11e9-8d2e-7c9ee23fcfb1.JPG)


HTTPS: [tistory](https://sjh836.tistory.com/81)

### HTTP message

**서버와 클라이언트가 HTTP 통신을 할때 주고 받는 메시지** <br>

```
클라이언트 --> 서버 : Request Message 
서버 --> 클라이언트 : Response Message 
```

#### Request Message

![request message](https://user-images.githubusercontent.com/33630505/57967936-59828e00-799f-11e9-8673-cbdb4db516ae.JPG)

```
요청라인: url 
         HTTP Method 
         protocol version 
요청헤더: User-Agent(브라우저) 
         Accept(수신되는 데이터중 브라우저가 처리가능한 데이터 타입) 
         Cookie(유저 정보 임시 기억)
         Host(요청 도메인 정보) 
         Referer(현재 페이지 접속 전 어느 사이트 경유했는지에 대한 정보) 
         Connection     # ex) keep-alive
공백라인
메시지 본문
```

#### Response Message 

![response message](https://user-images.githubusercontent.com/33630505/57968025-31dff580-79a0-11e9-9a83-0db6cd09117d.JPG)

```
상태라인: HTTP version 
         Status code 
         Reason-phrase 
응답헤더: Date  
         Server           # ex) Apache
         Last-Modified
         Content-Encoding
         Content-Length
         Content-Type     # ex) text/html; charset=utf-8
공백라인
메시지 본문
```

### HTTP Request method 

Request Method | Explanation 
--------|-------
Get | 요청라인을 통해 자원 요청(url에 데이터 표시)
Post | 메시지 본문을 통해서 자원 요청(url에서 데이터 숨김)
Put | URL에서 자원을 생성 
Delete | URL에서 자원을 삭제 
Options | 응답 가능한 HTTP Method 요청 
Head | HTTP Header 정보만 수신 
Trace | Request의 loop back 테스트 
Connect | 터널링의 목적으로 연결 요청 


### Client, Server 

![clientserver](https://user-images.githubusercontent.com/33630505/57967447-1114a180-799a-11e9-94d3-d0826dd1700e.JPG)

클라이언트(Request)  --->  서버(Response) <br>
브라우저에서 문서확인 <---  문서(요청에 대한 응답) ex) html, json, jpg... 


### HTTP Status 

```
200 (OK): 성공적인 응답, 오류 없이 전송 성공 
201 (Created): 요청이 성공적으로 처리되어 리소스가 만들어졌음을 의미 
202 (Accepted): 요청이 받아들여졌지만 처리되지 않았음을 의미 
301 (Moved Permanently): 영구적으로 컨텐츠가 이동했을때 
304 (Not Modified): 브라우저에 캐시되어 있는 버전을 쓴다 
400 (Bad Request): 요청 자체가 잘못 되었을때 사용하는 코드 
401 (Unauthorized): 인증이 필요한 리소스에 인증 없이 접근할 경우 발생 
403 (Forbidden): 서버가 요청을 거부할때 발생. 관리자에 의해 사용자를 차단했거나 서버에 index.html이 없는 경우 발생 
404 (Not Found): 에러는 파일의 확장자가 제대로 입력이 되지 않았거나 주소를 잘못 쳤을 경우(존재하지 않는 url 요청을 했을 경우) 발생하는 에러이다
408 (Request Timeout): 요청 중 시간이 초과되었을때 사용하는 코드 
500 (Internal Server Error): 요청한 주소의 서버에 관리상 문제가 있을 경우 발생하는 에러, 서버측 파일에 소스코드 자체에 오류가 있을 경우 즉, 컴파일이 불가능한 경우에 발생할 수 있다 
503 (Service Temporarily Unavailable): 서버를 현재 일시적으로 사용할 수 없을 때 발생, 유지보수중이거나 서버가 터졌을 때 발생
```
