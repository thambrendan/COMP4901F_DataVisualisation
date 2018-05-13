from flask import Flask, render_template
app = Flask(__name__)
 
@app.route("/")
def overview_home():
    return render_template('visualisation_2.html')

@app.route("/visualisation_1")
def visualisation_1():
    return render_template('visualisation_1.html')

@app.route("/visualisation_3")
def visualisation_3():
    return render_template('visualisation_3.html')

@app.route("/testing")
def visualisation_3():
    return render_template('bootstrap2.html')
 
if __name__ == "__main__":
	app.static_folder = 'static'
	app.run(debug=True)