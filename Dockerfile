FROM agrigorev/zoomcamp-model:2025

# Install uv (modern dependency manager)
RUN pip install uv

# Set working directory
WORKDIR /app

# Copy dependency files
COPY ["pyproject.toml", "uv.lock", "./"]

# Install dependencies into system Python
RUN uv pip install --system .

# Copy application files
COPY ["fastapi_python_predict.py", "pipeline_v1.bin", "./"]

# Expose FastAPI port
EXPOSE 8000

# Start FastAPI app
ENTRYPOINT ["uvicorn", "fastapi_python_predict:app", "--host", "0.0.0.0", "--port", "9696"]

