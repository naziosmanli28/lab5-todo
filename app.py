from flask import Flask, render_template, request, redirect
import pyrebase

firebase_config = {
    "apiKey": "AIzaSyDIeYaU3GoDW1gPEgmDuKyU_Ti8Htb-gRI",
    "authDomain": "todo2-42032.firebaseapp.com",
    "projectId": "todo2-42032",
    "storageBucket": "todo2-42032.firebasestorage.app",
    "messagingSenderId": "184485309281",
    "appId": "1:184485309281:web:06d458641756e50c70f320",
    "measurementId": "G-TZZRQKK66B",
    "databaseURL": "https://todo2-42032-default-rtdb.europe-west1.firebasedatabase.app/"
}


firebase = pyrebase.initialize_app(firebase_config)
db = firebase.database()

app = Flask(__name__)

@app.route('/')
def index():
    tasks = db.child("todos").get().val()
    tasks = tasks.items() if tasks else []
    return render_template("index.html", tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    db.child("todos").push({"task": task})
    return redirect('/')

@app.route('/delete/<id>')
def delete(id):
    db.child("todos").child(id).remove()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
