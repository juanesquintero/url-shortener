FROM python:3.11.1 AS development

WORKDIR /code

# Update pip
RUN pip install --upgrade pip

# Copy resources
COPY . /code

# Install requirements (dev)
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements-dev.txt

# Expose port
EXPOSE 80


FROM python:3.11.1 AS production

WORKDIR /code
# Update pip
RUN pip install --upgrade pip
# Copy resources
COPY . /code
# Install requirements (prod)
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
# Expose port
EXPOSE 80