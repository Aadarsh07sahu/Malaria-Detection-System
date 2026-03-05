from flask import Flask, render_template, request, redirect, url_for, flash, session
import os
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Configure file upload path
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load pre-trained model
model = load_model('model.keras')  # Replace with your model file

# Simulated user database
users = {}

# Helper function to process the image and make predictions
def process_and_predict(img_path):
    img = image.load_img(img_path, target_size=(224, 224))  # Adjust size for your model
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0  # Normalize
    
    prediction = model.predict(img_array)
    predicted_class = np.argmax(prediction)  # Use argmax if your model outputs probabilities

    # Map numeric prediction to human-readable labels
    if predicted_class == 0:
        return "Normal"
    elif predicted_class == 1:
        return "Malaria Detected"
    else:
        return "Unknown"

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        
        if username in users:
            flash("Username already exists. Please choose a different one.", "danger")
        else:
            users[username] = password
            flash("Signup successful. Please log in.", "success")
            return redirect(url_for("login"))
    
    return render_template("signup.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        
        if username in users and users[username] == password:
            session['user'] = username
            flash("Login successful!", "success")
            return redirect(url_for("index"))
        else:
            flash("Invalid username or password.", "danger")
    
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop('user', None)
    flash("Logged out successfully.", "success")
    return redirect(url_for("login"))

@app.route("/", methods=["GET", "POST"])
def index():
    if 'user' not in session:
        flash("Please log in to access the app.", "danger")
        return redirect(url_for("login"))
    
    if request.method == "POST":
        # Get user inputs
        username = request.form['username']
        userage = request.form['userage']
        uploaded_file = request.files['image']

        if uploaded_file.filename != '':
            filename = secure_filename(uploaded_file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            uploaded_file.save(filepath)

            # Process the image and predict
            result = process_and_predict(filepath)

            return render_template("result.html", username=username, userage=userage, result=result, image_url=filepath)

        flash("Please upload an image!", "danger")
        return redirect(url_for("index"))

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
