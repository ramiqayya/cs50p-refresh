from datetime import date
import inflect
import sys


def main():
    p = inflect.engine()
    bd = input("Date of Birth: ")
    try:
        birthday = get_birthday(bd)
    except ValueError:
        sys.exit("Invalid date")
        
    minutes = age_minutes(birthday)
    words = p.number_to_words(minutes)
    print(f"{words} minutes")


def get_birthday(bd):
    
    return date.fromisoformat(bd)
  


def age_minutes(bd1):
    delta_days = date.today().__sub__(bd1).days
    delta_minutes = delta_days * 24 * 60
    return delta_minutes


if __name__ == "__main__":
    main()
