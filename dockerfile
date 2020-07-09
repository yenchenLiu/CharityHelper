FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt .

RUN python3 -m pip install -r requirements.txt

COPY ./ ./

EXPOSE 8000

CMD uvicorn app.main:app --reload
