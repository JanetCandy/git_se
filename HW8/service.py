from models import Task

class TaskService:
    def __init__(self, repository):
        self.repository = repository
        self.tasks = self.repository.load()

    def add_task(self, task_id, title, category, estimated_hours):
        """新增一筆任務並自動存檔"""
        new_task = Task(task_id, title, category, estimated_hours)
        self.tasks.append(new_task)
        self.repository.save(self.tasks)
        return new_task

    def complete_task(self, task_id):
        """完成指定 ID 的任務並存檔"""
        for task in self.tasks:
            if task.task_id == task_id:
                task.complete()
                self.repository.save(self.tasks)
                return True
        return False

    def get_productivity_report(self):
        """計算生產力分析報表"""
        total_tasks = len(self.tasks)
        completed_tasks = sum(1 for t in self.tasks if t.status == "已完成")
        total_hours = sum(t.estimated_hours for t in self.tasks)
        completed_hours = sum(t.estimated_hours for t in self.tasks if t.status == "已完成")

        return {
            "total_tasks": total_tasks,
            "completed_tasks": completed_tasks,
            "completion_rate": (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0,
            "total_estimated_hours": total_hours,
            "completed_hours": completed_hours
        }