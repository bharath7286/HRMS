from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_cognito import CognitoAuth

bp = Blueprint('auth', __name__, url_prefix='/auth')

cognito = CognitoAuth()

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        try:
            cognito_auth_response = cognito.authenticate()  # Authenticate via Cognito
            session['user'] = cognito_auth_response  # Store user data in session
            flash('Logged in successfully!', 'success')
            return redirect(url_for('dashboard.index'))
        except Exception as e:
            flash(f'Login failed: {str(e)}', 'danger')
    return render_template('auth/login.html')

@bp.route('/logout')
def logout():
    session.clear()  # Clear Cognito session
    flash('Logged out successfully!', 'success')
    return redirect(url_for('auth.login'))
