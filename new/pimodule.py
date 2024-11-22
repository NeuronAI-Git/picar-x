import time
import requests

from vilib import Vilib
from picarx import Picarx
from robot_hat import Music, TTS

_music = Music()
_tts = TTS()
_picar = Picarx()
_vision = Vilib()
_time = time

class CAR:
    def stop(time=0):
        _time.sleep(time)
        _picar.stop()
        _picar.stop()

    def forward(speed, time=0):
        _time.sleep(time)
        _picar.forward(abs(speed))

    def backward(speed, time=0):
        _time.sleep(time)
        _picar.backward(abs(speed))

    def set_motor_1(speed, time=0):
        _time.sleep(time)
        _picar.motor_direction_calibrate(1, 1 if speed >= 0 else -1)
        _picar.set_motor_speed(1, speed)

    def set_motor_2(speed, time=0):
        _time.sleep(time)
        _picar.motor_direction_calibrate(2, 1 if speed >= 0 else -1)
        _picar.set_motor_speed(2, speed)

    def set_tilt(amount, time=0):
        _time.sleep(time)
        _picar.set_cam_tilt_angle(amount)

    def set_pan(amount, time=0):
        _time.sleep(time)
        _picar.set_cam_pan_angle(amount)

    def set_dir(amount, time=0):
        _time.sleep(time)
        _picar.set_dir_servo_angle(amount)

    def set_speed(amount, time=0):
        _time.sleep(time)
        _picar.set_motor_speed(amount)

    def set_power(amount, time=0):
        _time.sleep(time)
        _picar.set_power(amount)

    def set_cliff(amount, time=0):
        _time.sleep(time)
        _picar.set_cliff_reference(amount)

    def set_line(amount, time=0):
        _time.sleep(time)
        _picar.set_line_reference(amount)

    def set_grayscale(amount, time=0):
        _time.sleep(time)
        _picar.set_grayscale_reference(amount)

    def get_distamce(time=0):
        _time.sleep(time)
        return _picar.get_distance()

    def get_cliff(time=0):
        _time.sleep(time)
        return _picar.get_cliff_status()

    def get_grayscale(time=0):
        _time.sleep(time)
        return _picar.get_grayscale_data()

    def get_line(time=0):
        _time.sleep(time)
        return _picar.get_line_status()

class MUSIC:
    _music_playing = False

    def music(file, pause=False, time=0):
        _time.sleep(time)
        if MUSIC._music_playing is False:
            if pause:
                _music.music_resume()
            else:
                _music.music_play(file)
            MUSIC._music_playing = True
        else:
            if not pause:
                _music.music_stop()
            else:
                _music.music_pause()
            MUSIC._music_playing = False

    def beat(beat, time=0):
        _time.sleep(time)
        _music.beat(beat)

    def tempo(tempo=None, note_value=None, time=0):
        _time.sleep(time)
        _music.tempo(tempo, note_value)

    def note(note, natural=False, time=0):
        _time.sleep(time)
        _music.note(note, natural)

    

    def disable(time=0):
        _time.sleep(time)
        _music.disable_speaker()

    def enable(time=0):
        _time.sleep(time)
        _music.enable_speaker()

    def key_signature(key, time=0):
        _time.sleep(time)
        _music.key_signature(key)

    def time_signature(top=None, bottom=None, time=0):
        _time.sleep(time)
        _music.time_signature(top, bottom)

    def set_volume(amount, time=0):
        _time.sleep(time)
        _music.music_set_volume(amount)

    def play_tone(frequency, duration, time=0):
        _time.sleep(time)
        _music.play_tone_for(frequency, duration)
    
    def get_tone(frequency, duration, time=0):
        _time.sleep(time)
        return _music.get_tone_data(frequency, duration)
    
    def sound_length(file, time=0):
        _time.sleep(time)
        return _music.sound_length(file)
    
    def sound_play(file, volume=None, time=0):
        _time.sleep(time)
        _music.sound_play(file, volume)

    def sound_play(file, volume=None, time=0):
        _time.sleep(time)
        _music.sound_play_threading(file, volume)

class SPEAK:
    def speak(prompt, time=0):
        _time.sleep(time)
        _tts.say(prompt)

    def espeak(amp=None, speed=None, gap=None, pitch=None, time=0):
        _time.sleep(time)
        _tts.espeak_params(amp, speed, gap, pitch)

    def pico2wave(prompt, time=0):
        _time.sleep(time)
        _tts.pico2wave(prompt)

    def language(lang, time=0):
        _time.sleep(time)
        _tts.lang(lang)

    def get_languages(time=0):
        _time.sleep(time)
        return _tts.supported_lang()

