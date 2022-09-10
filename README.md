# Random Bible Passage Generator
A simple random Bible passage generator

## Backend
- The backend is a Python [Flask](https://flask.palletsprojects.com/en/2.2.x/) app

### Environment Setup
Setting up the environment is as easy as:
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Starting the Flask Development Server
You can start the backend development server (localhost:5000) with:  
```
python3 bible.py
```

Alternatively, you can run: 
```
export FLASK APP=bible.py
flask run
```

### Endpoints
The app has three endpoints:
1. `/whole-bible`
2. `/old-testament`
3. `/new-testament`
