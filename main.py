""" To launch the program:
 - write in the terminal $ python3 main.py
 or
 - press right button on the file and press "Run 'main' row 49"
 or
 - click green arrow and press "Run 'main'"
 """

"""----------STRINGS FOR TESTING----------"""
str = "Bla bla"
str_1 = "Eleonora El Peso"  # => P
str_2 = "Gerbils Mice King and Genkhis Khan" # => M
str_3 = """The Tao gave birth to machine language.  Machine language gave birth
to the assembler.
The assembler gave birth to the compiler.  Now there are ten thousand
languages.
Each language has its purpose, however humble.  Each language
expresses the Yin and Yang of software.  Each language has its place within
the Tao.
But do not program in COBOL if you can avoid it.
        -- Geoffrey James, "The Tao of Programming"
"""
str_4 = """ C makes it easy for you to shoot yourself in the foot. C++ makes that harder, 
but when you do, it blows away your whole leg. (с) Bjarne Stroustrup
""" # => e
str_5 = "55587327fahv" # => 8



"""----------SOLUTION WITH INSTRUCTIONS-----------
unique_all => function to wrap and kick the first_unique function, also converts input from string to list
and loops through every word in it"""
def unique_all(text: str) -> str:
    """ first_unique => function to get first unique symbols """
    def first_unique(word: str) -> str:
        """loops through every letter of the word of the list and adds unique symbols to the unique_letters variable """
        unique_letters = [letter for letter in word if word.count(letter) == 1]
        """ in case any symbols were found or just empty, the function returns an empty string """
        if not unique_letters:
            return ""
        """ returns only the first string from the list of the first unique symbols from every word """
        return unique_letters[0]
    """  first_letters => list of strings (every word) of the input text in case if the string is not empty,
    # triggers inside function (first_unique) to get to the letters of the word """
    first_letters = [first_unique(t) for t in text.split(' ') if t]
    return first_unique(first_letters)


if __name__ == '__main__':
    for s in (str, str_1, str_2, str_3, str_4, str_5):
        print(unique_all(s))
