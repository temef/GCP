ARG PYTHON_VERSION=""

FROM python:${PYTHON_VERSION}

WORKDIR /app

COPY . .

RUN pip3 install pylint

RUN pip3 install pytest

RUN pip3 install pytest nbmake

RUN pip3 install wheel

#####
