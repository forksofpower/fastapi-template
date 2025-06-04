FROM python:3.14-slim

WORKDIR /code

# Install UV
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Create and activate virtual environment
RUN uv venv /opt/venv
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Include dependency files
COPY pyproject.toml uv.lock /code/

# Install dependencies
RUN uv pip install --no-cache-dir -r pyproject.toml

# Copy application code
COPY ./app /code/app
COPY ./version.py /code/
COPY ./.env /code/
COPY ./.env.dev /code/

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]