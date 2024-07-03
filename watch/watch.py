import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern=r"https?://(?:www\.)?youtube\.com/embed/(\w+)"
    
    link=re.search(pattern,s)
    if link:
        return f"https://youtu.be/{link.group(1)}"
    return None





if __name__ == "__main__":
    main()