

class Author:

    def __init__(self, name, surname, birth_date, death_date):
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.death_date = death_date

    def __str__(self):
        birth_date = self.birth_date
        if birth_date is None:
            birth_date = ''

        death_date = self.death_date
        if death_date is None:
            death_date = ''

        return '{} {} ({}-{})'.format(self.name, self.surname, birth_date, death_date)
