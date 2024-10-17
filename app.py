from fastapi import FastAPI, HTTPException
from starlette import status
import requests


app = FastAPI()

async def get_api_records(api_url):
    url = f"https://mangatracker-502816012135.us-central1.run.app/{api_url}"
    print(url)
    response = requests.get(url=url)
    if response.status_code == 200:
        data = response.json()  # Parse JSON response
        return data
    else:
        return {'error': 'Failed to fetch data'}, response.status_code

@app.get('/', status_code=status.HTTP_200_OK)
async def homepage():
    try:
        return {"Hi Hello!!!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@app.get('/manga', status_code=status.HTTP_200_OK)
async def get_all_links():
    try:
        records = await get_api_records('api/links')
        return records
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")