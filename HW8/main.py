from storage import JsonTaskRepository
from service import TaskService

# 初始化儲存庫與服務
repo = JsonTaskRepository("tasks.json")
service = TaskService(repo)

# 新增任務
service.add_task("101", "完成軟體工程期末報告", "學業", 4.5)

# 取得生產力報告
report = service.get_productivity_report()
print(report)