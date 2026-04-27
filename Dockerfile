# Using python as a base. slim is small version of python (lighter)
FROM python:3.12-slim

# Create folder in /app folder
WORKDIR /app

# Copy library list file into container
COPY requirements.txt .

# install library 
RUN pip install --no-cache-dir -r requirements.txt

# Copy API code into container
COPY ./app ./app

# Tell Docker that we're gonna use container no.8000
EXPOSE 8000

# Set container to start running right after PC is boosted.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]