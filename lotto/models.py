from django.db import models
from django.utils import timezone
import random
# Create your models here.

class GuessNumbers(models.Model) :
    # models안에 있는 클래스 사용
    name = models.CharField(max_length = 24) # 문자열 저장 데이터
    text = models.CharField(max_length=255) # 문자열 저장 데이터 (로또의 설명)
    lottos = models.CharField(max_length=255, default="[1,2,3,4,5,6]") # 문자열 데이터 (로또 번호 담길 리스트) 
    num_lotto = models.IntegerField(default=5) # 숫자 데이터 (개수 6)
    update_date = models.DateTimeField() # 날짜 데이터

    def generate(self) :
        self.lottos = ""
        origin = list(range(1,46))
        # 번호 6개 set 개수 만큼 1-46 섞은 후 6개 골라서 sort
        for _ in range(0,self.num_lotto) :
            random.shuffle(origin)
            guess = origin[:6]
            guess.sort()
            self.lottos += str(guess) + '\n'

        self.update_date = timezone.now()
        # db 저장
        self.save()

    def _str_(self) :
        return "pk {} : {} - {}".format(self.pk, self.name, self.text)

# class Cage(Box) :
#     def _str_(self) :
#         return 'Cage 객체변수'

# cage_1 = Cage()
# print(cage_1)