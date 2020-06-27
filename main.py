from collections import OrderedDict
from random import sample, choice

class Verb():
    """ """
    def __init__(self, regular, forms):
        """ """
        self.regular = regular
        self.conjuction = OrderedDict()
        self.conjuction['simple'] = forms[0]
        self.conjuction['third'] = forms[1]
        self.conjuction['ing'] = forms[2]
        self.conjuction['past'] = forms[3]
        self.conjuction['participle'] = forms[4]

    def __str__(self):
        return self.conjuction['simple'] + '-' + ('regular' if self.regular else 'irregular')
    
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

class Game():
    """ """

    def __init__(self):
        """"""
        self.list_verbs = ListVerbs()
        errors = self.list_verbs.read_verbs('verbs.txt')
        if errors == 0:
            print('Verbs read succesfully')
        else:
            print('Please check verbs list for a better game')
    
    def random_quiz(self):
        questions = ['third', 'ing', 'past', 'participle']
        number_questions = int(input('How many questions do yo want to do? '))
        if number_questions > len(self.list_verbs.list) or number_questions <= 0:
            number_questions = 10
        
        correct_answers = 0
        verbs_quiz = sample(self.list_verbs.list, number_questions)

        for verb in verbs_quiz:
            question = choice(questions)
            msg = verb.conjuction['simple'] + ' in ' + question + ' form: '
            answer = input(msg)
            if answer == verb.conjuction[question]:
                correct_answers += 1
                print('good')
            else:
                print('bad')
        
        print('You have ' + str(correct_answers) + ' correct answers of ' + str(number_questions))

if __name__ == '__main__':
    new_game = Game()
    new_game.random_quiz()

