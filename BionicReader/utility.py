

def refactoring(line):
    words = line.split(" ")
    proposition = ""
    for word in words:
        wordLength = len(word)
        newWord = ""
        if wordLength >= 4:
            for i in range(wordLength):
                if i == 0:
                    newWord += "[b]" + word[i]
                elif i == 3:
                    newWord += "[/b]" + word[i]
                    
                else:
                    newWord += word[i]
        else:
            newWord ="[b]" + word + "[/b]"
        proposition += newWord + " "
    return proposition

               