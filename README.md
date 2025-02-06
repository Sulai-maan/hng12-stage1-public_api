# Number Classification API
An API that takes a number and returns interesting mathematical properties about it, along with a fun fact.

## Overview

This is the stage 1 task of the HNG12 internship cohort - backend track. 

Technology stack: Python's FastAPI framework, GitHub

## Features

- Restful endpoint
- JSON responses

## Installation

### Prerequiistes

- Python
- Pip
- FastAPI
- uvicorn

### Setup
#### Clone the repo:
```bash
git clone "https://github.com/Sulai-maan/stage_1.git"
cd stage_1
```
#### Install requirements

```bash

pip install -r requirements.txt

```

## Usage
### Running the API
```bash
uvicorn main:app --reload
```

The API should now be running on http://localhost:8000

## API Reference
- GET /api/calssify-number/number
-- Returns a fun fact for number
