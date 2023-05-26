from serializers.factory import Factory

Json = Factory.create_serializer(".json")
Xml = Factory.create_serializer(".xml")

while True:
    print("Select:")
    print('1) To get from json')
    print('2) To get from xml')
    print('3) Json to xml')
    print('4) Xml to json')

    ans = input("Choice:")
    ans = ans.replace(" ", "")
    match ans:
        case "1":
            fn = input('Input file name:\n')
            sourse = open(fn, "r")
            data = open("data.json", "w")
            Json.dump(sourse.read(), data)
            sourse.close()
            data.close()
        case "2":
            fn = input('Input file name:\n')
            sourse = open(fn, "r")
            data = open("data.xml", "w")
            Xml.dump(sourse.read(), data)
            sourse.close()
            data.close()
        case "3":
            xml = open("data.xml", "w")
            json = open("data.json", "r")
            obj = Json.load(json)
            Xml.dump(obj, xml)
            xml.close()
            json.close()
        case "4":
            xml = open("data.xml", "r")
            json = open("data.json", "w")
            obj = Xml.load(xml)
            Json.dump(obj, json)
            xml.close()
            json.close()
        case _:
            print('Invalid input. Try again')