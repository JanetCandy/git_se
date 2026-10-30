import json
import os
from models import Task

class JsonTaskRepository:
    def __init__(self, filepath="tasks.json"):
        self.filepath = filepath

    def save(self, tasks):
        """將任務列表儲存至 JSON 檔案中"""
        data = [task.to_dict() for task in tasks]
        with open(self.filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def load(self):
        """從 JSON 檔案載入任務列表"""
        if not os.path.exists(self.filepath):
            return []
        try:
            with open(self.filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return [Task.from_dict(item) for item in data]
        except json.JSONDecodeError:
            return []