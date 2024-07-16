def serialize_session(session) -> dict:
    return {
        "id": str(session["_id"]),
        "conversations": session["conversations"],
        "generated_response": session["generated_response"]
    }
