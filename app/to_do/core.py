from app.to_do import data_access
from uuid import uuid4
from datetime import datetime


def get_to_do_list(user_id):
    return data_access.get_to_do_list(user_id)


def create_todo_task(user_id, task_subject,
                     task_description,
                     task_due_date,
                     task_status,
                     task_labels, ):
    task_id = str(uuid4())
    created_date = datetime.utcnow()
    task_obj = {
        "user_id": user_id,
        "task_id": task_id,
        "task_subject": task_subject,
        "task_description": task_description,
        "task_due_date": task_due_date,
        "task_status": task_status,
        "task_created_date": created_date,
        "task_updated_date": created_date,
        "task_labels": task_labels
    }
    return data_access.create_todo_task(task_obj)


def update_todo_task(user_id, task_id, task_subject,
                     task_description,
                     task_due_date,
                     task_status,
                     task_labels):
    updated_date = datetime.utcnow()
    task_updated_obj = {
        "task_subject": task_subject,
        "task_description": task_description,
        "task_due_date": task_due_date,
        "task_status": task_status,
        "task_updated_date": updated_date,
        "task_labels": task_labels
    }
    return data_access.update_todo_task(user_id, task_id, task_updated_obj)


def delete_todo_list(user_id, task_id):
    return data_access.delete_todo_list(user_id, task_id)
