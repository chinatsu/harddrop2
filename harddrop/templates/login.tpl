<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="shortcut icon" href="/favicon.ico">
        <title>{{ form.action }} - Hard Drop</title>
        <style type="text/css">
            @import url(https://fonts.googleapis.com/css?family=Open+Sans:300,400,700);
        </style>
        <link href="http://cute.enterprises/static/css/style.css" rel="stylesheet" type="text/css">
        <link href="http://cute.enterprises/static/css/base.css" rel="stylesheet" type="text/css">
    </head>
    <body>
        <div id="root">
            <div class="harddrop">
                <div class="harddrop-header">
                    <img class="harddrop-logo" src="http://cute.enterprises/static/media/logo.png" alt="logo">
                    <h1>{{ form.action }}</h1>
                </div>
                <form method=post>
                    <ul class="harddrop-form">
                      {% for field in form %}
                      <li>
                        {% if field.type != "SubmitField" %}{{ field.label }}{% endif %}
                        {{ field }}
                      </li>
                      {% endfor %}
                    </ul>
                </form>
            </div>
        </div>
    </body>
</html>
