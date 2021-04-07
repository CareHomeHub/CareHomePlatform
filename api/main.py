""" 
main.py
"""
import json
import logging
import requests
import pandas as pd
# from .gdb import load_data as seed_db 
# from .gdb import magic_cypher as seed_magic 
# from .gdb_neo4j import seed_loc_data as seed_loc
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from typing import List
from pydantic import BaseModel
from py2neo import Graph

# seed_db()
# seed_loc()
# seed_magic()

data = [
    {
        "loc_id": "1-112787350",
        "typ": "Social Care Org",
        "name": "Mosaic Care Group Limited",
        "rating": "Requires improvement",
        "numberOfBeds": 0,
        "postcode": "PR2 1JR",
        "lat": -2.739045,
        "lng": 53.77018
    },
    {
        "loc_id": "1-112789029",
        "typ": "Social Care Org",
        "name": "Maison Moti Care Home",
        "rating": "Good",
        "numberOfBeds": 15,
        "postcode": "N14 4PH",
        "lat": -0.139015,
        "lng": 51.637248
    },
    {
        "loc_id": "1-112721881",
        "typ": "Social Care Org",
        "name": "Rosehill",
        "rating": "Good",
        "numberOfBeds": 6,
        "postcode": "SR2 7JX",
        "lat": -1.392688,
        "lng": 54.898291
    },
    {
        "loc_id": "1-1125959537",
        "typ": "Social Care Org",
        "name": "Choice East Midlands (Supported Living)",
        "rating": "Good",
        "numberOfBeds": 0,
        "postcode": "LE16 7DS",
        "lat": -0.918353,
        "lng": 52.478158
    },
    {
        "loc_id": "1-112620463",
        "typ": "Social Care Org",
        "name": "Agape House",
        "rating": "No published rating",
        "numberOfBeds": 20,
        "postcode": "ME4 6DG",
        "lat": 0.522515,
        "lng": 51.377218
    },
    {
        "loc_id": "1-112790575",
        "typ": "Social Care Org",
        "name": "Abbey Care",
        "rating": "Good",
        "numberOfBeds": 0,
        "postcode": "L24 9HZ",
        "lat": -2.858447,
        "lng": 53.350334
    },
    {
        "loc_id": "1-112767279",
        "typ": "Social Care Org",
        "name": "The Elms",
        "rating": "Inadequate",
        "numberOfBeds": 26,
        "postcode": "SE22 0JR",
        "lat": -0.070288,
        "lng": 51.452745
    },
    {
        "loc_id": "1-112747080",
        "typ": "Social Care Org",
        "name": "Independence Homes Limited - 37 Foxley Lane",
        "rating": "Good",
        "numberOfBeds": 8,
        "postcode": "CR8 3EH",
        "lat": -0.125545,
        "lng": 51.341286
    },
    {
        "loc_id": "1-112717753",
        "typ": "Social Care Org",
        "name": "Pilton House Trust",
        "rating": "No published rating",
        "numberOfBeds": 27,
        "postcode": "EX31 1PQ",
        "lat": -4.061823,
        "lng": 51.086923
    },
    {
        "loc_id": "1-112552719",
        "typ": "Social Care Org",
        "name": "Springfield Care Home",
        "rating": "Requires improvement",
        "numberOfBeds": 40,
        "postcode": "NG6 8BL",
        "lat": -1.191821,
        "lng": 53.012384
    },
    {
        "loc_id": "1-112803167",
        "typ": "Social Care Org",
        "name": "Westerley Residential Care Home for the Elderly - Westcliff-on-Sea",
        "rating": "Good",
        "numberOfBeds": 20,
        "postcode": "SS0 7QU",
        "lat": 0.697804,
        "lng": 51.536233
    },
    {
        "loc_id": "1-1125975874",
        "typ": "Primary Dental Care",
        "name": "Mydentist - Wells Road - Bristol",
        "rating": "Inspected but not rated",
        "numberOfBeds": 0,
        "postcode": "BS4 2QB",
        "lat": -2.567149,
        "lng": 51.434726
    },
    {
        "loc_id": "1-112743419",
        "typ": "Social Care Org",
        "name": "Abbeyfield Deben Extra Care Society Limited",
        "rating": "Good",
        "numberOfBeds": 24,
        "postcode": "IP12 1EN",
        "lat": 1.314567,
        "lng": 52.097641
    },
    {
        "loc_id": "1-112718008",
        "typ": "Social Care Org",
        "name": "St Vincents Care Home",
        "rating": "Requires improvement",
        "numberOfBeds": 25,
        "postcode": "PO33 3NB",
        "lat": -1.175594,
        "lng": 50.727754
    },
    {
        "loc_id": "1-1127939767",
        "typ": "Social Care Org",
        "name": "Home Instead Senior Care - Peterborough, Oundle & The Deepings",
        "rating": "Good",
        "numberOfBeds": 0,
        "postcode": "PE7 8GX",
        "lat": -0.257658,
        "lng": 52.544071
    },
    {
        "loc_id": "1-112721895",
        "typ": "Social Care Org",
        "name": "Thorndale",
        "rating": "Good",
        "numberOfBeds": 6,
        "postcode": "SR2 7JZ",
        "lat": -1.3905889999999999,
        "lng": 54.897858
    },
    {
        "loc_id": "1-112553898",
        "typ": "Social Care Org",
        "name": "J B Skillcare Limited",
        "rating": "No published rating",
        "numberOfBeds": 0,
        "postcode": "NE11 9SZ",
        "lat": -1.6762009999999998,
        "lng": 54.96377
    },
    {
        "loc_id": "1-112747096",
        "typ": "Social Care Org",
        "name": "Independence Homes Limited - 7 Hall Road",
        "rating": "Good",
        "numberOfBeds": 7,
        "postcode": "SM6 0RT",
        "lat": -0.149651,
        "lng": 51.350501
    },
    {
        "loc_id": "1-112620747",
        "typ": "Social Care Org",
        "name": "Chelston Park Nursing and Residential Home - Chelston Gardens Dementia Nursing Home",
        "rating": "Outstanding",
        "numberOfBeds": 86,
        "postcode": "TA21 9PH",
        "lat": -3.203572,
        "lng": 50.976401
    },
    {
        "loc_id": "1-112600540",
        "typ": "Social Care Org",
        "name": "Phoenix Care Services",
        "rating": "No published rating",
        "numberOfBeds": 0,
        "postcode": "RH19 1EQ",
        "lat": -0.010354,
        "lng": 51.12662
    },
    {
        "loc_id": "1-112767445",
        "typ": "Social Care Org",
        "name": "Faith House Residential Home",
        "rating": "Good",
        "numberOfBeds": 10,
        "postcode": "BS35 4PL",
        "lat": -2.664866,
        "lng": 51.560023
    },
    {
        "loc_id": "1-112721909",
        "typ": "Social Care Org",
        "name": "Ashdale - Sunderland",
        "rating": "Good",
        "numberOfBeds": 4,
        "postcode": "SR2 7JU",
        "lat": -1.392909,
        "lng": 54.899155
    },
    {
        "loc_id": "1-112718314",
        "typ": "Social Care Org",
        "name": "The Hollies Care Home",
        "rating": "Good",
        "numberOfBeds": 18,
        "postcode": "BA7 7AE",
        "lat": -2.515049,
        "lng": 51.090361
    },
    {
        "loc_id": "1-112803563",
        "typ": "Social Care Org",
        "name": "Millfield House Care Home",
        "rating": "No published rating",
        "numberOfBeds": 39,
        "postcode": "NE16 4QA",
        "lat": -1.674575,
        "lng": 54.9431
    },
    {
        "loc_id": "1-112749390",
        "typ": "Social Care Org",
        "name": "The Grange",
        "rating": "Good",
        "numberOfBeds": 27,
        "postcode": "NE66 3RR",
        "lat": -1.668043,
        "lng": 55.46005
    },
    {
        "loc_id": "1-112744371",
        "typ": "Social Care Org",
        "name": "Short Break Care",
        "rating": "Good",
        "numberOfBeds": 7,
        "postcode": "RG5 3QW",
        "lat": -0.902679,
        "lng": 51.445705
    },
    {
        "loc_id": "1-112794925",
        "typ": "Social Care Org",
        "name": "Maria Helena Care",
        "rating": "No published rating",
        "numberOfBeds": 33,
        "postcode": "PE12 9NQ",
        "lat": 0.11441399999999999,
        "lng": 52.84581
    },
    {
        "loc_id": "1-112803582",
        "typ": "Social Care Org",
        "name": "Chase Park Rehabilitation Centre",
        "rating": "No published rating",
        "numberOfBeds": 30,
        "postcode": "NE16 4QA",
        "lat": -1.674575,
        "lng": 54.9431
    },
    {
        "loc_id": "1-112810542",
        "typ": "Independent Healthcare Org",
        "name": "The Surgery",
        "rating": "No published rating",
        "numberOfBeds": 0,
        "postcode": "SM5 4JL",
        "lat": -0.172003,
        "lng": 51.352156
    },
    {
        "loc_id": "1-112767819",
        "typ": "Social Care Org",
        "name": "Vermont House",
        "rating": "No published rating",
        "numberOfBeds": 12,
        "postcode": "B74 2PR",
        "lat": -1.824112,
        "lng": 52.57098
    },
    {
        "loc_id": "1-112633103",
        "typ": "Social Care Org",
        "name": "Widecombe Nursing Home",
        "rating": "Good",
        "numberOfBeds": 38,
        "postcode": "LU3 2DT",
        "lat": -0.429543,
        "lng": 51.916895
    }
]

