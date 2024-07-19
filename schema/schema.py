def serialize_session(session) -> dict:
    return {
        "id": str(session["_id"]),
        "generated_response": session.get("generated_response", None),
        "topic": session.get("topic", None),
        "num_images": session.get("num_images", None),
        "num_words": session.get("num_words", None),
        "keywords": session.get("keywords", None),
        "description": session.get("description", None),
    }


def serialize_post(post) -> dict:
    return {
        "id": str(post["_id"]),
        "json_content": post["json_content"],
    }


def serial_list_posts(posts) -> list:
    return [serialize_post(post) for post in posts]
