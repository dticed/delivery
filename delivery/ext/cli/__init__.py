import click
from delivery.ext.db import db
from delivery.ext.site import models # noqa

def init_app(app):
    @app.cli.command()
    def create_db():
        """Esse comando inicializa o banco de dados
        """
        db.create_all()
        
    @app.cli.command()
    def drop_db():
        """Esse comando exclui o banco de dados
        """
        db.drop_all()
        
    @app.cli.command()
    @click.option("--email", "-e")
    @click.option("--passwd", "-p")
    @click.option("--admin", "-a", is_flag=True)
    def add_user(email, passwd, admin):
        """Adiciona novo usuário
        """
        user = models.User(
            email=email,
            passwd=passwd,
            admin=admin
        )
        db.session.add(user)
        db.session.commit()
        
        click.echo(f"Usuário {email} criado com sucesso!")
        
    @app.cli.command()
    def listar_pedidos():
        click.echo("lista de pedidos")

    @app.cli.command()
    def listar_usuarios():
        click.echo("lista de usuarios")
        