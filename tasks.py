from invoke import task


@task
def coverage(ctx):
    msg = "Coverage finished!"
    cmd = [
        "ls",
        "pwd",
        "coverage run  --source='testapp/api/.' testapp/manage.py test api",
        "coverage report --omit='*migrations*'",
        "coverage html"
    ]

    for c in cmd:
        ctx.run(c, pty=True)
    print(msg)
