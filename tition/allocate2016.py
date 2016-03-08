from random import randint

qntwenty = ["pQn3", "tQn1"]
qnten = ["pQn1", "pQn2", "tQn2", "tQn3", "tQn4"]

def allocateQn():
    name = input("What is your full name?: (Full name with capitalisation)")
    questions = []
    if name == "Alessandra Giam Mun Rong" or name == "Ching Hannie":
        coinflip = randint(0,1) # if 1, 1 20 marks question and 1 ten marks question. if 0, 3 10 marks questions
        if coinflip == 1:
            coinflip2 = randint(0,1)
            if coinflip2 == 1:
                questions.append("tQn1")
            else:
                questions.append("pQn3")
            questions.append(qnten[randint(1,4)]) # 0 excluded as they made question 1 (qnten[0])
        else:
            questions.append(qnten[randint(1,4)])
            while len(questions) != 3:
                toAppend = qnten[randint(1,4)]
                if toAppend in questions: # if the same question is chosen, rechoose
                    hi = ''
                else:
                    questions.append(toAppend)
                

    elif name == "Jasmine Seah Yong Yee" or name == "Metta Lim Fang Jun":
        coinflip = randint(0,1)
        if coinflip == 1:
            coinflip2 = randint(0,1)
            if coinflip2 == 1:
                questions.append("tQn1")
            else:
                questions.append("pQn3")
            while len(questions) != 3:
                question = randint(0,4)
                if question != 1: # 1 excluded as they made the question
                    questions.append(qnten[question])
        else:
            questions.append(qnten[randint(0,3)])
            while len(questions) != 3:
                question = randint(0,4)
                if qnten[question] in questions:
                    hi = ''
                else:
                    if question != 1:
                        questions.append(qnten[question])

    elif name == "Olivia Yu Wanzhi" or name == "Chan Heng Huat Jordan":
        coinflip = randint(0,1)
        if coinflip == 1:
            questions.append("tQn1") #pQn3 excluded as they made the question
            questions.append(qnten[randint(0,4)])
        else:
            questions.append(qnten[randint(0,4)])
            while len(questions) != 3:
                toAppend = qnten[randint(0,4)]
                if toAppend in questions:
                    hi = ''
                else:
                    questions.append(toAppend)

    elif name == "Chia Ding Heng Ryan" or name == "Chin Fu Rui Raymond" or name == "Dennis Ngin Cheong Jun":
        coinflip = randint(0,1)
        if coinflip == 1:
            questions.append("pQn3") #tQn1 excluded as they made the question
            questions.append(qnten[randint(0,4)])
        else:
            questions.append(qnten[randint(0,4)])
            while len(questions) != 3:
                toAppend = qnten[randint(0,4)]
                if toAppend in questions:
                    hi = ''
                else:
                    questions.append(toAppend)

    elif name == "Jovan Teo" or name == "Kua Weng Chew Ernest" or name == "Lee Yang Peng":
        coinflip = randint(0,1)
        if coinflip == 1:
            coinflip2 = randint(0,1)
            if coinflip2 == 1:
                questions.append("tQn1")
            else:
                questions.append("pQn3")
            while len(questions) != 3:
                question = randint(0,4)
                if question != 2: # 2 excluded as they made the question
                    questions.append(qnten[question])
        else:
            while len(questions) != 3:
                question = randint(0,4)
                if qnten[question] in questions:
                    hi = ''
                else:
                    if question != 2:
                        questions.append(qnten[question])

    elif name == "Lim Jin Yang" or name == "Pang Bang Yong":
        coinflip = randint(0,1)
        if coinflip == 1:
            coinflip2 = randint(0,1)
            if coinflip2 == 1:
                questions.append("tQn1")
            else:
                questions.append("pQn3")
            while len(questions) != 3:
                question = randint(0,4)
                if question != 3: #3 excluded as they made the question
                    questions.append(qnten[question])
        else:
            while len(questions) != 3:
                question = randint(0,4)
                if qnten[question] in questions:
                    hi = ''
                else:
                    if question != 3:
                        questions.append(qnten[question])

    elif name == "Li Menglin" or name == "Pang Shi Song" or name == "Tan Le Xuan":
        coinflip = randint(0,1)
        if coinflip == 1:
            coinflip2 = randint(0,1)
            if coinflip2 == 1:
                questions.append("tQn1")
            else:
                questions.append("pQn3")
            questions.append(qnten[randint(0,3)])
        else:
            questions.append(qnten[randint(0,3)])
            while len(questions) != 3:
                toAppend = qnten[randint(0,3)]
                if toAppend in questions:
                    hi = ''
                else:
                    questions.append(toAppend)
    

    else:
        print("Please check that you have keyed in your name correctly and used proper capitalisation")
    return questions
print(allocateQn())
