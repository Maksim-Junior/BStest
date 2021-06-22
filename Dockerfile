FROM python:3.6-slim
MAINTAINER maks.kurakevich@gmail.com
COPY . /BStest
WORKDIR /BStest
RUN pip install --no-cache-dir -r requirements.txt
RUN ["pytest", "-v", "--junitxml=reports/result.xml"]
CMD tail -f /dev/null