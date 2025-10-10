

class Phone:

    __current_voltage = 1

    def __keep_single_core(self):
        print("单核cpu运行模式")

    def call_by_5g(self):
        if self.__current_voltage >=1:
            print("5g通话已开启")
        else:
            self.__keep_single_core()
            print("电量不足，无法使用5g通话")

phone = Phone()
phone.call_by_5g()
