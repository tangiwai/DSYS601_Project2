FROM python:3.9-slim

# Install Nano
RUN apt-get update && apt-get install -y nano

WORKDIR /app

COPY assessment_code.py .
COPY network_equipment.json .

RUN pip install Flask

EXPOSE 5050

CMD ["python", "assessment_code.py"]

