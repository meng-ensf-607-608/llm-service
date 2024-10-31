FROM python:3.11-slim
ENV PYTHONUNBUFFERED True

ENV APP_HOME /llm-service
WORKDIR $APP_HOME
COPY src $APP_HOME/src
COPY Pipfile Pipfile.lock serve.py $APP_HOME/

RUN pip install --upgrade pip
RUN pip install pipenv && pipenv install --system --deploy

EXPOSE 8080
CMD ["python", "serve.py"]