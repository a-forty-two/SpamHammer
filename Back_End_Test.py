//Included in file Hello.py

def load(classifier_file):
    with open(classifier_file) as fp:
        classifier=c.load(fp)
    return classifier
	
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


        
    for word in dict:
        features.append(user.count(word[0]))
    res = classifier.predict([features])
    
    a=["Not Spam", "Spam!"][res[0]]
    return render_template('hello.html',result=a)

