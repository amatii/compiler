from lexer import Lexer

text_input = """
print(4444 + 4 - 2+3+3+4+5+6+7*9==4 >= 5 != 6 > 8);
"""

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

for token in tokens:
    print(token)
