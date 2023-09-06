FROM python:3.8.5
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

ENV TZ=America/Vancouver
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY . .
WORKDIR /app

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

EXPOSE 1234

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "1234"]
