from app import db

to_do_db = db.to_do_list


def get_to_do_list(user_id):
    result = list(to_do_db.find({"user_id": user_id}, {"_id": 0}))
    return result


def create_todo_task(task_obj):
    to_do_db.insert(task_obj)
    return "Task Added Successfully"


def update_todo_task(user_id, task_id, task_update_obj):
    to_do_db.update({"user_id": user_id, "task_id": task_id}, {"$set": task_update_obj})
    return "Task Updated Successfully"


def delete_todo_list(user_id, task_id):
    to_do_db.remove({"user_id": user_id, "task_id": task_id})
    return "Task Deleted Successfully"
