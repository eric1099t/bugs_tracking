import json
import os
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from lesson2 import BugTracker, load_data_from_json, export_report_data

app = FastAPI(title="Bug Tracker API")

current_dir = os.path.dirname(os.path.abspath(__file__))
data_file = os.path.join(current_dir, "jira_data.json")

raw_data = load_data_from_json(data_file)
tracker = BugTracker(raw_data)

class CreateBugRequest(BaseModel):
    ticket_id: str
    severity: str = "UNKNOWN"
    status: str = "OPEN"

class UpdateBugStatusRequest(BaseModel):
    ticket_id: str
    new_status: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the Bug Tracker API!"}

@app.get("/all_bugs")
def get_all_bugs():
    return {"bugs": tracker.get_all_bugs()}

@app.get("/critical-bugs/count")
def count_critical_bugs():
    return {"critical_bug_count": tracker.count_critical_bugs()}    
    
@app.get("/actionable-bugs")      
def get_actionable_bugs():
    actionable_bugs = tracker.get_actionable_bugs()
    export_report_data(actionable_bugs, os.path.join(current_dir, "actionable_report.json"))
    return {"actionable_bugs": actionable_bugs}

@app.post("/add-bug")
def add_bug(payload: CreateBugRequest):
    try:
        new_bug_data = tracker.add_bug(ticket_id=payload.ticket_id, severity=payload.severity, status=payload.status)
        tracker.save_to_json(data_file)
        return {"message": "Bug added successfully.", "bug": new_bug_data}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@app.put("/api/bugs/{ticket_id}")
def update_bug(ticket_id: str, payload: UpdateBugStatusRequest):
    try:
        updated_bug_data = tracker.update_bug(ticket_id=ticket_id, status=payload.new_status)
        tracker.save_to_json(data_file)
        return {"message": "Bug status updated successfully.", "bug": updated_bug_data}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
        
@app.delete("/api/bugs/{ticket_id}")
def delete_bug(ticket_id: str):
    try:
        delete_endpoint = tracker.delete_bug(ticket_id=ticket_id)
        tracker.save_to_json(data_file)
        return {"message": "Bug deleted successfully.", "details": delete_endpoint}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))