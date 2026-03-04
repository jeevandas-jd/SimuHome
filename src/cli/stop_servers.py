import os
import subprocess
import time


def get_pids(port: int) -> list[str]:
    cmd = ["lsof", "-ti", f"tcp:{port}"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout.strip().split()


def stop_server_on_port(port: int):
    try:
        pids = get_pids(port)
        if not pids:
            return

        print(f"[stop_servers] Stopping port {port} (PIDs: {', '.join(pids)})")
        subprocess.run(["kill"] + pids, check=False)

        time.sleep(1)

        remaining_pids = get_pids(port)
        if remaining_pids:
            print(
                f"[stop_servers] Force killing port {port} (PIDs: {', '.join(remaining_pids)})"
            )
            subprocess.run(["kill", "-9"] + remaining_pids, check=False)

    except Exception as e:
        print(f"[stop_servers] Error on port {port}: {e}")


def main():
    ports: set[int] = set()

    if env_port := os.environ.get("PORT"):
        ports.add(int(env_port))

    if not ports:
        return

    print(f"[stop_servers] Target ports: {sorted(ports)}")
    for port in sorted(ports):
        stop_server_on_port(port)


if __name__ == "__main__":
    main()
