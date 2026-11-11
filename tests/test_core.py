import tempfile
import unittest
from pathlib import Path

from sage.core import SageStore


class SageStoreTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.store = SageStore(Path(self.temp_dir.name) / "test.db")

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_create_project_and_task(self):
        project_id = self.store.add_project("Launch website", "First milestone")
        task_id = self.store.add_task(project_id, "Write homepage copy", priority=1)

        projects = self.store.list_projects()
        tasks = self.store.list_tasks()

        self.assertEqual(projects[0]["name"], "Launch website")
        self.assertEqual(tasks[0]["id"], task_id)
        self.assertEqual(tasks[0]["title"], "Write homepage copy")
        self.assertEqual(tasks[0]["priority"], 1)

    def test_task_status_and_dashboard(self):
        project_id = self.store.add_project("SAGE")
        task_id = self.store.add_task(project_id, "Build first feature")
        self.store.set_task_status(task_id, "in_progress")

        self.assertEqual(self.store.dashboard()["in_progress_tasks"], 1)
        self.store.set_task_status(task_id, "done")
        self.assertEqual(self.store.dashboard()["completed_tasks"], 1)

    def test_reject_empty_project_name(self):
        with self.assertRaises(ValueError):
            self.store.add_project(" ")

    def test_reject_invalid_priority(self):
        project_id = self.store.add_project("SAGE")
        with self.assertRaises(ValueError):
            self.store.add_task(project_id, "Bad priority", priority=9)

    def test_reject_unknown_project(self):
        with self.assertRaises(ValueError):
            self.store.add_task(999, "No project")

    def test_project_can_be_paused(self):
        project_id = self.store.add_project("SAGE")
        self.store.set_project_status(project_id, "paused")
        self.assertEqual(self.store.list_projects()[0]["status"], "paused")


if __name__ == "__main__":
    unittest.main()
