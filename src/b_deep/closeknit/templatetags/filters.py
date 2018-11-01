from django import template

register = template.Library()

def react_percentage(value):
    listHold = [0, 0, 0, 0]
    for reaction in value:
        for i in range(1, 5):
            if(int(reaction.status) == i):
                listHold[i - 1] = (listHold[i - 1] + 1)
    maxVal = max(listHold)
    listHold = list(map(lambda x: int(((x/maxVal) * 100)), listHold))
    return listHold

register.filter("percentage", react_percentage)
