from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    with app.open_resource('static/css/vesper-icons.css', 'r') as f:
        css_list = f.readlines()

    icons = [i[4:i.index(':')] for i in css_list if i.startswith('.vs-')]

    return render_template('index.html', icons=icons)


if __name__ == '__main__':
    app.run(debug=True)
