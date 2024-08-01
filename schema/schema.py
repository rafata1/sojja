def serialize_session(session) -> dict:
    return {
        "id": str(session["_id"]),
        "generated_response": session.get("generated_response", None),
        "topic": session.get("topic", None),
        "num_images": session.get("num_images", None),
        "num_words": session.get("num_words", None),
        "keywords": session.get("keywords", None),
        "description": session.get("description", None),
        "status": session.get("status", "pending"),
    }


def serialize_post(post) -> dict:
    return {
        "id": str(post["_id"]),
        "stt": post.get("stt", 100),
        "json_content": post["json_content"],
    }


def serial_list_posts(posts) -> list:
    stt = 0
    result = []
    for post in posts:
        stt += 1
        post["stt"] = stt
        result.append(serialize_post(post))
    result.reverse()
    return result
