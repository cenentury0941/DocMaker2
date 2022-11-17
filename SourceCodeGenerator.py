from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import img
from pygments.styles import STYLE_MAP

class GenerateSourceCode():
    def __init__(self, code):
        self.code = """
        Miku Miku Ni Shite Agerou
        
        from pygments import highlight                                                                     
        from pygments.style import Style
        from pygments.token import Token
        from pygments.lexers import Python3Lexer
        from pygments.formatters import Terminal256Formatter
        
        class MyStyle(Style):
                styles = {
                    Token.String:     'ansibrightblue bg:ansibrightred',
                }
        """

        self.code = code
        with open("res/Code.png" , "wb" ) as image:
            lexer = get_lexer_by_name("python", stripall=True)
            formatter = img.ImageFormatter( font_size=39 , line_number_bg='#FFFFFF', line_number_fg='#FFFFFF' , style='vs' , line_pad=10)
            result = highlight( code , lexer, formatter , image)
