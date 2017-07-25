from urllib.request import urlopen

def main():

    url = "http://devnodus.com"
    response = urlopen(url)

    print("El codigo de respuesta es: %s" % response.getcode())

    data = response.read()

    print(data)

    pass

if __name__ == '__main__':
    main()