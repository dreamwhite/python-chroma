from datetime import datetime

class Chroma:

    """
    This class contains all the functions needed to create custom colorful text
    """

    reset = '\033[0m'

    def __init__(self, information_header='INFORMATION', warning_header='WARNING', error_header='ERROR', debug_header='DEBUG',
                sponsor_header='SPONSOR', stackoverflow_header='STACKOVERFLOW', documentation_header='DOCUMENTATION'):

                self.information_header = information_header
                self.warning_header = warning_header
                self.error_header = error_header
                self.debug_header = debug_header
                self.sponsor_header = sponsor_header
                self.stackoverflow_header = stackoverflow_header
                self.documentation_header = documentation_header
                self.fg_color_code = self.get_color_code(255,255,255)

    def get_color_code(self, red: int, green: int, blue: int, background: bool = False) -> str:
        """Generate a custom color code based off RGB and background/foreground parameters.

            Keyword arguments:
            red -- an integer between 0 and 255 (default 255)
            green -- an integer between 0 and 255 (default 255)
            blue -- an integer between 0 and 255 (default 255)
            background -- a boolean that if set to true sets the above colors as background, otherwise as foreground (default False)
        """

        red = red if red in range(0,256) else 255
        blue = blue if blue in range(0,256) else 255
        green = green if green in range(0,256) else 255
        background = background if (background in [True, False]) else False

        colorCode = f"\033[{48 if background else 38};2;{red};{green};{blue}m"
        return colorCode

    def get_header(self, header: str) -> str:
            MAX_HEADER_LENGTH = 16 #TODO: for the dreamwhite of the future make this parameter customizable from a settings.ini file
            if (len(header) > MAX_HEADER_LENGTH):
                return header[0:MAX_HEADER_LENGTH]
            else:
                return header.ljust(MAX_HEADER_LENGTH)

    def get_date(self) -> str:
        DATE_BACKGROUND = self.get_color_code(44, 62, 80, True)
        CURRENT_DATE = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"{DATE_BACKGROUND} {CURRENT_DATE.ljust(20)}"

    def string_builder(self, bg_color_code: str, fg_color_code: str, printed_header: str, text_colorCode: str, message: str) -> str:
        return ''.join([
            bg_color_code,
            fg_color_code,
            ' | ',
            printed_header,
            self.get_date(),
            self.reset,
            bg_color_code,
            ' ',
            self.reset,
            ' ',
            text_colorCode,
            message,
            self.reset
        ])

    def information(self, message: str) -> str:        
        printed_header = self.get_header(self.information_header)
        bg_color_code = self.get_color_code(46, 204, 113, True)
        text_colorCode = self.get_color_code(46, 204, 113)
        print(self.string_builder(bg_color_code, self.fg_color_code, printed_header, text_colorCode, message))

    def warning(self, message: str) -> str:
        printed_header = self.get_header(self.warning_header)
        bg_color_code = self.get_color_code(243, 156, 18, True)
        text_colorCode = self.get_color_code(243,156,18)
        print(self.string_builder(bg_color_code, self.fg_color_code, printed_header, text_colorCode, message))

    def error(self, message: str) -> str:
        printed_header = self.get_header(self.error_header)
        bg_color_code = self.get_color_code(192, 57, 43, True)
        text_colorCode = self.get_color_code(192, 57, 43)
        print(self.string_builder(bg_color_code, self.fg_color_code, printed_header, text_colorCode, message))

    def debug(self, message: str) -> str:
        printed_header = self.get_header(self.debug_header)
        bg_color_code = self.get_color_code(155, 89, 182, True)
        text_colorCode = self.get_color_code(155, 89, 182)
        print(self.string_builder(bg_color_code, self.fg_color_code, printed_header, text_colorCode, message))

    def sponsor(self, message: str) -> str:
        printed_header = self.get_header(self.sponsor_header)
        bg_color_code = self.get_color_code(22, 160, 133, True)
        text_colorCode = self.get_color_code(22, 160, 133)
        print(self.string_builder(bg_color_code, self.fg_color_code, printed_header, text_colorCode, message))

    def stackoverflow(self, message: str) -> str:
        printed_header = self.get_header(self.stackoverflow_header)
        bg_color_code = self.get_color_code(41, 128, 185, True)
        text_colorCode = self.get_color_code(41, 128, 185)
        print(self.string_builder(bg_color_code, self.fg_color_code, printed_header, text_colorCode, message))

    def documentation(self, message: str) -> str:
        printed_header = self.get_header(self.documentation_header)
        bg_color_code = self.get_color_code(236, 135, 191, True)
        text_colorCode = self.get_color_code(236, 135, 191)
        print(self.string_builder(bg_color_code, self.fg_color_code, printed_header, text_colorCode, message))
