FROM python:3.11
WORKDIR /fsrc

COPY ./requirements.txt /fsrc/requirements.txt 
RUN pip install --no-cache-dir --upgrade -r /fsrc/requirements.txt
COPY ./app /fsrc/app
EXPOSE 5100
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "5100"]