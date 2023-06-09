from fastapi import FastAPI
from  pydantic import BaseModel
from typing import Text, Optional
from datetime import datetime
from uuid import uuid4 as uuid
import app.modelv1 as modelv1

posts = []

class Post(BaseModel):
    id: Optional[str]
    content: Text
    created_at: datetime = datetime.now()
    calification: Optional[str]
    

app = FastAPI()

origins = [
    "http://localhost:4200",
    "https://vdgutierrez.github.io/frontendToxic",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)


@app.post('/comment')
def post_comment(post: Post):
    post.id = str(uuid())
 
    clss = modelv1.Predictor()
    pres = clss.pred(str(post.content))
  
    return {"data": { "id": post.id, "score": pres} , "message": "created", "status": True}
