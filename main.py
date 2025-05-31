import uvicorn
import os
from fastapi import FastAPI
from Config.db import engine, Base
from Routes import router as ApiRouter

app = FastAPI()

@app.on_event("startup")
def on_startup():
    try:
        Base.metadata.create_all(bind=engine)
        print("✅ Database connected and initialized")
    except Exception as e:
        print(f"❌ Error connecting to DB: {e}")

@app.on_event("shutdown")
def on_shutdown():
    engine.dispose()
    print("🛑 Database connection closed")

app.include_router(ApiRouter)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8006))  # fallback to 8000
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)
