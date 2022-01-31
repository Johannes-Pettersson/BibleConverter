with open('in.txt', encoding='utf-8') as i:
    text = i.read()

for element in text:
    try:
        num = int(element)
    except:
        print(element)
    else:
        print("nummer")

