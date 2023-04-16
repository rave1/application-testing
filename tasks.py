from invoke import task


@task
def coverage(ctx):
    msg = "Coverage finished!"
    cmd = [
        "coverage run --source='.' ./testapp/manage.py test",
        "coverage report --omit='*migrations*'",
        "coverage html"
    ]

    for c in cmd:
        ctx.run(c, pty=True)
    print(msg)
