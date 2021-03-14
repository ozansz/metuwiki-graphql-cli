LOGIN = """mutation {{
    authentication {{
        login(username: \"{username}\", password: \"{passwd}\", strategy: \"local\") {{
            jwt
        }}
    }}
}}"""

CREATE_PAGE = """mutation Page {{
  pages {{
    create (content: "{content}", description: "{desc}", editor: "{editor}", isPublished: {is_published}, isPrivate: {is_private}, locale: "{locale}", path: "{path}", tags: {tags}, title: "{title}") {{
      responseResult {{
        succeeded,
        errorCode,
        slug,
        message
      }},
      page {{
        id,
        path,
        title
      }}
    }}
  }}
}}"""