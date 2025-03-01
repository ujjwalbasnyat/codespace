import inflect
import datetime
p = inflect.engine()
import sys

class Student:
    def __init__(self, till_day):
        self.till_day = till_day
        print(self.till_day)

    
    @classmethod
    def get(cls):
        bday = input("Date of Birth: ")
        if not "-" in bday:
            return "Invalid date"
        year, months, day = bday.split("-")
        year, months, day = int(year), int(months), int(day)
        bday = datetime.date(year, months, day)
        tday=  datetime.date.today()
        till_day = (tday - bday)*24
        wday = p.number_to_words(till_day.days)
        wday = wday.replace(" and ", " ") + " minutes"
        return wday


def main():
    print(Student.get())
    sys.exit()

main()