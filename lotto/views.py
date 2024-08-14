from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return (render(request, 'lotto/default.html',{}))
    # 유저의 요청을 넘겨주면서 어떤 html보여줄지
    # {}는 예측된 결과물을 같이 꽂아서 뒤에 넘겨줌



    #<input type="text" name="name"></name>
    # user가 인풋에 입력한 name이라는 이름을 가진 태그값 생성
    # user_input_name = request.POST['name'] # name이란 이름을 가진 태그의 값을 받아옴
    # user_input_text = request.POST['text']
    # # 하나의 행을 생성
    # new_row = GuessNumbers(name=user_input_name, text=user_input_text)
    # new_row.name = new_row.name.upper()
    # new_row.generate()

    # new_row.save()
    # return HttpResponse('<h1>Hello, world!</h1>')

def hello(request) :
    return HttpResponse("<h1 style='color:red;'>Hello, world!</h1>")