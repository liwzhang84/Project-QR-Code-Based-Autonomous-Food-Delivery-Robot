import time
import subprocess

CMD_TOPIC = "/cmd_vel"

SPEED = 0.5
RATE = 10

# 테이블까지 가는 시간
ID_TO_FORWARD_TIME = {
    1: 9.0,
    2: 9.0,
    3: 30.0,
    4: 30.0,
}

# 다시 돌아오는 시간
# 로봇이 뒤로 너무 많이 가면 이 값을 줄이세요.
ID_TO_RETURN_TIME = {
    1: 3.0,
    2: 3.0,
    3: 11.0,
    4: 11.0,
}


def send_cmd(vx):
    cmd = (
        f"gz topic -t {CMD_TOPIC} "
        f"-m gz.msgs.Twist "
        f"-p \"linear: {{x: {vx}}}, angular: {{z: 0.0}}\""
    )
    subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def drive_for(seconds, vx):
    start = time.time()
    while time.time() - start < seconds:
        send_cmd(vx)
        time.sleep(1.0 / RATE)


def stop_for(seconds=1.0):
    start = time.time()
    while time.time() - start < seconds:
        send_cmd(0.0)
        time.sleep(1.0 / RATE)


def main():
    target_id = int(input("Enter target QR ID: "))

    if target_id not in ID_TO_FORWARD_TIME:
        print("Unknown ID. Please use one of:", list(ID_TO_FORWARD_TIME.keys()))
        return

    forward_time = ID_TO_FORWARD_TIME[target_id]
    return_time = ID_TO_RETURN_TIME[target_id]

    print(f"Going to QR ID {target_id}...")
    drive_for(forward_time, SPEED)

    print("Arrived. Stopping.")
    stop_for(1.0)

    print("Waiting for 5 seconds.")
    time.sleep(5)

    print("Returning to start...")
    drive_for(return_time, -SPEED)

    print("Final stop.")
    stop_for(1.0)

    print("Done. Robot stopped.")


if __name__ == "__main__":
    main()
