import json

class Verb():
    """ """
    def __init__(self, regular, simple_form, third_form, ing_form, past_form, participle_form):
        """ """
        self.regular = regular
        self.simple_form = simple_form
        self.third_form = third_form
        self.ing_form = ing_form
        self.past_form = past_form
        self.participle_form = participle_form

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
        
        for line in lines:
            attributes = line.strip().split()
            regular = True if attributes[0] == 'si' else False
            verb = Verb(regular, attributes[1], attributes[2], attributes[3],
                attributes[4], attributes[5])
            self.add_verb(verb)



if __name__ == '__main__':
    my_list = ListVerbs()
    my_list.read_verbs('verbs.txt')

    for verb in my_list.list:
        print(verb)