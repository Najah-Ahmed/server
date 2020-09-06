from itsdangerous import URLSafeTimedSerializer

from config import SECRET_KEY, SECURITY_PASSWORD_SALT


def generate_confirmation_token(email):
    serializer = URLSafeTimedSerializer(SECRET_KEY)
    return serializer.dumps(email, salt=SECURITY_PASSWORD_SALT)


def confirm_token(token, expiration):
    serializer = URLSafeTimedSerializer(SECRET_KEY)
    try:
        email = serializer.loads(
            token, salt=SECURITY_PASSWORD_SALT, max_age=expiration)
    except:
        return {'error': "Invalid Token"}
    return email