tags_metadata = [
    {
        "name": "locations",
        "description": "Location the cqc reference to an establishment used in the provision of care.",
    },
    {
        "name": "providers",
        "description": "providors the cqc reference to an organisation used to provide care.",
    },
    {
        "name": "items",
        "description": "Manage items. So _fancy_ they have their own docs.",
        "externalDocs": {
            "description": "Items external docs",
            "url": "https://fastapi.tiangolo.com/",
        },
    },
]

class Item(BaseModel):
    loc_id: str
    typ: str
    name: str
    rating: str
    numberOfBeds: int
    postcode: str
    lat: float
    lng: float

    class Config:
        orm_mode = True


class Message(BaseModel):
    message: str

# setup logger
logger = logging.getLogger('CHH-CORE-API')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# add formatter to ch
ch.setFormatter(formatter)
# add ch to logger
logger.addHandler(ch)


app = FastAPI(
    title="CareHomeHub API interface Project",
    description="This is the primary connection/ Interface to the data layer, with auto docs for the API knowledge share",
    version="0.0.1",)


@app.get("/")
async def root():
    logger.info("logging from the root logger")
    return {"message": "Welcome to CareHomeHubAPI."}


@app.get("/locations", response_model= List[Item], responses={404: {"model": Message}}, tags=["locations"])
async def read_loc():
    logger.info("logging from the /location")
    return data
    
    
