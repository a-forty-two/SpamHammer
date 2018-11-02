import os
from collections import Counter


def save(classifier, name):
    with open(name, 'wb') as fp:
        c.dump(classifier, fp)
    print "saved"



def make_dict():
    directory = "emails/"
    root = os.listdir(directory)
    emails = [directory + email for email in root]
    words = []
    count = len(emails)
    for email in emails:
        y = open(email)
        z = y.read()
        words += z.split(" ")
        print count
        count -= 1

    for j in range(len(words)):
        if not words[j].isalpha():
            words[j] = ""

    dictionary = Counter(words)
    del dictionary[""]
    return dictionary.most_common(3000)

