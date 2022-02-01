with open('in.txt', encoding='utf-8') as i:
    text = i.read()

num1 = "?"
num2 = "?"
num3 = "?"
num4 = "?"
num5 = "?"
bookPrint = False
chapterPrint = False
firstBook = True
firstChapter = True
verseNum = 0



with open('out.txt', 'w') as o:

    o.write('<?xml version="1.0" encoding="ISO-8859-1"?><bible>')

    for element in text:

        if element == "%" and bookPrint == False and firstBook:
            bookPrint = True
            firstBook=False
            verseNum = 0
            o.write('<b n="')
            continue
        elif element == "%" and bookPrint == False:
            bookPrint = True
            verseNum = 0
            firstChapter = True
            o.write('</v></c></b><b n="')
            continue
        elif element == "%" and bookPrint == True:
            bookPrint = False
            o.write('">')
            continue
        elif element == "'" and chapterPrint == False and firstChapter:
            chapterPrint = True
            firstChapter=False
            verseNum = 0
            o.write('<c n="')
            continue
        elif element == "'" and chapterPrint == False:
            chapterPrint = True
            verseNum = 0
            o.write('</v></c><c n="')
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
            #printing verse
            try:
                int(element)
            except:
                
                if (num5 != "?"):
                    o.write(num1 + num2 + num3 + num4 + num5)
                    o.write(element)
                    num1 = "?"
                    num2 = "?"
                    num3 = "?"
                    num4 = "?"
                    num5 = "?"
                elif (num4 != "?"):
                    o.write(num1 + num2 + num3 + num4)
                    o.write(element)
                    num1 = "?"
                    num2 = "?"
                    num3 = "?"
                    num4 = "?"
                    num5 = "?"
                elif (num3 != "?"):
                    o.write(num1 + num2 + num3)
                    o.write(element)
                    num1 = "?"
                    num2 = "?"
                    num3 = "?"
                    num4 = "?"
                    num5 = "?"
                elif (num2 != "?"):
                    if(int(num1 + num2) == verseNum + 1):
                        o.write('</v><v n="' + num1 + num2 + '">')
                        o.write(element)
                        verseNum = verseNum + 1
                        num1 = "?"
                        num2 = "?"
                        num3 = "?"
                        num4 = "?"
                        num5 = "?"
                    else:
                        o.write(num1 + num2)
                        o.write(element)
                        num1 = "?"
                        num2 = "?"
                        num3 = "?"
                        num4 = "?"
                        num5 = "?"
                elif(num1 != "?"):
                    if(int(num1) == verseNum + 1):
                        o.write('</v><v n="' + num1 + '">')
                        o.write(element)
                        verseNum = verseNum + 1
                        num1 = "?"
                        num2 = "?"
                        num3 = "?"
                        num4 = "?"
                        num5 = "?"
                    else:
                        o.write(num1)
                        o.write(element)
                        num1 = "?"
                        num2 = "?"
                        num3 = "?"
                        num4 = "?"
                        num5 = "?"
                else:
                    o.write(element)

            else:
                if num1 == "?":
                    num1 = element
                elif num1 != "?" and num2 == "?":
                    num2 = element
                elif num1 != "?" and num2 != "?" and num3 == "?":
                    num3 = element
                elif num1 != "?" and num2 != "?" and num3 != "?" and num4 == "?":
                    num4 = element
                elif num1 != "?" and num2 != "?" and num3 != "?" and num4 != "?" and num5 == "?":
                    num5 = element
                
    o.write('</v></c></b></bible>')

num1 = "?"
num2 = "?"
num3 = "?"
num4 = "?"
num5 = "?"