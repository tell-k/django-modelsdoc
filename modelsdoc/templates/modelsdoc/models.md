{% load modelsdoc_tags %}

{% for model in models %}
## {{ model.name }}({{ model.class_fullname }})

```
{{ model.doc }}
```

{% emptylineless %}
{% for label, attr in display_fields %}|{{ label }}{% endfor %}|
{% for label, attr in display_fields %}|---{% endfor %}|
{% for field in model.fields %}
{% for label, attr in display_fields %}|{{ field|get_attr:attr }}{% endfor %}|
{% endfor %}
{% endemptylineless %}
{% endfor %}

{% if model.model_options %}
```
Options::

 {% emptylineless %}
 {% for name, value in model.model_options.items %}
 {{ name }} : {{ value|safe }}
 {% endfor %}
 {% endemptylineless %}
```
{% endif %}
