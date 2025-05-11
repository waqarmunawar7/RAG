from jose import JWTError, jwt
from config import setting


class Auth():

    def create_access_token():
        token = jwt.encode(setting.allowed_host[0],setting.auth_key,setting.algorithm)
        print(token)