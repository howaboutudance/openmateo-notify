import nox

@nox.session
def lint(session):
    session.install('ruff')
    session.run('ruff', 'check', 'src')

@nox.session
def format(session):
    session.install('ruff')
    session.run('ruff', 'format', 'src')

@nox.session
def test(session):
    session.install('pytest')
    session.run('pytest', 'src/openmateo_notify')