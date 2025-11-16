class Car:
    def run(self):
        print(f"汽车在跑...")

    def work(self):
        print(f"汽车在工作")
        self.run()


car = Car()
car.work()
