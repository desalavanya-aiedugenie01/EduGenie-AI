from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field

from qna import answer_question
from explanation_module import explain_concept
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations


app = FastAPI(
    title="EduGenie",
    description="Google Gemini Powered Learning Assistant",
    version="1.0.0"
)


# --------------------------------------------------
# Static files
# --------------------------------------------------

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)


# --------------------------------------------------
# Templates
# --------------------------------------------------

templates = Jinja2Templates(
    directory="templates"
)


# --------------------------------------------------
# Request Model
# --------------------------------------------------

class TextRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=1,
        max_length=20000
    )


# --------------------------------------------------
# Home Page
# --------------------------------------------------

@app.get(
    "/",
    response_class=HTMLResponse
)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request
        }
    )


# --------------------------------------------------
# Health Check
# --------------------------------------------------

@app.get("/health")
async def health():

    return {
        "status": "ok",
        "service": "EduGenie"
    }


# --------------------------------------------------
# Q&A API
# --------------------------------------------------

@app.post("/qa")
async def qa(payload: TextRequest):

    try:

        result = answer_question(
            payload.text
        )

        return {
            "result": result
        }

    except Exception as exc:

        raise HTTPException(
            status_code=500,
            detail=str(exc)
        )


# --------------------------------------------------
# Explanation API
# --------------------------------------------------

@app.post("/explain")
async def explain(payload: TextRequest):

    try:

        result = explain_concept(
            payload.text
        )

        return {
            "result": result
        }

    except Exception as exc:

        raise HTTPException(
            status_code=500,
            detail=str(exc)
        )


# --------------------------------------------------
# Quiz API
# --------------------------------------------------

@app.post("/quiz")
async def quiz(payload: TextRequest):

    try:

        result = generate_quiz(
            payload.text
        )

        return {
            "result": result
        }

    except Exception as exc:

        raise HTTPException(
            status_code=500,
            detail=str(exc)
        )


# --------------------------------------------------
# Summary API
# --------------------------------------------------

@app.post("/summarize")
async def summarize(payload: TextRequest):

    try:

        result = summarize_text(
            payload.text
        )

        return {
            "result": result
        }

    except Exception as exc:

        raise HTTPException(
            status_code=500,
            detail=str(exc)
        )


# --------------------------------------------------
# Learning Recommendation API
# --------------------------------------------------

@app.post("/learn/recommendations")
async def recommendations(
    payload: TextRequest
):

    try:

        result = get_learning_recommendations(
            payload.text
        )

        return {
            "result": result
        }

    except Exception as exc:

        raise HTTPException(
            status_code=500,
            detail=str(exc)
        )