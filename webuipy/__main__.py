# Standard library imports
import sys

# imports
import webuipy
from webuipy import viewer


def main():  # type: () -> None
    """show website"""
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    opts = [o for o in sys.argv[1:] if o.startswith("-")]

    # Show help message
    if "-h" in opts or "--help" in opts:
        viewer.show(__doc__)
        return

    # Get URL from config file
    url = webuipy.URL

    # Show website message
    if "-w" in opts or "--website" in opts:
        viewer.show(url)
        return

    if args:
        for arg in args:
            if arg == 'init':
                viewer.show('Setup initialization')
            else:
                viewer.show('Invalid Argument')

    # No ID is given, show list of articles
    else:
        viewer.show('hello, try to use init, -h or -w')


if __name__ == "__main__":
    main()
