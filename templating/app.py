from flask import Flask, render_template

app = Flask(__name__)

@app.route('/zak')
def ben():
    return render_template('zak.html')

@app.route('/jeff')
def harry():
    return render_template('jeff.html')

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
