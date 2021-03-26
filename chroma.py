from datetime import datetime

class Chroma():

    """
    This class contains all the functions needed to create custom colorful text
    """

    RESET = '\033[0m'

    def getColorCode(self, red: int, green: int, blue: int, background: bool = False) -> str:

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

    def getHeader(self, header: str) -> str:
            MAX_HEADER_LENGTH = 16 #TODO: for the dreamwhite of the future make this parameter customizable from a settings.ini file
            if (len(header) > MAX_HEADER_LENGTH):
                return header[0:MAX_HEADER_LENGTH]
            else:
                return header.ljust(16)

    def getDate(self) -> str:
        DATE_BACKGROUND = self.getColorCode(44, 62, 80, True)
        CURRENT_DATE = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"{DATE_BACKGROUND} {CURRENT_DATE.ljust(20)}"

    def getColoredMessage(self, colorCode: str, message: str) -> str:
        return f"{colorCode}{message}{self.RESET}"

    def informationMessage(self, message: str) -> str:
        HEADER = "INFORMATION"
        
        printed_header = self.getHeader(HEADER)
        bg_colorCode = self.getColorCode(46, 204, 113, True)
        fg_colorCode = self.getColorCode(255,255,255)
        text_colorCode = self.getColorCode(46, 204, 113)

        final_string = f"{bg_colorCode}{fg_colorCode} | "
        final_string += f"{printed_header}"
        final_string += f"{self.getDate()}"
        final_string += f"{self.RESET}{bg_colorCode} {self.RESET} {text_colorCode}{message}{self.RESET}" 
        print(final_string)

    def warningMessage(self, message: str) -> str:
        HEADER = "WARNING"
        
        printed_header = self.getHeader(HEADER)
        bg_colorCode = self.getColorCode(243, 156, 18, True)
        fg_colorCode = self.getColorCode(255,255,255)
        text_colorCode = self.getColorCode(243,156,18)

        final_string = f"{bg_colorCode}{fg_colorCode} | "
        final_string += f"{printed_header}"
        final_string += f"{self.getDate()}"
        final_string += f"{self.RESET}{bg_colorCode} {self.RESET} {text_colorCode}{message}{self.RESET}" 
        print(final_string)

    def errorMessage(self, message: str) -> str:
        HEADER = "ERROR"
        
        printed_header = self.getHeader(HEADER)
        bg_colorCode = self.getColorCode(192, 57, 43, True)
        fg_colorCode = self.getColorCode(255,255,255)
        text_colorCode = self.getColorCode(192, 57, 43)

        final_string = f"{bg_colorCode}{fg_colorCode} | "
        final_string += f"{printed_header}"
        final_string += f"{self.getDate()}"
        final_string += f"{self.RESET}{bg_colorCode} {self.RESET} {text_colorCode}{message}{self.RESET}" 
        print(final_string)

    def debugMessage(self, message: str) -> str:
        HEADER = "DEBUG"
        
        printed_header = self.getHeader(HEADER)
        bg_colorCode = self.getColorCode(155, 89, 182, True)
        fg_colorCode = self.getColorCode(255,255,255)
        text_colorCode = self.getColorCode(155, 89, 182)

        final_string = f"{bg_colorCode}{fg_colorCode} | "
        final_string += f"{printed_header}"
        final_string += f"{self.getDate()}"
        final_string += f"{self.RESET}{bg_colorCode} {self.RESET} {text_colorCode}{message}{self.RESET}" 
        print(final_string)

    def sponsorMessage(self, message: str) -> str:
        HEADER = "SPONSOR"
        
        printed_header = self.getHeader(HEADER)
        bg_colorCode = self.getColorCode(22, 160, 133, True)
        fg_colorCode = self.getColorCode(255,255,255)
        text_colorCode = self.getColorCode(22, 160, 133)

        final_string = f"{bg_colorCode}{fg_colorCode} | "
        final_string += f"{printed_header}"
        final_string += f"{self.getDate()}"
        final_string += f"{self.RESET}{bg_colorCode} {self.RESET} {text_colorCode}{message}{self.RESET}" 
        print(final_string)

    def stackOverflowMessage(self, message: str) -> str:
        HEADER = "STACKOVERFLOW"
        
        printed_header = self.getHeader(HEADER)
        bg_colorCode = self.getColorCode(41, 128, 185, True)
        fg_colorCode = self.getColorCode(255,255,255)
        text_colorCode = self.getColorCode(41, 128, 185)

        final_string = f"{bg_colorCode}{fg_colorCode} | "
        final_string += f"{printed_header}"
        final_string += f"{self.getDate()}"
        final_string += f"{self.RESET}{bg_colorCode} {self.RESET} {text_colorCode}{message}{self.RESET}" 
        print(final_string)

    def documentationMessage(self, message: str) -> str:
        HEADER = "DOCUMENTATION"
        
        printed_header = self.getHeader(HEADER)
        bg_colorCode = self.getColorCode(236, 135, 191, True)
        fg_colorCode = self.getColorCode(255,255,255)
        text_colorCode = self.getColorCode(236, 135, 191)

        final_string = f"{bg_colorCode}{fg_colorCode} | "
        final_string += f"{printed_header}"
        final_string += f"{self.getDate()}"
        final_string += f"{self.RESET}{bg_colorCode} {self.RESET} {text_colorCode}{message}{self.RESET}" 
        print(final_string)