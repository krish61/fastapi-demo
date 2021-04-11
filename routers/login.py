from app.token import create_access_token
from app.hashing import Hash
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from starlette.exceptions import HTTPException
from app import schemas, database, models
router = APIRouter(prefix='/login', tags=['authentication'])

get_db = database.get_db
session = database.Session

@router.post('/', status_code=200)
async def login(request:OAuth2PasswordRequestForm=Depends(), db:session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.email==request.username).first()
    if not user:
        raise HTTPException(status_code=400, detail="Invalid Credentials")
    if not Hash().verify(user.password, request.password):
        raise HTTPException(status_code=400, detail="Invalid password")
    access_token = create_access_token({'sub':user.email})
    return {"access_token": access_token, "token_type": "bearer"}

# def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):