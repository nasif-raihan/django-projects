from django import template

register = template.Library()


@register.filter(name="remove_characters")
def remove_characters(value, args):
    for character in args:
        if character == ",":
            value = value.replace(character, ", ")
        else:
            value = value.replace(character, "")
    return value
