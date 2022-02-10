from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import get_db, engine
import schemas, custom_model1

app = FastAPI()
custom_model1.Base.metadata.create_all(engine)
# employee = get_db.Table('employee', get_db.metadata)

@app.get('/') #TODO: 
def test(db:Session = Depends(get_db)):
    post = db.query(custom_model1.Band).all()
    # for r in post:
        # p = r.First_name
    return ("hello world",  post)

# @app.post('all/')
# def allmodels(user:schemas.Blogger, db:Session = Depends(get_db)):
#     post = models.BlogDetails(title = user.title, summary=user.summary)
#     db.add(post)
#     db.commit()
#     db.refresh(post)
#     return post