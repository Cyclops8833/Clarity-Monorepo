from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Issue(BaseModel):
    title: str
    link: str
    source: str

@app.get("/top-issues", response_model=list[Issue])
def get_top_issues():
    # TODO: replace with your news-fetch logic
    return [
        Issue(title="Sample Issue", link="https://example.com", source="Example News")
