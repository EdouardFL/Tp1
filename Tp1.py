#Code crée par Édouard Fortin Lefrancois
#Ce code compte le nombre de mot dans une string

chaine = input("Input a string of your choosing")

def word_count(string):
    words = 0 #counts the number of words
    for i in string.split(" "):
        if i != "": #Évite que les espaces sont comptées.
            words += 1
    return words

print(word_count(chaine))
