import unittest
import os
from models import Task
from storage import JsonTaskRepository
from service import TaskService

class TestTaskService(unittest.TestCase):
    def setUp(self):
        """每個測試執行前初始化暫存檔案與服務"""
        self.test_file = "test_tasks.json"
        self.repo = JsonTaskRepository(self.test_file)
        self.service = TaskService(self.repo)

    def tearDown(self):
        """測試結束後清理產生的暫存檔案"""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_task(self):
        task = self.service.add_task("1", "寫軟體工程作業", "學業", 3.5)
        self.assertEqual(len(self.service.tasks), 1)
        self.assertEqual(task.title, "寫軟體工程作業")
        self.assertEqual(task.status, "未完成")

    def test_complete_task(self):
        self.service.add_task("1", "專案重構", "工作", 5.0)
        success = self.service.complete_task("1")
        self.assertTrue(success)
        self.assertEqual(self.service.tasks[0].status, "已完成")

    def test_productivity_report(self):
        self.service.add_task("1", "任務 A", "測試", 2.0)
        self.service.add_task("2", "任務 B", "測試", 3.0)
        self.service.complete_task("1")
        
        report = self.service.get_productivity_report()
        self.assertEqual(report["total_tasks"], 2)
        self.assertEqual(report["completed_tasks"], 1)
        self.assertEqual(report["completion_rate"], 50.0)

if __name__ == "__main__":
    unittest.main()
