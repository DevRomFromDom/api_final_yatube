# Social site Yatube!

## Description

It`s a social site project **Yatube**. In this project you can make posts, comments etc. Like other social sites do. The main reason of this project is research of python development with Django.

# Build and start

-   Clone repository ( git clone + 'link' or download it like a ZIP file );
-   Go in root of the project (cmd/...>: cd api_final_yatube );
-   Install virtual environment ( python -m venv venv );
-   Download all requirements ( pip install -r requirements.txt );# Social site Yatube!

## Description

It`s a social site project **Yatube**. In this project you can make posts, coments etc. Like other social sites do. The main reason of this project is research of python development with Django.

# Build and start

-   Clone repository ( git clone + 'link' or download it like a ZIP file );
-   Go in root of the project (cmd/...>: cd api_final_yatube );
-   Install virtual environment ( python -m venv venv );
-   Download all requirements ( pip install -r requirements.txt );
-   Enter the root folder (cmd/...>: cd yatube_api );
-   Run server (cmd/...>: python manage.py runserver );
-   Enjoy (^ \_ ^)

# Usage

All save methods can be used by not authenticated user.
**If you need to use all methods, create JWT token with JWT methods.**
**More info about methods you can find in Docs**

-   **Run server and go to http://127.0.0.1:8000/redoc/**

### Posts methods

-   GET - '/api/v1/posts/', will return all posts;
-   POST - '/api/v1/posts/', make a new post with:

    -   text: string(required),
    -   group ( integer or null (id сообщества),
    -   image( string or null < binary >)

-   PUT and PATCH - '/api/v1/posts/{post_id}' edit your post with:
    -   text: string(required),
    -   group ( integer or null ( id сообщества ),
    -   image( string or null < binary >)
-   DELETE '/api/v1/posts/{post_id}' delete your post;

### Groups methods

-   GET - '/api/v1/groups/', will return all groups;

-   GET - '/api/v1/groups/{group_id}', will return group by passed id;

### Comments methods

-   GET - '/api/v1/posts/{post_id}/comments/', will return all comments of post;
-   POST - '/api/v1/posts/{post_id}/comments/', make a new comment for post with:

    -   text: string(required),

-   PUT and PATCH - '/api/v1/posts/{post_id}/comments/{comment_id}/', edit your comment with:
    -   text: string(required),
-   DELETE '/api/v1/posts/{post_id}/comments/{comment_id}/', delete your comment;

### Follow methods

-   GET - '/api/v1/follow/', will return all your follows;

-   POST - '/api/v1/follow/', make a new follow with:
    -   following : string (required)

### JWT token methods

-   POST - '/api/v1/users/', create new user with:

    -   email (optional)
    -   username: string,
    -   password: string;

-   POST - '/api/v1/jwt/create/', make a tokens for user:
    -   username: string,
    -   password: string;
-   POST - '/api/v1/jwt/refresh/', reftesh your token:
    -   refresh (token): string,
-   POST - '/api/v1/jwt/verify/', cheack your token as valid or not:

    -   token: string,

-   Enter the root folder (cmd/...>: cd yatube_api );
-   Run server (cmd/...>: python manage.py runserver );
-   Enjoy (^ _ ^)
