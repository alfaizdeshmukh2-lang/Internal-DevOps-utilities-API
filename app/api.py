from fastapi import FastAPI
from app.routers import metrics , aws

app = FastAPI(
          title = "Internal DevOps Utilities API",
          description = """This is an Internal API Utilities APP for Monitoring metrics , AWS Usage , Log Analysis, etc""",
          version = "1.0.0", 
          redoc_url = "/redocs"
)
@app.get("/")             
def hello():
          """
          This is a Hello API , just for testing 
          """
          return {"message":"Hello Dosto , This is DevOps utilities API EX "}

app.include_router(metrics.router)
app.include_router(aws.router, prefix ="/aws")



