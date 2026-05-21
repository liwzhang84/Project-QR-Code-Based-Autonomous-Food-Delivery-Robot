import time
import subprocess

CMD_TOPIC = "/cmd_vel"

SPEED = 0.25
RATE = 10

# 这里根据每个二维码在通道上的前后距离设置时间
# 你可以之后自己微调这些秒数
ID_TO_FORWARD_TIME = {
    1: 2.5,
    2: 4.0,
    3: 5.5,
    4: 7.0,
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


def main():
    target_id = int(input("Enter target QR ID: "))

    if target_id not in ID_TO_FORWARD_TIME:
        print("Unknown ID. Please use one of:", list(ID_TO_FORWARD_TIME.keys()))
        return

    forward_time = ID_TO_FORWARD_TIME[target_id]

    print(f"Going to QR ID {target_id}...")
    drive_for(forward_time, SPEED)

    print("Arrived. Stop for 5 seconds.")
    send_cmd(0.0)
    time.sleep(5)

    print("Returning to start...")
    drive_for(forward_time, -SPEED)

    send_cmd(0.0)
    print("Done. Robot stopped.")


if __name__ == "__main__":
    main()
