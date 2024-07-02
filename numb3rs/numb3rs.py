import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # pattern = r"^([0-1]{1}[0-9]{2}|[2]{1}[0-5]{2})\.([0-1]{1}[0-9]{2}|[2]{1}[0-5]{2})\.([0-1]{1}[0-9]{2}|[2]{1}[0-5]{2})\.([0-1]{1}[0-9]{2}|[2]{1}[0-5]{2})$"
    pattern = r"^([0-1]?[0-9]?[0-9]{1}|[2]{1}[0-5]{2})\.([0-1]?[0-9]?[0-9]{1}|[2]{1}[0-5]{2})\.([0-1]?[0-9]?[0-9]{1}|[2]{1}[0-5]{2})\.([0-1]?[0-9]?[0-9]{1}|[2]{1}[0-5]{2})$"
    match = re.search(pattern, ip)
    if match:
        return True
    else:
        return False


...


if __name__ == "__main__":
    main()
