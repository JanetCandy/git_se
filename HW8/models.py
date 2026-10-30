class Task:
    def __init__(self, task_id, title, category, estimated_hours, status="未完成"):
        self.task_id = task_id
        self.title = title
        self.category = category
        self.estimated_hours = float(estimated_hours)
        self.status = status

    def complete(self):
        """將任務狀態設為已完成"""
        self.status = "已完成"

    def to_dict(self):
        """將物件轉換為字典格式，以利 JSON 序列化"""
        return {
            "task_id": self.task_id,
            "title": self.title,
            "category": self.category,
            "estimated_hours": self.estimated_hours,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, data):
        """從字典反序列化建立 Task 物件"""
        return cls(
            task_id=data["task_id"],
            title=data["title"],
            category=data["category"],
            estimated_hours=data["estimated_hours"],
            status=data["status"]
        )