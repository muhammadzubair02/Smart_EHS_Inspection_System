from fastapi import FastAPI

# Create the FastAPI application
app = FastAPI(
    title="Smart EHS Inspection System",
    description="Digital Inspection and Maintenance Management System",
    version="1.0.0",
)


@app.get("/")
def root():
    """Welcome message and running status."""
    return {
        "message": "Welcome to the Smart EHS Inspection System",
        "status": "running",
    }


@app.get("/health")
def health():
    """Health check endpoint."""
    return {"status": "healthy"}
