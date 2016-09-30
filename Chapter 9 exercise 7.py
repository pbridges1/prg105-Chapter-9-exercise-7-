def is_triple(word):

    i = 0
    count = 0
    while i < len(word)-1:
        if word[i] == word[i+1]:
            count = (count + 1)
            if count == 3:
                return True
            i = (i + 2)
        else:
            count = 0
            i = (i + 1)
    return False


def find_consecutive():

    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if is_triple(word):
            print word


print "Words with 3 consecutive double letters are: \n"
find_consecutive()
