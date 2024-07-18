def serialize_session(session) -> dict:
    return {
        "id": str(session["_id"]),
        "conversations": session["conversations"],
        "generated_response": session["generated_response"]
    }


def serialize_post(post) -> dict:
    return {
        "id": str(post["_id"]),
        "json_content": post["json_content"],
    }


def serial_list_posts(posts) -> list:
    return [serialize_post(post) for post in posts]
