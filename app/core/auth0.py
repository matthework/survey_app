from fastapi import Depends, HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt
from urllib.request import urlopen
import json, ssl
from app.core.config import settings

token_auth_scheme = HTTPBearer()
JWKS_URL = f"https://{settings.AUTH0_DOMAIN}/.well-known/jwks.json"
ALGORITHMS = [settings.ALGORITHMS]

def get_jwks():
    context = ssl._create_unverified_context()
    with urlopen(JWKS_URL, context=context) as response:
        return json.load(response)

def verify_jwt(token: str):
    jwks = get_jwks()
    unverified_header = jwt.get_unverified_header(token)
    rsa_key = {}
    for key in jwks["keys"]:
        if key["kid"] == unverified_header["kid"]:
            rsa_key = {
                "kty": key["kty"],
                "kid": key["kid"],
                "use": key["use"],
                "n": key["n"],
                "e": key["e"],
            }
    if rsa_key:
        return jwt.decode(
            token,
            rsa_key,
            algorithms=ALGORITHMS,
            audience=settings.API_AUDIENCE,
            issuer=f"https://{settings.AUTH0_DOMAIN}/"
        )
    raise HTTPException(status_code=401, detail="Token validation failed")

def get_current_user(token: HTTPAuthorizationCredentials = Depends(token_auth_scheme)):
    return verify_jwt(token.credentials)

def get_role_user(required_roles: list[str]):
    def role_dependency(user=Depends(get_current_user)):
        roles = user.get("https://yourdomain.com/roles", [])
        if not any(role in roles for role in required_roles):
            raise HTTPException(status_code=403, detail="Forbidden")
        return user
    return role_dependency