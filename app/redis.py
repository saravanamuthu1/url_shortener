import redis.asyncio as redis

# Created once at module level
redis_client = redis.from_url(
    "redis://localhost:6379",
    decode_responses=True
)

# Dependency
async def get_redis():
    yield redis_client