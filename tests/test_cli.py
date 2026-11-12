from sage.cli import main


def test_cli_project_task_and_dashboard_flow(tmp_path, capsys):
    database = str(tmp_path / "sage.db")
    assert main(["--db", database, "add-project", "Portfolio", "--description", "Build real projects"]) == 0
    assert "Created project #1: Portfolio" in capsys.readouterr().out

    assert main(["--db", database, "add-task", "1", "Ship first feature", "--priority", "1"]) == 0
    assert "Created task #1: Ship first feature" in capsys.readouterr().out

    assert main(["--db", database, "tasks"]) == 0
    task_output = capsys.readouterr().out
    assert "Ship first feature" in task_output
    assert "Portfolio" in task_output

    assert main(["--db", database, "dashboard"]) == 0
    dashboard_output = capsys.readouterr().out
    assert "Active Projects: 1" in dashboard_output
    assert "Open Tasks: 1" in dashboard_output


def test_cli_can_update_task_status(tmp_path, capsys):
    database = str(tmp_path / "sage.db")
    main(["--db", database, "add-project", "SAGE"])
    capsys.readouterr()
    main(["--db", database, "add-task", "1", "Run tests"])
    capsys.readouterr()

    assert main(["--db", database, "set-task-status", "1", "done"]) == 0
    assert "Updated task #1 to done" in capsys.readouterr().out

    main(["--db", database, "dashboard"])
    dashboard_output = capsys.readouterr().out
    assert "Open Tasks: 0" in dashboard_output
    assert "Completed Tasks: 1" in dashboard_output
