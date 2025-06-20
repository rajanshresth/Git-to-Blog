# Use the official AWS Lambda Python base image
FROM public.ecr.aws/lambda/python:3.11

# Install uv (fast Python package manager)
RUN pip install --upgrade pip && pip install uv

# Set working directory
WORKDIR /var/task

# Copy only dependency files first for better caching
COPY pyproject.toml .
COPY uv.lock . 

# Install dependencies into the system Python environment
RUN uv sync --system --locked || uv pip install --system .

# Copy the rest of your application code
COPY . .

# Set the Lambda handler (module.function)
CMD ["app.main.handler"]
