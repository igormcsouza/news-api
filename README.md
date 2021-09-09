# News Api

These days I figured out would be a great idea to have news on my website.
So I decide to create this api to support this feature.
It fetches news from Google News Section, bringing useful info about the news.
Visit **/docs** to see how to use this api.

## How to develop

This project has a [docker-compose.yml](docker-compose.yml) file to manage
the container. Utilize it to run whatsoever you might need.

1. How to start: Start by running the following command. Remember you need to
change ports on docker-compose if that (8001) is already taken.

    ```bash
    app$ docker-compose up --build
    ```

2. How to test: Use the [test_app.py](test_app.py) file to test the api. After
that run the command below to run the tests.

    ```bash
    app$ docker-compose build
    app$ docker-compose run web pytest
    ```

## Troubleshooting

*_Heroku app is not not working Code H14_: This is an error with Heroku that
does not start the dyno when we push a container. See
[this](https://stackoverflow.com/questions/41804507/h14-error-in-heroku-no-web-processes-running)
to understand it better and get the fix to it.
