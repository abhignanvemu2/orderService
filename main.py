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
