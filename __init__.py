# todo - objective is to build a framework that handle's the following tasks
# todo - given a set of sql files, determine dependencies
# todo - schedule a process: sql, python, sh, etc

from scripts.report import Report


if __name__ == "__main__":
    rep = Report("1234")
    rep.type = "sql"
    rep.name = "test.sql"
    rep.handle()

    rep.type = "py"
    rep.name = "test.py"
    rep.handle()

    rep.type = "sh"
    rep.name = "test.sh"
    rep.handle()
