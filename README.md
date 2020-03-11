# Laundry Delivery
***
## 1. 개요<br>
세탁 대행 어플리케이션을 서비스 하기 위해 Back-End를 설계하였다.
Model은 각종 배달 어플리케이션들의 서비스 방식을 참고 하였으며, Front-End 개발자와 협업을 위해 다양한 프레임워크를 사용하였다.
***
## 2. 구현 <br>
***
### 2-1. Django <br>
<pre><code>$ python --version
Python 3.7.4
</code></pre>
<pre><code>$ python -m django --version
3.0
</code></pre>
***
### 2-2. Django REST Framework
Front 개발자에게 정보를 전달하기 위한 방법으로 사용
<pre><code>$ pip show djangorestframework
Name: djangorestframework
Version: 3.10.3
</code></pre>
***
### 2-3. ngrok
외부에서 로컬에 접속 가능하게 하기 위해 사용한 터널 프로그램


<pre><code>ngrok by @inconshreveable                                                                               (Ctrl+C to quit)

Session Status                online
Session Expires               7 hours, 59 minutes
Version                       2.3.35
Region                        United States (us)
Web Interface                 http://127.0.0.1:4040
Forwarding                    http://e23b73bc.ngrok.io -> http://localhost:8000
Forwarding                    https://e23b73bc.ngrok.io -> http://localhost:8000
Connections                   ttl     opn     rt1     rt5     p50     p90                                                                                              0       0       0.00    0.00    0.00    0.00 
</code></pre>
***
### 2-4. Postman<br>
개발한 API를 테스트하기위해 사용한 GUI기반 플랫폼<br>
<img height=100 src="https://media-exp1.licdn.com/dms/image/C560BAQFF6NsJiRfdIQ/company-logo_200_200/0?e=2159024400&v=beta&t=__Uf6QioRE6C4_4JHyT7XZe0c3fKGmkZP8_M75ELB5k">

