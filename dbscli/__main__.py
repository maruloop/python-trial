import sys
import click


@click.group()
def cmd():
    pass

@cmd.command()
def xio():
    click.echo('xio sub command!')

@cmd.command()
def nb():
    click.echo('nb sub coomand!')

@cmd.command()
def sf():
    click.echo('sf sub command!')

def main():
    cmd()
    return 0

if __name__ == "__main__":
    sys.exit(main())
