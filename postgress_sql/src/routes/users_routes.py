from fastapi import APIRouter , Depends , HTTPException
from models.todo_models import Users
from config.database import  get_db
from sqlalchemy.orm import Session
from validations.validation import UserCreate , UserLogin
from utils.utils_helper import create_access_token


user_route = APIRouter()

@user_route.post("/create/")
def create_user( user : UserCreate , db: Session = Depends(get_db) ):
    try:
        db_user = Users(name = user.name , mail=user.mail , password= user.password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except Exception as e:
        db.rollback()
        return {
            'error' : str(e),
            'massage' : 'Error',
            'status': 'failed'
        }
    return {
            "data": db_user,
            "massage": "User Created",
            "status": "success"
        }


@user_route.post("/login/")
def user_login( user : UserLogin , db: Session = Depends(get_db) ):
    try:
        db_user = db.query(Users).filter(Users.mail == user.mail).first()
        if not user:
            raise HTTPException(status_code=404 , detail= "User Not Found")
        if user.password != db_user.password:
            raise HTTPException(status_code=404 , detail= 'Invalid User')
        token = create_access_token (data= {'sub':user.mail})
        user_data = {
            'name' : db_user.name,
            'mail' : db_user.mail,
            "token" : token
        }
    except Exception as e:
        return {
            'error' : str(e),
            'massage' : 'Error',
            'status': 'failed'
        }
    return {
            "data": user_data,
            "massage": "User Logged In",
            "status": "success"
        }

