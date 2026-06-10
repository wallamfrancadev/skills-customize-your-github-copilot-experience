# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a RESTful API using FastAPI framework to understand HTTP methods, request/response handling, and modern web application development. Students will create endpoints for managing data and learn how FastAPI simplifies API development with automatic validation and documentation.

## 📝 Tasks

### 🛠️ Task 1: Set Up FastAPI Application and Create Basic Endpoints

#### Description
Set up a FastAPI application with basic GET and POST endpoints to understand the framework structure and routing.

#### Requirements
Completed program should:

- Initialize a FastAPI application instance
- Create a GET endpoint that returns a greeting message
- Create a POST endpoint that accepts JSON data and returns a confirmation
- Include proper response status codes


### 🛠️ Task 2: Implement CRUD Operations

#### Description
Extend the API with full CRUD (Create, Read, Update, Delete) operations on a list of items (e.g., books, tasks, or products).

#### Requirements
Completed program should:

- Implement GET endpoint to retrieve all items
- Implement GET endpoint to retrieve a single item by ID
- Implement POST endpoint to create a new item with automatic ID generation
- Implement PUT endpoint to update an existing item
- Implement DELETE endpoint to remove an item
- Handle edge cases like item not found (return 404)


### 🛠️ Task 3: Add Data Validation and Error Handling

#### Description
Use Pydantic models for request validation and implement proper error handling to ensure API robustness.

#### Requirements
Completed program should:

- Define Pydantic model(s) for request/response data
- Validate all input data (required fields, data types, constraints)
- Return meaningful error messages with appropriate HTTP status codes
- Handle cases where requests contain invalid data


### 🛠️ Task 4: Explore Interactive Documentation and Testing (Stretch Goal)

#### Description
Discover FastAPI's automatic API documentation and test your endpoints using the built-in Swagger UI and ReDoc interfaces.

#### Requirements
Completed program should:

- Run the application with `uvicorn`
- Access interactive documentation at `/docs` (Swagger UI)
- Test all CRUD endpoints using the Swagger interface
- Document endpoints with docstrings visible in the interactive docs

