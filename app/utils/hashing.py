from werkzeug.security import generate_password_hash, check_password_hash
from config.dotenv import env

class Hashing:
    
    def generateHash(self, password: str) -> str:
        password = env['SECRET_HASH'] + password
        return generate_password_hash(password, env['METHOD_HASH'], int(env['SALT_INT'])).replace(f"{env['METHOD_HASH']}:600000$", '')
    
    
    def CheckHash(self, password_hashed, password) -> bool:
        password = env['SECRET_HASH'] + password
        password_hashed = f"{env['METHOD_HASH']}:600000$" + password_hashed
        return check_password_hash(password_hashed, password)