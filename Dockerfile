FROM debian:buster as compiler

RUN apt-get update && apt-get upgrade -y

RUN apt-get install -y build-essential git

WORKDIR /src/

RUN git clone https://github.com/festvox/flite.git

WORKDIR /src/flite/

RUN git checkout tags/v2.2

RUN ./configure

RUN make


FROM python:3.8.7-buster

RUN apt-get update && apt-get upgrade -y

WORKDIR /app/

COPY --from=compiler /src/flite/bin/flite .

COPY requirements/app.txt requirements.txt

RUN pip install -r requirements.txt

COPY src/ .

ENV FLASK_APP=main.py

CMD [ "python", "-m", "flask", "run", "--host=0.0.0.0" ]
