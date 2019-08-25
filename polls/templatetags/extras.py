from django import template

register = template.Library()


# returns specific element of a form when served with form and question_id
@register.filter
def respective_field(form, question_id):
    return form['question' + str(question_id)]


# returns percentage in integer when given with number and total
@register.filter
def to_percent(num, total):
    print(num)
    return int(num*100/total)
