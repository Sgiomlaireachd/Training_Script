def getInfo():
    with open('./previous.txt','r') as out_file:
        text = out_file.read()
        text = text.split()
        print('**Previous training**')
        if len(text) > 0:
            print('--> Level:',text[0])
            print('--> Week:',text[1])
        else:
            print('--> Have not trained before')

def setInfo(lvl,week):
    with open('./previous.txt','w') as in_file:
        in_file.write(lvl + ' ' + str(week))

if __name__ == "__main__": getInfo()


