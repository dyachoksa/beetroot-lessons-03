import asyncio
import random
import time

from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route


async def fake_db_query(message, delay=3):
    print("Query:", message)
    print("Delay:", delay)
    await asyncio.sleep(delay)

    return random.randint(1, 100)


async def homepage(request):
    start_time = time.perf_counter()
    
    delay = random.randint(1, 10)
    result = await fake_db_query("select count(*) from users", delay=delay)

    end_time = time.perf_counter()
    run_time = end_time - start_time

    metric = f"Finished {homepage.__name__!r} in {run_time:.4f} secs"

    return JSONResponse({
        "success": True, 
        "total_users": result,
        "metrics": {
            "delay": delay,
            "message": metric
        }
    })


app = Starlette(debug=True, routes=[
    Route('/', homepage),
])
