class Phone:
    IMEI = None
    producer = 'shuqin'

    def call_by_5g(self):
        print("父类的5g网络进行通话")

class MyPhone(Phone):
    producer = "shuqin.ai"
    def call_by_5g(self):
        print("子类的5g网络通话")


myPhone = MyPhone()
myPhone.call_by_5g()
print(myPhone.producer)
