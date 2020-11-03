from flask import Flask, render_template

app = Flask(__name__)

@app.route('/zak')
def zak():
    return render_template('zak.html')

@app.route('/jeff')
def jeff():
    return render_template('jeff.html')

@app.route('/exercise')
def exercise():
    return render_template('exercise.html')

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
