import requests

from .queries import LOGIN, CREATE_PAGE

def _graphql_request(query):
    return requests.post("https://wiki.metu.life/graphql", json={
        "operationName": None,
        "variables": {},
        "query": query
    })

def login(email, passwd):
    res = _graphql_request(LOGIN.format(username=email, passwd=passwd))

    try:
        return res.json()["data"]["authentication"]["login"]["jwt"]
    except:
        return None

def create_page(content, desc, editor, is_published, is_private, locale, path, tags, title):
    res = _graphql_request(CREATE_PAGE.format(
        content=content,
        desc=desc,
        editor=editor,
        is_published=is_published,
        is_private=is_private,
        locale=locale,
        path=path,
        tags=tags,
        title=title
    ))

    try:
        return res.json()["data"]
    except:
        return None