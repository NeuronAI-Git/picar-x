def main():
    music.music_set_volume(20)
    tts.lang("en-US")
    tts.say("3")
    tts.say("2")
    tts.say("1")
    tts.say("DANCE!")

    # Save the initial direction (assuming 0 degrees is the default)
    initial_angle = px.dir_current_angle

    # Start playing music
    music.music_play('../musics/macarena.mp3')
    for i in range(5):
        # Dancing movements
        px.set_dir_servo_angle(30)
        px.set_cam_pan_angle(30)
        px.set_cam_tilt_angle(30)
        time.sleep(0.7)
        px.set_dir_servo_angle(-30)
        px.set_cam_pan_angle(-30)
        px.set_cam_tilt_angle(-30)
        time.sleep(0.7)
        px.set_dir_servo_angle(0)
        px.set_cam_pan_angle(0)
        px.set_cam_tilt_angle(0)
        time.sleep(0.7)
        px.set_dir_servo_angle(-15)
        px.backward(15)
        time.sleep(0.7)
        px.backward(0)
        px.set_dir_servo_angle(15)
        px.forward(15)
        time.sleep(0.7)
        px.forward(0)
        px.set_dir_servo_angle(-30)
        px.set_cam_pan_angle(30)
        px.set_cam_tilt_angle(-30)
        time.sleep(0.7)
        px.set_dir_servo_angle(30)
        px.set_cam_pan_angle(-30)
        px.set_cam_tilt_angle(30)
        time.sleep(0.7)
        px.set_dir_servo_angle(0)
        px.set_cam_pan_angle(0)
        px.set_cam_tilt_angle(0)
        time.sleep(0.7)

    # Stop music
    music.music_stop()
    tts.say("Woohoo!")

    # Return to the initial position/orientation
    final_angle = px.dir_current_angle  # Current direction after dance
    rotation_angle = (initial_angle - final_angle) % 360  # Compute difference
    if rotation_angle > 180:  # Optimize for shortest rotation path
        rotation_angle -= 360

    # Rotate the car to face the initial direction
    if rotation_angle > 0:
        px.set_dir_servo_angle(30)  # Turn right
    elif rotation_angle < 0:
        px.set_dir_servo_angle(-30)  # Turn left

    # Calculate the duration of rotation based on your car's speed and angle
    rotation_duration = abs(rotation_angle / 45)  # Assuming 45° per second
    px.forward(10)  # Rotate in place
    time.sleep(rotation_duration)
    px.stop()

    # Reset servo angles to zero
    px.set_dir_servo_angle(0)
    px.set_cam_pan_angle(0)
    px.set_cam_tilt_angle(0)


if __name__ == "__main__": main()
