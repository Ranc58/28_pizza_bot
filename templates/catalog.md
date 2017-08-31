Пицца из нашего меню:

{% for entry in catalog -%}
*{{ entry.pizza_title }} #{{loop.index}}*
{{ entry.pizza_toppings }}
    {%- for choice in entry.pizza_variable_content %}
        *{{ choice.pizza_size }} - {{ choice.pizza_price }} руб.*
    {%- endfor %}

{% endfor %}
