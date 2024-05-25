from flask import Flask, render_template
from data import generate_plots

app = Flask(__name__)

@app.route('/')
def plot():
    plot1, plot2 = generate_plots()
    return render_template('index.html', plot1=plot1, plot2=plot2)

if __name__ == '__main__':
    app.run(debug=True)
