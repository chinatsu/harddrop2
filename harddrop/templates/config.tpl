<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="shortcut icon" href="/favicon.ico">
        <title>Harddrop Configuration</title>
        <style type="text/css">
            @import url(https://fonts.googleapis.com/css?family=Open+Sans:300,400,700);
        </style>
        <link href="http://cute.enterprises/static/css/conf.css" rel="stylesheet" type="text/css">
        <link href="http://cute.enterprises/static/css/base.css" rel="stylesheet" type="text/css">
    </head>
    <body>
        <div id="root">
            <div class="config">
                <div class="config-header">
                    <img class="config-logo" src="http://cute.enterprises/static/media/config.svg" alt="logo">
                    <h1>Configuration</h1>
                </div>
                <p class="config-intro">
                    I seem to have lost my configuration file! Let's start setting up by connecting to a database server.
                </p>
                <p class="config-intro">
                    Once connected, I'll look for a database named <code>harddrop</code>, and create it if I don't see it.
                </p>
                <form method=post>
                    <ul class="config-form">
                        <li>
                            <label for="server">Database server</label>
                            <input type="text" id="server" name="server">
                        </li>
                        <li>
                            <label for="username">Database username</label>
                            <input type="text" id="username" name="username">
                        </li>
                        <li>
                            <label for="password">Database password</label>
                            <input type="password" id="password" name="password">
                        </li>
                        <li>
                            <input type="submit" value="Continue">
                        </li>
                    </ul>
                </form>
            </div>
        </div>
    </body>
</html>
