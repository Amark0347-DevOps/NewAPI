from jose import JWTError, jwt
from fastapi import Depends, HTTPException, status
from datetime import timedelta, datetime
from ..core.config import settings
from fastapi import  Header
##################################################################
async def create_access_token(data:dict,expires_delta:timedelta):
    data_copy = data.copy()
    total_time = datetime.utcnow() + expires_delta
    data_copy.update({"exp":total_time})
    token = jwt.encode(data_copy,settings.jwt_secret_key, algorithm=settings.jwt_algorithem)
    return token
####################################################################################################

##################################################################################################
async def decode_access_token(token:str):
    credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not Validate Credentials",
    headers={"WWW-Authenticate": "Bearer"})

    try:
        payload = jwt.decode(token, settings.jwt_secret_key, algorithms=settings.jwt_algorithem)
        # if payload is None:
        #     expiration_datetime = datetime.utcfromtimestamp(payload["exp"])
        #     current_datetime = datetime.utcnow()
        #     if expiration_datetime < current_datetime:
        #         raise HTTPException(
        #             status_code=status.HTTP_401_UNAUTHORIZED,
        #             detail="Token has expired",
        #             headers={"WWW-Authenticate": "Bearer"})
        #     else:
        #         return payload
        return payload
    except JWTError:
        raise credentials_exception

####################################################################################################
# async def root(request: Request):
#     re = request.headers.get("Authorization")
#     if re is None:
#         raise HTTPException(detail="Unauthorized Access", status_code=status.HTTP_401_UNAUTHORIZED)
#     else:
#         return re.removeprefix("Bearer ")
async def root(token: str = Header(..., alias="Authorization")):
    if token is None:
        raise HTTPException(detail="Unauthorized Access", status_code=status.HTTP_401_UNAUTHORIZED)
    else:
        return token.removeprefix("Bearer ")

####################################################################################################
async def GetCurrentUser(token:str = Depends(root)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"})
    
    payload = await decode_access_token(token)
    if payload is None:
        raise credentials_exception
    else:
        return payload
    