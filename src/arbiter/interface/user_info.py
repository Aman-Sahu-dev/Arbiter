
from typing import Any
from arbiter.interface.prompts import  ask_float, ask_text

def ask_user_info() -> dict[str,Any]:
    return {
    "name": ask_text("Name"),
    "credit_limit": ask_float("Credit_Limit",1000.00),
    "platforms": [ask_text("Platforms")],
    "current_debt": ask_float("Debt",0.00),
    "Safety Buffer": ask_text("In Hand Cash") 
    }


