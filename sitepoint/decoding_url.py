from urllib.request import urlopen #brings the urllib to action
with urlopen('http://sixty-north.com/c/t.txt') as story: #using with function for openning urls
    story_words = []
    for line in story:
        line_story = line.decode('utf-8').split() #decoding lines from binary 
        for word in line_story:
            story_words.append(word) #adding to the the list story_words 
    print(story_words)
