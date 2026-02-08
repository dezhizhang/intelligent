import signal
import sys

import uvicorn
import argparse


def handle_shutdown(sig, frame):
    sys.exit(0)

#  监听退出信号
signal.signal(signal.SIGINT, handle_shutdown)
signal.signal(signal.SIGTERM, handle_shutdown)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run the server')
    parser.add_argument(
        '--host',
        type=str,
        default="localhost",
        help='host to bind the server to (default: localhost)'
    )
    parser.add_argument(
        '--port',
        type=int,
        default=8080,
        help='port to bind to (default: 8000)'
    )

    parser.add_argument(
        "--reload",
        action="store_true",
        help="reload the server"
    )

    parser.add_argument(
        "--log-level",
        type=str,
        default="INFO",
        choices=["critical", "error", "warning", "info", "debug"],
        help="log level (default: info)"
    )
    args = parser.parse_args()
    reload = False
    if args.reload:
        reload = True

    try:
        uvicorn.run(
            "src.main:app",
            host=args.host,
            port=args.port,
            reload=reload
        )
    except Exception as e:
        print(e)
        sys.exit(1)
