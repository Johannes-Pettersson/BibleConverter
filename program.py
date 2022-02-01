with open('in.txt', encoding='utf-8') as i:
    text = i.read()

num1 = "0"
num2 = "0"

for element in text:

    #printing chapter
    try:
        int(element)
    except:
        if num1 == "1":
            print('<v n="' + num1 + '">')
            print(element)
            num1 = "0"
        elif num1 != "0":
            print('</v><v n="' + num1 + '">')
            print(element)
            num1 = "0"
        else:
            print(element)
    else:
        if num1 == "0":
            num1 = element
        else:
            print('</v><v n="' + num1 + element + '">')
            num1 = "0"
        




        