@app.get("/locations/{loc_id}", response_model=Item, responses={404: {"model": Message}}, tags=["locations"])
async def read_item(loc_id: str):
    logger.info("logging from the /location/{loc_id}")
    for loc in data:
        logger.info("reading ID "+loc["loc_id"]+" in the data search logger for "+ loc_id)
        
        if loc_id == loc["loc_id"]:
            return {
            "loc_id": loc["loc_id"],
            "typ": loc["typ"],
            "name": loc["name"],
            "rating": loc["rating"],
            "numberOfBeds": loc["numberOfBeds"],
            "postcode": loc["postcode"],
            "lat": loc["lat"],
            "lng": loc["lng"]
        }
    return JSONResponse(status_code=404, content={"message": "Location not found"})


@app.get("/data", response_model= List[Item], responses={404: {"model": Message}}, tags=["locations"])
async def read_data():
    logger.info("logging from the /data")
    data = gdb.getData()
    return data


@app.get("/providers", response_model= List[Item], responses={404: {"model": Message}}, tags=["providers"])
async def read_prov():
    logger.info("logging from the /provider")
    return data
    
    
@app.get("/providers/{loc_id}", response_model=Item, responses={404: {"model": Message}}, tags=["providers"])
async def read_item(loc_id: str):
    logger.info("logging from the /provider/{loc_id}")
    for loc in data:
        logger.info("reading ID "+loc["loc_id"]+" in the data search logger for "+ loc_id)
        
        if loc_id == loc["loc_id"]:
            return {
            "loc_id": loc["loc_id"],
            "typ": loc["typ"],
            "name": loc["name"],
            "rating": loc["rating"],
            "numberOfBeds": loc["numberOfBeds"],
            "postcode": loc["postcode"],
            "lat": loc["lat"],
            "lng": loc["lng"]
        }
    return JSONResponse(status_code=404, content={"message": "Location not found"})
