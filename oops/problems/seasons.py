import inflect
from datetime import date
import sys


def get_minutes(dob_str):

    try:
        dob = date.fromisoformat(dob_str)
        today = date.today()
        if dob > today:
            sys.exit("Invalid date")
        days_diff = (today-dob).days
        return days_diff*1440
    except ValueError:
        sys.exit("Invalid date")

def main():
    dob_str = input("Date of Birth: ")
    minutes = get_minutes(dob_str)
    if minutes is not None:
        p = inflect.engine()
        minutes_words = p.number_to_words(minutes, andword ="")
        print(minutes_words, "minutes")

main()
