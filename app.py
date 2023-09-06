from flask import Flask, request, render_template

app = Flask(__name__)
@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form['name']
    email = request.form['email']
    
    # Do something with the form data (e.g., store it in a Python variable)
    data = {
        'name': name,
        'email': email
    }
    
    return render_template('result.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
