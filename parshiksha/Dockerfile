FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /coolcode
WORKDIR /coolcode
COPY requirements.txt /coolcode/
RUN pip install -r requirements.txt
COPY . /coolcode/