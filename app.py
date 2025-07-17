from flask import Flask, render_template, session, request, url_for, redirect
from scripts.helper_functions import generate_equation

app = Flask(__name__)
app.secret_key = 'BDd82s9fh1f1bc2inbBAsb9SBDYE6d06vc0cduc'  # Required when using session

question_total = 3

@app.route("/")
def home():
    session['score'] = 0
    session['question_count'] = 0
    return render_template("index.html")

@app.route('/question', methods=['GET', 'POST'])
def question():
    feedback = ''
    if request.method == 'POST':
        user_response = request.form['answer']

        try:
            if int(user_response) == session['answer']:
                feedback = "Correct!"
                session['score'] += 1
            else:
                feedback = f"Wrong, the correct answer is {session['answer']}."
        except ValueError:
            feedback = f"Invalid input. Please enter an integer. The correct answer is {session['answer']}."
        
        session['question_count'] += 1

    if session['question_count'] >= question_total:
        return redirect(url_for('result'))
    
    session['question'], session['answer'] = generate_equation()

    return render_template("question.html", question=session['question'], feedback=feedback)

@app.route('/result')
def result():
    score = session['score']
    percentage = (score / question_total) * 100

    percentage_display = int(percentage) if percentage.is_integer() else round(percentage, 1)

    return render_template('result.html', score=score, maximum_score=question_total, percentage=percentage_display)

if __name__ == '__main__':
    app.run(debug=True)