class VISION:
    def camera(time=0):
        _time.sleep(time)
        _vision.camera()

    def camera_close(time=0):
        _time.sleep(time)
        _vision.camera_close()

    def camera_start(vflip=False, hflip=False, time=0):
        _time.sleep(time)
        _vision.camera_start()

    def close_color_detection(time=0):
        _time.sleep(time)
        _vision.close_color_detection()

    def color_detect(color="red", time=0):
        _time.sleep(time)
        _vision.color_detect(color)

    def color_detect_func(img, time=0):
        _time.sleep(time)
        _vision.color_detect_func(img)

    def display(local=True, web=True, time=0):
        _time.sleep(time)
        _vision.display(local, web)

    def display_qrcode(local=True, web=True, time=0):
        _time.sleep(time)
        _vision.display_qrcode(local, web)

    def face_detect_func(img, time=0):
        _time.sleep(time)
        _vision.face_detect_func(img)

    def face_detect_switch(flag=False, time=0):
        _time.sleep(time)
        _vision.face_detect_switch(flag)

    def hands_detect_fuc(img, time=0):
        _time.sleep(time)
        _vision.hands_detect_fuc(img)

    def hands_detect_switch(flag=False, time=0):
        _time.sleep(time)
        _vision.hands_detect_switch(flag)

    def image_classify_fuc(img, time=0):
        _time.sleep(time)
        _vision.image_classify_fuc(img)

    def image_classify_switch(flag=False, time=0):
        _time.sleep(time)
        _vision.image_classify_switch(flag)

    def image_classify_set_labels(path, time=0):
        _time.sleep(time)
        _vision.image_classify_switch(path)

    def image_classify_set_model(path, time=0):
        _time.sleep(time)
        _vision.image_classify_set_model(path)

    def object_detect_fuc(img, time=0):
        _time.sleep(time)
        _vision.object_detect_fuc(img)

    def object_detect_switch(flag=False, time=0):
        _time.sleep(time)
        _vision.object_detect_switch(flag)

    def object_detect_set_model(path, time=0):
        _time.sleep(time)
        _vision.object_detect_set_model(path)

    def object_detect_set_labels(path, time=0):
        _time.sleep(time)
        _vision.object_detect_set_labels(path)

    def pose_detect_fuc(img, time=0):
        _time.sleep(time)
        _vision.pose_detect_fuc(img)

    def pose_detect_switch(flag=False, time=0):
        _time.sleep(time)
        _vision.pose_detect_switch(flag)

    def qrcode_detect_func(img, time=0):
        _time.sleep(time)
        _vision.qrcode_detect_func(img)

    def qrcode_detect_switch(flag=False, time=0):
        _time.sleep(time)
        _vision.qrcode_detect_switch(flag)

    def traffic_detect_fuc(img, time=0):
        _time.sleep(time)
        _vision.traffic_detect_fuc(img)

    def traffic_detect_switch(flag=False, time=0):
        _time.sleep(time)
        _vision.traffic_detect_switch(flag)
    
    def rec_video_pause(time=0):
        _time.sleep(time)
        _vision.rec_video_pause()

    def rec_video_run(time=0):
        _time.sleep(time)
        _vision.rec_video_run()

    def rec_video_start(time=0):
        _time.sleep(time)
        _vision.rec_video_start()

    def rec_video_stop(time=0):
        _time.sleep(time)
        _vision.rec_video_stop()

    def rec_video_work(time=0):
        _time.sleep(time)
        _vision.rec_video_work()

    def show_fps(color=None, fps_size=None, fps_origin=None, time=0):
        _time.sleep(time)
        _vision.show_fps(color, fps_size, fps_origin)

    def hide_fps(time=0):
        _time.sleep(time)
        _vision.hide_fps()

    def rec_video_work(time=0):
        _time.sleep(time)
        _vision.rec_video_work()

    def make_qrcode(data, path, version=1, box_size=10, border=4, fill_color=(132, 112, 255), back_color=(255, 255, 255), time=0):
        _time.sleep(time)
        _vision.make_qrcode(data, path, version, box_size, border, fill_color, back_color)

    def take_photo(photo_name, path=None, time=0):
        _time.sleep(time)
        if path: _vision.take_photo(photo_name, path)
        else: _vision.take_photo(photo_name)

class LLM:
    model="openai"
    system="""
    You are a 4 wheeled rover like robot called Pie (Picar-X robot). Use only short sentences, max 2 sentences. Don't offer to help the user, just give help if they ask, you are for conversation, not for assistance unless asked. Instead of typing numbers or symbols (besides punctuation like , . ? ! ' etc), type them out like this:
    1   --->   One
    100 --->   One Hundred
    /   --->   Slash
    -   --->   Minus

    and so on.
    """
    messages=[]
    headers={"Content-Type": "application/json"}
    timeout=45

    _create = lambda role, content: {"role": str(role), "content": str(content)}

    messages.append(_create("system", system))

    def generate(prompt, time=0):
        _time.sleep(time)
        LLM.messages.append(LLM._create("user", prompt))

        if len(LLM.messages) > 25:
            while True:
                LLM.messages.pop(1)
                if len(LLM.messages) == 25:
                    break
        
        params = {
            "messages": LLM.messages,
            "model": LLM.model
        }

        request = requests.post(
            "https://text.pollinations.ai/", json=params, headers=LLM.headers, timeout=LLM.timeout
        )

        try:
            content = request.content
            LLM.messages.append(LLM._create("assistant", content))
            return LLM._decode(content)
        except:
            LLM.messages.append(LLM._create("assistant", "Sorry, I'm having an issue."))
            return LLM._decode(b"Sorry, I'm having an issue.")
    
    def _decode(content):
        try:
            decoded_response = content.decode('utf-8')
            escaped_response = decoded_response.replace("'", "\\'")
            return escaped_response
        except Exception as e:
            return content
            
    def clear(time=0):
        _time.sleep(time)
        LLM.messages = []
        LLM.messages.append(LLM._create("system", LLM.system))
