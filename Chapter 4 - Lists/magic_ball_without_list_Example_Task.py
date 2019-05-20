import random


def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate on what you"re doing'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'For sure'


fortune = getAnswer(random.randint(1,8))
print(fortune)
