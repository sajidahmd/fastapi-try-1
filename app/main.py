from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from app.config.database import engine, Base
from app.controllers import user_controller

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="My API",
    description="Converted from Laravel",
    version="1.0.0"
)

# CORS middleware (similar to Laravel CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure as needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers (similar to Laravel Route groups)
app.include_router(user_controller.router, prefix="/api/v1", tags=["users"])


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)