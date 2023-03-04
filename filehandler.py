import time
import validator

class Solution:
    """_summary_
    """
    def __init__(self, programs_list, accepted_programs):
        """ Args:
            programs_list (str): name of the text file (user desired programs), located in the main file.
            accepted_programs (str): name of the text file (incl. program names that are valid), located in the main file.
        """
        self.programs_list = programs_list
        self.accepted_programs = accepted_programs

    def txt_files(self):
        """ 1. cleans empty lines, if any.
            2. saves it without empty lines, in to same file.
            3. checks if the given program already exist.
                - this happens using "which" command (in validator file).
        """
        no_empty_lines = ""
        programs_added = []
        with open(self.programs_list, "r") as file:
            for line in file:
                if not line.isspace():
                    no_empty_lines += line
                    programs_added.append(line.strip())

        with open(self.programs_list, "w") as file:
            # print(no_empty_lines) # debugging
            file.write(no_empty_lines)


        for line in programs_added:
            result = validator.check_exist(line)
            time.sleep(2)
            print(result)
            if not line:
                break

    def make_list(self):
        """ Turns "accepted programs".txt in to an array.
        """
        with open(self.accepted_programs) as file:
            lst_comprehension = [line.replace("\n","") for line in file]
            print(lst_comprehension)