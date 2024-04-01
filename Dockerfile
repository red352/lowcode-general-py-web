FROM python:3.9.13-slim

ARG root=/app

WORKDIR ${root}

COPY . .

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python", "app.py"]

