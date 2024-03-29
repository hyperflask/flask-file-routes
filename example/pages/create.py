from app import POSTS

def POST():
    slug = request.form["title"].lower().replace(" ", "-")
    POSTS.append({
        "slug": slug,
        "title": request.form["title"],
        "content": request.form["content"]
    })
    return redirect(url_for("[slug]", slug=slug))
