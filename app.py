from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'edutestor_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///edutestor.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    role = db.Column(db.String(50), nullable=False, default='student')

class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(500), nullable=False)
    option_a = db.Column(db.String(200), nullable=False)
    option_b = db.Column(db.String(200), nullable=False)
    option_c = db.Column(db.String(200), nullable=False)
    correct = db.Column(db.String(1), nullable=False)

@app.route('/')
def home():
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        return render_template('dashboard.html', user=user)
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
    name = request.form['name']
    email = request.form['email']
    password = generate_password_hash(
        request.form['password'], method='pbkdf2:sha256'
    )
    role = request.form['role']
    if User.query.filter_by(email=email).first():
        flash('Email already exists.')
        return redirect(url_for('register'))
    new_user = User(name=name, email=email, password=password, role=role)
    db.session.add(new_user)
    db.session.commit()
    flash('Registration successful. Please login.')
    return redirect(url_for('login'))
return render_template('register.html')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            return redirect(url_for('home'))
        else:
            flash('Incorrect email or password.')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out.')
    return redirect(url_for('home'))

@app.route('/delete_account', methods=['GET', 'POST'])
def delete_account():
    if 'user_id' not in session:
        flash('Please login to delete your account.')
        return redirect(url_for('login'))
    user = User.query.get(session['user_id'])
    if request.method == 'POST':
        db.session.delete(user)
        db.session.commit()
        session.pop('user_id', None)
        flash('Your account has been deleted.')
        return redirect(url_for('home'))
    return render_template('delete_account.html', user=user)

@app.route('/add_test', methods=['GET', 'POST'])
def add_test():
    if 'user_id' not in session:
        flash('Please login as teacher to add test.')
        return redirect(url_for('login'))
    user = User.query.get(session['user_id'])
    if user.role != 'teacher':
        flash('Access denied.')
        return redirect(url_for('home'))
    if request.method == 'POST':
        question = request.form['question']
        option_a = request.form['option_a']
        option_b = request.form['option_b']
        option_c = request.form['option_c']
        correct = request.form['correct']
        new_test = Test(question=question, option_a=option_a, option_b=option_b, option_c=option_c, correct=correct)
        db.session.add(new_test)
        db.session.commit()
        flash('Test added successfully.')
        return redirect(url_for('home'))
    return render_template('add_test.html')

@app.route('/take_test/<int:test_id>', methods=['GET', 'POST'])
def take_test(test_id):
    if 'user_id' not in session:
        flash('Please login to take the test.')
        return redirect(url_for('login'))
    test = Test.query.get_or_404(test_id)
    result = None
    if request.method == 'POST':
        answer = request.form['answer']
        result = 'Correct!' if answer == test.correct else 'Incorrect!'
    return render_template('take_test.html', test=test, result=result)

@app.route('/tests')
def tests():
    all_tests = Test.query.all()
    return render_template('tests.html', tests=all_tests)

if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0', port=5000)
