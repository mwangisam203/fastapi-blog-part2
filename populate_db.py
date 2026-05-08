import asyncio
from datetime import UTC, datetime, timedelta
from pathlib import Path

import httpx
from sqlalchemy import delete, select, update

import models
from database import AsyncSessionLocal, engine
from image_utils import PROFILE_PICS_DIR
from main import app

POPULATE_IMAGES_DIR = Path("populate_images")

USERS = [
    {
        "username": "CoreyMSchafer",
        "email": "CoreyMSchafer@gmail.com",
        "password": "TestPassword1!",
        "image": "corey.png",
    },
    {
        "username": "DefaultDude",
        "email": "TestEmail2@test.com",
        "password": "TestPassword2!",
        # No image - uses default
    },
    {
        "username": "WillowTheCat",
        "email": "TestEmail3@test.com",
        "password": "TestPassword3!",
        "image": "willow.png",
    },
    {
        "username": "FarmDogs",
        "email": "TestEmail4@test.com",
        "password": "TestPassword4!",
        "image": "farmdogs.png",
    },
    {
        "username": "PoppyTheCoder",
        "email": "TestEmail5@test.com",
        "password": "TestPassword5!",
        "image": "poppy.png",
    },
    {
        "username": "GoodBoyBronx",
        "email": "TestEmail6@test.com",
        "password": "TestPassword6!",
        "image": "bronx.png",
    },
]