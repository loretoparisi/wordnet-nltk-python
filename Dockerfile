#
# WordNet NLTK Examples
# @author Loreto Parisi (loretoparisi gmail dot com)
# Copyright (c) 2021 Loreto Parisi
#

FROM python:3.7.4-slim-buster

LABEL maintainer Loreto Parisi loretoparisi@gmai.com

WORKDIR app

# app requirements
COPY src/requirements.txt requirements.txt
RUN pip install -r requirements.txt

CMD ["bash"]
