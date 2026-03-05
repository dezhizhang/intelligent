class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return f"{self.year}-{self.month}-{self.day}"

    @classmethod
    def from_string(cls, date_str):
        year, month, day = tuple(date_str.split("-"))
        return cls(int(year), int(month), int(day))


if __name__ == "__main__":
    # day = Date(2021, 12, 31)

    new_date = Date.from_string("2018-12-31")
    print(new_date)
