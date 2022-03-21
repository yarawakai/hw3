from flask import Flask

myapp_obj = Flask(__name__)

name = 'Hieu'
city_names = ['Paris', 'London', 'Rome', 'Tahiti']

@myapp_obj.route("/")
def home():
    name = 'Lisa'
    city_names = ['Paris', 'London', 'Rome', 'Tahiti']
    str = ""
    for city in city_names:
        str += "<li>" + city + "</li>"
    return '''
    <html>
    <head>
    </head>
    <body>
            <h1>Welcome ''' + name + '''!</h1>
            <a href="www.google.com">not google</a>
            <ul>''' + str + '''</ul>
</body>
</html>'''

myapp_obj.run()
