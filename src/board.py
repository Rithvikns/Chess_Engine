from dataclasses import dataclass , field

@dataclass
class board:
    board : list[int] = field(default_factory = list)

    @staticmethod
    def convert_notation_to_position(str):
        if str[0] not in "abcdefgh":
            return "wrong notation"
        else:
            if str[0] == 'a':
                return (1,int(str[1]))
            elif str[0] == 'b':
                return (2,int(str[1]))
            elif str[0] == 'c':
                return (3,int(str[1]))
            elif str[0] == 'd':
                return (4,int(str[1]))
            elif str[0] == 'e':
                return (5,int(str[1]))
            elif str[0] == 'f':
                return (6,int(str[1]))
            elif str[0] == 'g':
                return (7,int(str[1]))
            elif str[0] == 'h':
                return (8,int(str[1]))
            
    def display_function():
        print("chess Board is")