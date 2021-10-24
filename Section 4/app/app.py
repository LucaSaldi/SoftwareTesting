from flask import Flask, jsonify

app = Flask(__name__)


# jsonify is belangrijk want een Flaskendpoint kan geen dictionary returnen
# Flask niet zo belangrijk, dit is een API van python die ons toelaat web-applications te bouwen.
# onze system test gaat het endpoint gaan testen
@app.route('/')  # http://www.mysite.com/
def home():
    return jsonify({'message': 'Hello, world!'})


# wanneer geldt dit, het hangt ervan af oe python modules importeert, niet echt belangrijk zegt hij dsu gebeurt enkel
# wanneer name == main, hier is dit het geval met app, hadden we een andere file geïmporteerd had dit niet zo geweest

# Niet enkel app.run(), want als er een andere variabele app importeert gaat de app niet runnen als je dit niet wilt
if __name__ == '__main__':
    app.run()
