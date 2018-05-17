from flask import Flask, render_template
import os

IMAGE_FOLDER = os.path.join('static', 'image')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = IMAGE_FOLDER
 
@app.route("/")
def overview_home():
    imagename = os.path.join(app.config['UPLOAD_FOLDER'], 'paul-smith-193761-unsplash.jpg')
    return render_template('temp_visualisation.html', user_image = imagename)

@app.route("/visualisation_1")
def visualisation_1():
    return render_template('visualisation_1.html')

@app.route("/visualisation_3")
def visualisation_3():
    return render_template('visualisation_3.html')

# @app.route("/main")
# def testing_bootstrap():
#     return render_template('bootstrap2.html')

# @app.route("/testing")
# def testing_bootstrap():
#     return render_template('bootstrap3.html')
 
if __name__ == "__main__":
	app.static_folder = 'static'
	app.run(debug=True)