"""
Building REST APIs with FastAPI

Starter code for implementing a RESTful API using FastAPI framework.
Complete the tasks to build a functional API with CRUD operations.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Initialize FastAPI application
app = FastAPI(
    title="Student API",
    description="A simple REST API for managing items",
    version="1.0.0"
)

# Define Pydantic model for request/response validation
# TODO: Update this model based on your specific use case
class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    price: Optional[float] = None


# In-memory storage for items (for demonstration purposes)
items_db: List[Item] = []
item_id_counter = 1


# Task 1: Basic endpoints
@app.get("/")
async def read_root():
    """Welcome endpoint - returns a greeting message."""
    # TODO: Implement this endpoint to return a greeting
    pass


@app.post("/hello")
async def create_greeting(message: dict):
    """Echo endpoint - accepts JSON and returns confirmation."""
    # TODO: Implement this endpoint to accept data and return confirmation
    pass


# Task 2: CRUD Operations
@app.get("/items", response_model=List[Item])
async def get_all_items():
    """Retrieve all items from the database."""
    # TODO: Implement to return all items
    pass


@app.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int):
    """Retrieve a specific item by ID."""
    # TODO: Implement to return a single item or 404 if not found
    pass


@app.post("/items", response_model=Item, status_code=201)
async def create_item(item: Item):
    """Create a new item in the database."""
    # TODO: Implement to add item and return it with generated ID
    pass


@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, updated_item: Item):
    """Update an existing item."""
    # TODO: Implement to update item or return 404 if not found
    pass


@app.delete("/items/{item_id}", status_code=204)
async def delete_item(item_id: int):
    """Delete an item from the database."""
    # TODO: Implement to delete item or return 404 if not found
    pass


# Task 3: Error handling is already partially set up with HTTPException
# Your validation will happen automatically through Pydantic models

# To run this application, use:
# uvicorn starter_code:app --reload
