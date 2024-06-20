def main():
   before= input()
   print((convert(before)))


def convert(x):
   y=x.replace(':)','🙂')
   z=y.replace(':(','🙁')
   return z

main()