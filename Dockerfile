FROM python:3.10
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application code into the container
COPY . .

ENV PYTHONDONTWRITEBYTECODE=1  
ENV PYTHONUNBUFFERED=1     

EXPOSE 8000

CMD ["bash"]
