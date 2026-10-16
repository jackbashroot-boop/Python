#This will update CachyOS every 30 minutes on a loop.
#Make sure to use sudo chmod +x to apply executable permissions to the .py file
#sudo python3 "/file dir" to run the command and test its working correctly. Should get a message that it updated successfully.

# !/usr/bin/env python3
import subprocess
import sys
import time
import os

LOCK_FILE = "/var/lib/pacman/db.lck"


def is_pacman_locked():
    return os.path.exists(LOCK_FILE)


def run_update():
    if is_pacman_locked():
        print("Warning: Pacman database is locked. Skipping this cycle.", file=sys.stderr)
        return

    try:
        subprocess.run(
            ["/usr/bin/pacman", "-Syu", "--noconfirm"],
            check=True,
            timeout=600,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
            text=True
        )
        print("System updated successfully.")
    except subprocess.TimeoutExpired:
        print("Error: Update timed out after 10 minutes.", file=sys.stderr)
    except subprocess.CalledProcessError as e:
        error_msg = e.stderr.strip() if e.stderr else "Unknown error"
        print(f"Update failed: {error_msg}", file=sys.stderr)
    except Exception as e:
        print(f"Unexpected error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    # Small 5 second delay for manual testing convenience
    time.sleep(5)

    while True:
        run_update()
        time.sleep(1800)





