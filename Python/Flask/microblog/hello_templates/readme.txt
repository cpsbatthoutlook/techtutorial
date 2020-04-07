Package name: hello_templates ##Tut1-2
App name : cps

from hello_templates import cps



Jinja2 templates : https://jinja.palletsprojects.com/en/2.11.x/templates/
{% %} , if else endif
    for endfor
        for u in users
        for k,v in mydict.items()
    block content, endblock

{% extends "base.html" %}
{% include 'header.html' %}

filter: https://jinja.palletsprojects.com/en/2.11.x/templates/#builtin-filters
    {{ [1, 2, 3]|min }} #min
    {{ [1, 2, 3]|join('|') }}
    {% for item in mydict|dictsort %}



{% ... %} for Statements
{{ ... }} for Expressions to print to the template output
{# ... #} for Comments not included in the template output
#  ... ## for Line Statements


