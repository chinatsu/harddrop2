{# This simple template derives from ``base.html``. See ``base.html`` for
   more information about template inheritance. #}
{%- extends "base.tpl" %}

{# Loads some of the macros included with Flask-Bootstrap. We are using the
   utils module here to automatically render Flask's flashed messages in a
   bootstrap friendly manner #}
{% import "bootstrap/utils.html" as utils %}


{# Inside the ``content`` is where you should place most of your own stuff.
   This will keep scripts at the page end and a navbar you add on later
   intact. #}
{% block content %}
  <div class="container">
  {%- with messages = get_flashed_messages(with_categories=True) %}
  {%- if messages %}
    <div class="row">
      <div class="col-md-12">
        {{utils.flashed_messages(messages)}}
      </div>
    </div>
  {%- endif %}
  {%- endwith %}
    <div class="jumbotron">
        <p>News should be here</p>
    </div>
   </div>
{%- endblock %}
