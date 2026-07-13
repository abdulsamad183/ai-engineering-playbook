---
title: "Authentication Module Template"
description: "Auth module structure for FastAPI AI backends."
type: backend-template
---

# Authentication Module Template

## Directory

```
src/my_ai_api/auth/
├── __init__.py
├── dependencies.py      # get_current_user, require_permission
├── jwt.py               # Token create/validate
├── api_keys.py          # API key validation
├── models.py            # User, TokenPayload schemas
└── exceptions.py        # Auth-specific errors
```

## JWT Dependency

```python
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from my_ai_api.auth.jwt import decode_access_token
from my_ai_api.auth.models import TokenPayload

security = HTTPBearer()


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
) -> TokenPayload:
    try:
        return decode_access_token(credentials.credentials)
    except TokenExpiredError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expired")
    except InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
```

## Permission Check

```python
def require_permission(permission: str):
    async def checker(user: TokenPayload = Depends(get_current_user)) -> TokenPayload:
        if permission not in user.permissions:
            raise HTTPException(status_code=403, detail="Insufficient permissions")
        return user
    return checker
```

## See Also

- [Authentication and Authorization for AI](../../../domains/security/authentication-authorization-for-ai.md)
