#과제 1번
class FourCal:
    add_num=0
    sub_num=0
    div_num=0
    mul_num=0
    def __init__(self, name, age, school):
        self.name=name
        self.age=age
        self.school=school

    def add(self, n1,n2):
        self.add_num+=1
        result=n1+n2
        return result
    def sub(self,n1,n2):
        self.sub_num+=1
        result=n1-n2
        return result
    def div(self,n1,n2):
        self.div_num+=1
        if (n2 == 0):
            print("0으로 나눌 수 없습니다")
            return None
        result=n1/n2
        return result
    def mul(self,n1,n2):
        self.mul_num+=1
        result=n1*n2
        return result
    def ShowCount(self):
        print (f'덧셈 : {self.add_num}\n뺄셈 : {self.sub_num}\n곱셈 : {self.mul_num}\n나눗셈 : {self.div_num}')

cal=FourCal("김보경",23,"korea")
cal.add(1,4)
cal.sub(9,1)
cal.mul(9,1)
cal.mul(2,7)

cal.ShowCount()