import click

from bitcoinpython.keygen import generate_matching_address


@click.group(invoke_without_command=True)
def bitcoinpython():
    pass


@bitcoinpython.command()
@click.argument('prefix')
@click.option('--cores', '-c', default='all')
def gen(prefix, cores):
    click.echo(generate_matching_address(prefix, cores))
