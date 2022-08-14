"""Functions to parse a file containing villager data."""

import csv

def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """
    with open(filename, 'r') as csvfile:
        spamreader = csv.reader(csvfile)
        all_species = []
        for rows in spamreader:
            # print(row)
            line = rows[0].split('|')
            all_species.append(line[1])
            #print(all_species)
            unique_species = set(all_species)

        return unique_species


print(all_species("/Users/gedailey/src/data-structures/villagers.csv"))


def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """
    with open(filename, 'r') as csvfile:
        villager_file = csv.reader(csvfile)

        villagers = []

        for rows in villager_file:
            lines = rows[0].split('|')
            if search_string == lines[1]:
                villagers.append(lines[0])
            elif search_string == "All":
                villagers.append(lines[0])


    return sorted(villagers)

print(get_villagers_by_species("/Users/gedailey/src/data-structures/villagers.csv"))

def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """


    with open(filename, 'r') as csvfile:
        villager_file = csv.reader(csvfile)
        full_list = [[],[],[],[],[],[]]

        for rows in villager_file:
            lines = rows[0].split('|')
            if lines[3] == 'Fitness':
                full_list[0].append(lines[0])

            elif lines[3] == "Nature":
                full_list[1].append(lines[0])

            elif lines[3] == "Education":
                full_list[2].append(lines[0])

            elif lines[3] == "Music":
                full_list[3].append(lines[0])

            elif lines[3] == "Fashion":
                full_list[4].append(lines[0])

            elif lines[3] == "Play":
                full_list[5].append(lines[0])

    return full_list

print(all_names_by_hobby("/Users/gedailey/src/data-structures/villagers.csv"))


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    with open(filename, 'r') as csvfile:
        villager_file = csv.reader(csvfile)

        all_data = []

        for rows in villager_file:
            lines = rows[0].split('|')
            all_data.append((lines[0], lines[1], lines[2], lines[3]))


    return all_data

print(all_data("/Users/gedailey/src/data-structures/villagers.csv"))

def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    with open(filename, 'r') as csvfile:
        villager_file = csv.reader(csvfile)

        for rows in villager_file:
            lines = rows[0].split('|')
            if villager_name == lines[0]:
                return lines[4]
        return None

    # TODO: replace this with your code
print(find_motto("/Users/gedailey/src/data-structures/villagers.csv", 'Audie'))

def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    the_set = set()
    the_personality = None

    for i in all_data(filename):
        name, _, personality = i[:3]

        if name == villager_name:
            the_personality = personality
            break

    if the_personality:
        for i in all_data(filename):
            name, _, personality = i[:3]
            if personality == the_personality:
                the_set.add(name)
    return the_set


print(find_likeminded_villagers("/Users/gedailey/src/data-structures/villagers.csv", 'Kyle'))

