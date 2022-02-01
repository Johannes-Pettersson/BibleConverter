with open('in.txt', encoding='utf-8') as i:
    text = i.read()

num1 = "0"
num2 = "0"
bokprint = False

#bara kapitel kvar att lägga in

with open('out.txt', 'w') as o:

    o.write('<?xml version="1.0" encoding="ISO-8859-1"?><bible>')

    for element in text:

        if element == "%":
            bokprint = True
            o.write('<b n="')
            continue
        elif element == "/":
            bokprint = False
            o.write('">')
            continue
        if bokprint:
            o.write(element)
        else:
            #printing chapter
            try:
                int(element)
            except:
                if num1 == "1":
                    o.write('<v n="' + num1 + '">')
                    o.write(element)
                    num1 = "0"
                elif num1 != "0":
                    o.write('</v><v n="' + num1 + '">')
                    o.write(element)
                    num1 = "0"
                else:
                    o.write(element)
            else:
                if num1 == "0":
                    num1 = element
                else:
                    o.write('</v><v n="' + num1 + element + '">')
                    num1 = "0"

    o.write('</b></v></bible>')