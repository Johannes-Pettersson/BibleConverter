with open('in.txt', encoding='utf-8') as i:
    text = i.read()

num1 = "0"
num2 = "0"
bookPrint = False
chapterPrint = False
firstBook = True
firstChapter = True


#behöver lägga in bokslutstagg efter varje bok

with open('out.txt', 'w') as o:

    o.write('<?xml version="1.0" encoding="ISO-8859-1"?><bible>')

    for element in text:

        if element == "%" and bookPrint == False and firstBook:
            bookPrint = True
            firstBook=False
            o.write('<b n="')
            continue
        elif element == "%" and bookPrint == False:
            bookPrint = True
            o.write('</b><b n="')
            continue
        elif element == "%" and bookPrint == True:
            bookPrint = False
            o.write('">')
            continue
        elif element == "'" and chapterPrint == False and firstChapter:
            chapterPrint = True
            firstChapter=False
            o.write('<c n="')
            continue
        elif element == "'" and chapterPrint == False:
            chapterPrint = True
            o.write('</c><c n="')
            continue
        elif element == "'" and chapterPrint == True:
            chapterPrint = False
            o.write('">')
            continue

        if bookPrint:
            o.write(element)
        elif chapterPrint:
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

    o.write('</v></c></b></bible>')