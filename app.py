from bottle import Bottle, run, template

app = Bottle()


@app.route('/')
def hello():
        return template('chart.html')


run(app, host='localhost', port=8081, debug=True)