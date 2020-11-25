FROM python:3
ENV PYTHONUNBUFFERED=1
RUN mkdir /calculator_dir
WORKDIR /calculator_dir
ADD requirements.txt /calculator_dir
COPY requirements.txt /calculator_dir
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /calculator_dir