import re 

# Makes the names of books on each line the full name instead of an abbreviation

def write(line):
    with open("king-james-version.txt", "a") as new_file:
        new_file.write(line)

def replace(abbreviation, full_name):
    with open("king-james-version-old.txt", "r") as old_file:
        for line in old_file:
            for i in range(10):
                if (re.search(f"^{abbreviation}{i}.*$", line)):
                    new_line = re.sub(f"{abbreviation}{i}", f"{full_name} {i}", line)
                    write(new_line)

def main():
    names = {"Ge":"Genesis", "Exo":"Exodus", "Lev":"Leviticus", "Num":"Numbers", "Deu":"Deuteronomy", "Josh":"Joshua", "Jdgs":"Judges", "Ruth":"Ruth", "1Sm":"1 Samuel", "2Sm":"2 Samuel", "1Ki":"1 Kings", "2Ki":"2 Kings", "1Chr":"1 Chronicles", "2Chr":"2 Chronicles", "Ezra":"Ezra", "Neh":"Nehemiah", "Est":"Esther", "Job":"Job", "Psa":"Psalm", "Prv":"Proverbs", "Eccl":"Ecclesiastes", "SSol":"Song of Solomon", "Isa":"Isaiah", "Jer":"Jeremiah", "Lam":"Lamentations", "Eze":"Ezekiel", "Dan":"Daniel", "Hos":"Hosea", "Joel":"Joel", "Amos":"Amos", "Obad":"Obadiah", "Jonah":"Jonah", "Mic":"Micah", "Nahum":"Nahum", "Hab":"Habakkuk", "Zep":"Zephaniah", "Hag":"Haggai", "Zec":"Zechariah", "Mal":"Malachi", "Mat":"Matthew", "Mark":"Mark", "Luke":"Luke", "John":"John", "Acts":"Acts", "Rom":"Romans", "1Cor":"1 Corinthians", "2Cor":"2 Corinthians", "Gal":"Galatians", "Eph":"Ephesians", "Phi":"Philippians", "Col":"Colossians", "1Th":"1 Thessalonians", "2Th":"2 Thessalonians", "1Tim":"1 Timothy", "2Tim":"2 Timothy", "Titus":"Titus", "Phmn":"Philemon", "Heb":"Hebrews", "Jas":"James", "1Pet":"1 Peter", "2Pet":"2 Peter", "1Jn":"1 John", "2Jn":"2 John", "3Jn":"3 John", "Jude":"Jude", "Rev":"Revelation"}

    for i in names:
        # print(i, names[i])
        replace(i, names[i])


def check():
    with open("king-james-version-old.txt", "r") as old:
        with open("king-james-version.txt", "r") as new:
            while(True):
                i = old.readline()
                j = new.readline()
                if(i[0] != j[0]): 
                    print(f"{i} was not equal to {j}")
                    break



if __name__ == "__main__":
    main()