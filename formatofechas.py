from datetime import datetime

def main():
    hoy = datetime.now()
    print(hoy.strftime("%Y"))
    print(hoy.strftime("%d"))
    print(hoy.strftime("%A"))


    print(hoy.strftime("%a, %d %B %Y"))

    print("=============================")

    print(hoy.strftime())

if __name__ == "__main__":
    main()