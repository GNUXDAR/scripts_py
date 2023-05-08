from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin):

    def __init__(self, id, name, email, password, is_admin=False):
        self.id = id
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)
        self.is_admin = is_admin

    def set_password(self, password):
        """Envio de contraseñas"""
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """verificar contraseña de usuario"""
        return check_password_hash(self.password, password)

    def __repr__(self):
        """retornar email"""
        return '<User {}>'.format(self.email)
    

users = []

def get_user(email):
    """obtener el correo del usuario"""
    for user in users:
        if user.email == email:
            return user
    return None
