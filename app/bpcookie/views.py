from . import cook_bp
from flask import session, redirect, url_for, request, make_response


@cook_bp.route('/set_user/<int:user_id>')
def set_user(user_id):
    session['user_id'] = user_id  # Зберігаємо user_id в сесії
    return f'User ID {user_id} has been set!'

@cook_bp.route('/get_user')
def get_user():
    if 'user_id' in session:
        user_id = session['user_id']  # Отримуємо user_id з сесії
        return f'Current user ID is {user_id}'
    return 'No user ID set in session!'

@cook_bp.route('/del_user')
def delete_user():
    if 'user_id' in session:
        user_id = session.pop('user_id')
        return f'Current user ID={user_id} was deleted!'
    return redirect(url_for("get_user"))

@cook_bp.route('/clear_session')
def clear_session():
    session.clear()  # Очищує всю сесію
    return "Сесія очищена"

from datetime import datetime, timedelta

@cook_bp.route('/set_cookie')
def set_cookie():
    response = make_response('Кука встановлена')
    # response.set_cookie('username', 'student', expires=datetime.now()+timedelta(seconds=10))
    response.set_cookie('username', 'student', max_age=timedelta(seconds=10))
    return response

@cook_bp.route('/get_cookie')
def get_cookie():
    username = request.cookies.get('username')
    return f'Користувач: {username}'

@cook_bp.route('/delete_cookie')
def delete_cookie():
    response = make_response('Кука видалена')
    response.set_cookie('username', '', expires=0) # response.set_cookie('username', '', max_age=0)
    return response

