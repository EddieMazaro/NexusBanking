from fastapi import FastAPI
app = FastAPI(
    title="Nexus Banking API",
    description="A scalable banking platform API",
    version="0.1.0"
)

app.get("/")
async def root():
    return {"message": "Welcome to Nexus Banking API"}

@app.get("/health")
async def health_check():
    return{"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)