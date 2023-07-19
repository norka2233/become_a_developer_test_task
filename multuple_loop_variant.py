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


def exclude_unique_symbol(str_3):
    splited_str = str_3.split()
    first_symbols = []
    first_unique = []
    for el in splited_str:
        for e in el:
            if el.count(e) == 1:
                first_symbols.append(e)
                break
            else: break
    for symbol in first_symbols:
        if first_symbols.count(symbol) == 1:
            first_unique.append(symbol)
            break
    return ''.join(first_unique)


if __name__ == '__main__':
    for f in (str, str_1, str_2, str_3, str_4, str_5):
        print(exclude_unique_symbol(f))



