from os import getenv
from typing import Dict, List, Tuple

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from GoogleNews import GoogleNews


app = FastAPI(debug=True if getenv("ENVIRONMENT") == "DEVELOP" else False)
googlenews = GoogleNews(lang='en', period="7d", encode='utf-8')


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5500",
        "https://igormcsouza.github.io"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class RequestBody(BaseModel):
    topic: str


ResponseType = Dict[str, List[Tuple[str, str, str]]]


class ResponseBody(BaseModel):
    headlines: ResponseType


@app.post("/fetch")
def fetch(body: RequestBody) -> ResponseType:

    try:
        googlenews.get_news(body.topic)
        top: List[dict] = googlenews.results(sort=True)
    except Exception as e:
        raise HTTPException(status_code=500,
                            detail="Error fetching news from Google, %s" % e)

    parse = [(t['title'], t['link'], t['date']) for t in top]

    return {'headlines': parse}
