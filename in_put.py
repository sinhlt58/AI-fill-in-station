import string
import random

class Input:
    @classmethod
    def get_dictionary(self):
        file1 = open('3_letters_dictionary')
        dictionary = []
        with file1 as f:
            for line in f:
                dictionary.append(line[0:3])
        return dictionary

    @classmethod
    def get_frequency_list(self):
        return self.get_new_frequency_list("bigram_frequence_list")
        """
        file2 = open('bigram_frequence_list')
        frequency_list = {}
        with file2 as f:
            for line in f:
                actLen = len(line) - 1
                frequency_list[line[0]+line[2]] = float(line[4:actLen])
        return frequency_list
        """
    @classmethod
    def get_new_frequency_list(self, filename):
        file1 = open(filename)
        frequency_list = {}
        with file1 as f:
            for line in f:
                pair_freq = []
                actLen = len(line)-1
                line = line[:actLen]
                array_line = line.split()
                pair = array_line[0] + array_line[1]
                for i in range(2, len(array_line)):
                    pair_freq.append(float(array_line[i]))
                frequency_list[pair] = pair_freq
        return frequency_list

    @classmethod
    def get_letter_matrix(self, file_name):
        file1 = open(file_name)
        letters = []
        with file1 as f:
            for line in f:
                line = line[0:9]
                s = self.convert_line_to_matrix(line)
                letters.append(s)
        return letters

    @classmethod
    def convert_line_to_matrix(self, line):
        s = []
        for i in range(3):
            w = []
            for l in line[i*3:(i*3+3)]:
                w.append(str(l))
            s.append(w)
        return s

    @classmethod
    def get_source(self):
        return self.get_dictionary(), self.get_frequency_list()
