from fastapi import APIRouter, HTTPException
from app.services.aws_service import get_bucket_info

router = APIRouter()

@router.get("/s3", status_code=200)
def get_buckets():
    try:
        return get_bucket_info()
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)   # <-- show real error (important)
        )

