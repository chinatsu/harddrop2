{%- extends "base.tpl" %}

{% import "bootstrap/utils.html" as utils %}
{% import "bootstrap/wtf.html" as wtf %}

{% block content %}
    <div class="container">
    {%- with messages = get_flashed_messages(with_categories=True) %}
    {%- if messages %}
        <div class="row">
            <div class="col-md-12">
                {{ utils.flashed_messages(messages) }}
            </div>
        </div>
    {%- endif %}
    {%- endwith %}
        <div class="col-md-12">
            <form method="post">
            {% for field in form %}
                {% if field.type != "SubmitField" %}
                    <div class="form-group">
                        {{ field.label }}
                        {{ field(class_="form-control") }}
                        {% if field.errors %}
                            <ul class="errors">
                                {% for error in field.errors %}
                                    <li>{{ error }}</li>
                                {% endfor %}
                            </ul>
                        {% endif %}
                    </div>
                {% else %}
                    <button class="btn btn-default" type="{{ field.label.data }}">{{ form.action }}</button>
                {%- endif %}
            {%- endfor %}
            </form>
        </div>
    </div>
{%- endblock %}
