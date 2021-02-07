FROM ubuntu:20.04 as compiler

RUN apt-get update && apt-get upgrade -y

RUN apt-get install -y build-essential git

WORKDIR /src/

RUN git clone https://github.com/festvox/flite.git

WORKDIR /src/flite/

RUN ./configure

RUN make


FROM ubuntu:20.04

RUN apt-get update && apt-get upgrade -y

WORKDIR /flite/

COPY --from=compiler /src/flite/bin/flite .

CMD [ "/flite/flite", "'Flite is a small fast run-time synthesis engine'", "flite.wav" ]
