
class Phone:
    imei = None
    producer = None

    def call_by_4g(self):
        print("4g通话")

class Phone2022(Phone):
    face_id = True

    def call_by_5g(self):
        print("2025最新5g通话")

phone2022 = Phone2022()
phone2022.call_by_4g()
phone2022.call_by_5g()
