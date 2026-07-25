from fastapi import APIRouter

from app.models import AgentRequest
from app.agent import run_agent
from app.tools import get_current_time

router = APIRouter()


@router.get("/health")

def health():

    return {

        "status": "healthy",

        "service": "AI Agent API"

    }


@router.get("/time")

def current_time():

    return {

        "time": get_current_time()

    }


@router.post("/agent")

def agent(data: AgentRequest):

    answer = run_agent(data.task)

    return {

        "result": answer

    }
