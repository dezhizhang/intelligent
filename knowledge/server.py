import sys

import uvicorn
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run the server')
    parser.add_argument(
        '--host',
        type=str,
        default="localhost",
        help='Host to bind to (default: localhost)'
    )
    parser.add_argument(
        '--port',
        type=int,
        default=8080,
        help='Port to bind to (default: 8080)'
    )

    parser.add_argument(
        "--reload",
        action="store_true",
        help="Reload the server"
    )

    parser.add_argument(
        "--log-level",
        type=str,
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        help="Log level"
    )
    args = parser.parse_args()
    reload = False
    if args.reload:
        reload = True

    try:
        uvicorn.run("src.main.app:app", host=args.host, port=args.port, reload=reload)
    except Exception as e:
        print(e)
        sys.exit(1)
