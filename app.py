from flask import Flask, render_template
app = Flask(__name__)
 
@app.route("/")
def overview_home():
    return render_template('visualisation_1.html')

@app.route("/overview")
def overview():
    return render_template('visualisation_1.html')
 
if __name__ == "__main__":
	app.static_folder = 'static'
	app.run(debug=True)