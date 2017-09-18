FROM python:3
RUN mkdir /src
WORKDIR /src
ADD requirements.txt /src/
RUN pip3 install -r /src/requirements.txt
ENV PIZZA_ADMIN_PAGE_LOGIN admin
ENV PIZZA_ADMIN_PAGE_PASSWORD Admin
ENV PIZZA_ADMIN_PAGE_SECRET_KEY pizza secret key
ENV PATH_TO_PIZZA_DB pizza.db
ENV PIZZA_BOT_TOKEN _put_here_Your_token_
ENV FLASK_HOST 0.0.0.0
ADD . /src/
