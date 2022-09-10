from random import randint
from flask import Flask

app = Flask(__name__)


@app.route("/whole-bible")
def whole_bible():
    # Prints 1-7 random verses from the Bible
    verses = []
    rand_verse_selector = randint(1, 31102)
    rand_how_many_verses = randint(1, 7)

    verse_finder_count = 0
    current_count_verses = 0

    with open("king-james-version.txt", "r") as file:
        file_line = file.readline()
        while(file_line):
            if(verse_finder_count == rand_verse_selector):
                while(current_count_verses < rand_how_many_verses):
                    file_line = file.readline()
                    verses.append(file_line.strip())
                    current_count_verses += 1
                break
            else:
                file_line = file.readline()
                verse_finder_count += 1

    return verses


@app.route("/new-testament")
def new_testament():
    # Prints 1-7 random verses from the Bible
    verses = []
    rand_verse_selector = randint(23146, 31102)
    rand_how_many_verses = randint(1, 7)

    verse_finder_count = 0
    current_count_verses = 0

    with open("king-james-version.txt", "r") as file:
        file_line = file.readline()
        while(file_line):
            if(verse_finder_count == rand_verse_selector):
                while(current_count_verses < rand_how_many_verses):
                    file_line = file.readline()
                    verses.append(file_line.strip())
                    current_count_verses += 1
                break
            else:
                file_line = file.readline()
                verse_finder_count += 1

    return verses


@app.route("/old-testament")
def old_testament():
    # Prints 1-7 random verses from the Bible
    verses = []
    rand_verse_selector = randint(1, 23145)
    rand_how_many_verses = randint(1, 7)

    verse_finder_count = 0
    current_count_verses = 0

    with open("king-james-version.txt", "r") as file:
        file_line = file.readline()
        while(file_line):
            if(verse_finder_count == rand_verse_selector):
                while(current_count_verses < rand_how_many_verses):
                    file_line = file.readline()
                    verses.append(file_line.strip())
                    current_count_verses += 1
                break
            else:
                file_line = file.readline()
                verse_finder_count += 1

    return verses


if __name__ == "__main__":
    app.run("localhost", 5000)

