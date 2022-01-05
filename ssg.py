import typer
from ssg.site import Site

def main(source, dest):
    source = "content"
    dest = "dist"
    config = {
        "dest": dest,
        "source" : source
    }
    Site(**config)
    build(Site)

typer.run(main)
