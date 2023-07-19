""" To launch the program:
1. Clone the git repository to your device:
    - move to the working directory you prefer to locate the files
    - run in the terminal:
        $ git clone git@github.com:norka2233/become_a_developer_test_task.git
    - open  'become_a_developer_test_task' folder
2. Run the program
     - write in the terminal $ python3 multiple_loop_variant.py
     or
     - press right button on the file and press "Run 'multiple_loop_variant' row 58"
     or
     - click green arrow and press "Run 'multiple_loop_variant'"
     - in the terminal you should see the values after function execution:
         B
         P
         M
         m
         e
         8

 """

"""----------STRINGS FOR TESTING----------"""
str = "Bla bla" # => B
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
""" # => m
str_4 = """ C makes it easy for you to shoot yourself in the foot. C++ makes that harder, 
but when you do, it blows away your whole leg. (с) Bjarne Stroustrup
""" # => e
str_5 = "55587327fahv" # => 8

"""----------SOLUTION WITH INSTRUCTIONS----------"""
def exclude_unique_symbol(text: str) -> str:
    """convert input text to the list"""
    splited_str = text.split()
    """variable for first unique symbols of every word"""
    first_symbols = []
    """variable for first unique symbol of first_symbols variable"""
    first_unique = []
    """loop through every word in the list"""
    for el in splited_str:
        """loop through every letter in the word"""
        for e in el:
            """find unique symbol"""
            if el.count(e) == 1:
                """add this symbol to the list"""
                first_symbols.append(e)
                """as we need only the first unique symbol we can break the loop right after the symbol is found"""
                break
    """loop through the list of the first unique symbol of every word"""
    for symbol in first_symbols:
        """check the first unique symbol"""
        if first_symbols.count(symbol) == 1:
            """add this symbol to the list"""
            first_unique.append(symbol)
            """as we need only the first one, the loop can be stopped"""
            break
    """convert this first symbol to the string """
    return ''.join(first_unique)


if __name__ == '__main__':
    for f in (str, str_1, str_2, str_3, str_4, str_5):
        print(exclude_unique_symbol(f))



