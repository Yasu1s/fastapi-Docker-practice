FROM python:3.11-slim
WORKDIR /fastapi-app
COPY . /fastapi-app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 80
CMD ["uvicorn", "fastapi-app.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]