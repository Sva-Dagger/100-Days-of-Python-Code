from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String

app = Flask(__name__)
app.secret_key = "ggfdcbvchgfhgvjg"  # Needed for flashing messages

# Define base for SQLAlchemy ORM
class Base(DeclarativeBase):
    pass

# Flask configuration for SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///login.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy with custom model base
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Define Sign_in model
class Sign_in(db.Model):
    __tablename__ = 'user_sign_in'  # Changed to avoid spaces in table name
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(250), nullable=False)

    def __repr__(self):
        return f'<Sign_in {self.name}>'

# Create database table
with app.app_context():
    db.create_all()

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get('confirm_password')

        # Basic validation
        if not name or not email or not password:
            return render_template('error.html')

        if password != confirm_password:
            flash("Passwords do not match", "error")
            return render_template('error.html')

        # Check if email already exists
        existing_user = Sign_in.query.filter_by(email=email).first()
        if existing_user:
            flash("Email is already registered.", "error")
            return render_template('error.html')

        # Add new user to the database
        new_user = Sign_in(name=name, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        flash(f"Signup successful! Welcome, {name}!", "success")
        return redirect(url_for('home'))

    return render_template('sign_up.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")

        # Check if user exists
        user = Sign_in.query.filter_by(email=email).first()

        if not user:
            flash("Email not found", "error")
            return render_template('error.html')

        # Check if password matches
        if user.password != password:
            flash("Password incorrect", "error")
            return render_template('error.html')

        return redirect(url_for('home'))

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
