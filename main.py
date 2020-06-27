import json

class Verb():
    """ """
    def __init__(self, regular, forms):
        """ """
        self.regular = regular
        self.simple_form = forms[0]
        self.third_form = forms[1]
        self.ing_form = forms[2]
        self.past_form = forms[3]
        self.participle_form = forms[4]

    def __str__(self):
        return self.simple_form + '-' + ('regular' if self.regular else 'irregular')
    
class ListVerbs():
    """ """
    def __init__(self):
        """ """
        self.list = []

    def add_verb(self, verb):
        """ """
        self.list.append(verb)

    def read_verbs(self, file_name):
        """"""
        with open(file_name) as file_verbs:
            lines = file_verbs.readlines()
        
        errors = 0
        for line in lines:
            attributes = line.strip().split()
            if len(attributes) == 6:
                regular = True if attributes[0] == 'si' else False
                verb = Verb(regular, attributes[1:])
                self.add_verb(verb)
            else:
                errors += 1
            
        return errors


if __name__ == '__main__':
    my_list = ListVerbs()
    total_errors = my_list.read_verbs('verbs.txt')

    for verb in my_list.list:
        print(verb)

    print('\n\nTotal Errors : ' + str(total_errors))
    print('\nVerbs registered : ' + str(len(my_list.list)))