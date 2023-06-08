# Inside the DSYS601_Project2 directory create a Dockerfile
echo "FROM python:3.9-slim

WORKDIR /app

COPY assessment_code.py .
COPY network_equipment.json .

RUN pip install Flask

EXPOSE 5050

CMD [\"python\", \"assessment_code.py\"]" > Dockerfile

# Commit and push the Dockerfile
git add Dockerfile
git commit -m "Add Dockerfile"
git push
