import pycodestyle


class PepChecker:
    def __init__(self):
        self.text = ""
        self.error_list = []

    def get_errors(self, text):
        self.write_into_file(text)
        fchecker = pycodestyle.Checker("text.txt", show_source=True)

        self.error_list = fchecker.check_all()

    def write_into_file(self, text):
        out_text = []
        temp_string = []
        for i in range(len(text)):
            if text[i] == "\n":
                out_text.append(temp_string)
                temp_string = []
            else:
                temp_string += text[i]

        """for i in range(len(out_text)):
            for j in range(len(out_text[i])):
                print(out_text[i])"""

        with open('text.txt', 'w') as f:
            for i in range(len(out_text)):
                for j in range(len(out_text[i])):
                    f.write("".join(out_text[i][j]))
