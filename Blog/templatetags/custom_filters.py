from django import template

register = template.Library()


# this filter will return a string from character 0 until 500
# this will allow users to see a preview of the blog post on the main display page
def range_filter(value):
    return value[0:500] + "....."


register.filter('range_filter', range_filter)
