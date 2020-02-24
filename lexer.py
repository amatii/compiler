from rply import LexerGenerator


class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # Print
        self.lexer.add('PRINT', r'print')
        # Parenthesis
        self.lexer.add('OPEN_PAREN', r'\(')
        self.lexer.add('CLOSE_PAREN', r'\)')
        # Semi Colon
        self.lexer.add('SEMI_COLON', r'\;')
        # Operators
        self.lexer.add('SUM', r'\+')
        self.lexer.add('SUB', r'\-')
        self.lexer.add('MUL', r'\*')
        # RelOP
        self.lexer.add('LESS', r'\<')
        self.lexer.add('GRT', r'\>')

        self.lexer.add('EQU', r'\==')
        self.lexer.add('NEQU', r'\!=')
        self.lexer.add('EQU', r'\==')
        self.lexer.add('LEQU', r'\<=')
        self.lexer.add('GEQU', r'\>=')

        # Number
        self.lexer.add('NUMBER', r'\d+')
        # Ignore spaces
        self.lexer.ignore('\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()
