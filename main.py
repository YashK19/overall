class Lesson:
    current_question_index = 0
    questions = [
        {"question": "Which planet is closest to sun?", "answer": "Mercury"},
        {"question": "Which planet is known as the Red Planet?", "answer": "Mars"},
        {"question": "Which planet is the largest?", "answer": "Jupiter"},
        {"question": "Which planet is the smallest?", "answer": "Saturn"},
        {"question": "Which planet is the furthest from the sun?", "answer": "Venus"}
        # TODO: ...other questions
    ]

    def __init__(self):
        self.audio_visual = AudioVisual()
        self.planet_detection = PlanetDetection()

    def start_lesson(self):
        """Method to start the lesson."""
        self.next_question()
        
    def next_question(self):
        """Method to proceed to the next question."""
        self.current_question_index += 1
        if self.current_question_index < len(self.questions):
            self.audio_visual.display_question(self.questions[self.current_question_index]['question'])
            id = self.planet_detection.detect_planet()
            I2C_LCD1602.clear()
            # self.check_response(id)
        else:
            self.finish_lesson()

    def check_response(self, planet: str):
        """Method to check the response.

        Args:
        planet (str): The planet name in the response.
        """
        correct_answer = self.questions[self.current_question_index]['answer']
        if planet == correct_answer:
            self.audio_visual.display_success(planet)
            # self.audio_visual.play_success_sound()
            # wait(1000)
            # self.audio_visual.play_rotation_sound()
            # speed = self.get_orbit_speed(planet)
            # self.planet_motion.rotate_arm(speed)
        else:
            self.audio_visual.display_failure(planet)
            # self.audio_visual.play_fail_sound()

    def finish_lesson(self):
        """Method to finish the lesson."""
        pass
    


class PlanetDetection:
    def __init__(self):
        JoyPiAdvanced.rfid_init()

    def detect_planet(self):
        """Method to detect a planet.

        Returns:
        str: The detected planet name.
        """
        # Code to detect which planet is placed on the sensor
        planet_map = [("259584497701", "Mercury"), ("809057392480", "Venus")]
    
        id = 0
        while (id == 0):
            id = JoyPiAdvanced.rfid_read_id() 

        while (True):
            if (pins.digital_read_pin(DigitalPin.P1) == 0):
                break

        for (planet_data in planet_map):
            planet_id = planet_data[0]
            planet = planet_data[1]
            if (str(id) == planet_id):
                return planet
        
        return "Unknown"

class AudioVisual:
    def __init__(self):
        pass

    def display_success(self, planet: str):
        """Method to display a success message.

        Args:
        planet (str): The planet name in the success message.
        """
        # Code to display success message on LED and play correct sound
        I2C_LCD1602.clear()
        I2C_LCD1602.show_string(planet, 0, 0)
        I2C_LCD1602.show_string("is correct!", 1, 0)

    def display_failure(self, planet: str):
        """Method to display a failure message.

        Args:
        planet (str): The planet name in the failure message.
        """
        # Code to display failure message on LED
        I2C_LCD1602.show_string("Incorrect..." , 0, 0)
        I2C_LCD1602.show_string("Try again." , 1, 0)

    def display_lesson_complete(self, message: str):
        """Method to display a lesson complete message.

        Args:
        message (str): The message to be displayed.
        """

    def play_success_sound(self):
        """Method to play success sound."""
        # Code to play the specified sound
        music.play(music.tone_playable(784, music.beat(BeatFraction.QUARTER)),
                    music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(784, music.beat(BeatFraction.WHOLE)),
                    music.PlaybackMode.UNTIL_DONE)

    def play_fail_sound(self):
        """Method to play fail sound."""
        # Code to play the specified sound
        pass

    def play_rotation_sound(self):
        """Method to play rotation sound."""
        # Star Wars
        music.play(music.tone_playable(392, music.beat(BeatFraction.HALF)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(587, music.beat(BeatFraction.HALF)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(523, music.beat(BeatFraction.QUARTER)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(494, music.beat(BeatFraction.QUARTER)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(440, music.beat(BeatFraction.QUARTER)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(784, music.beat(BeatFraction.HALF)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(587, music.beat(BeatFraction.QUARTER)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(523, music.beat(BeatFraction.QUARTER)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(494, music.beat(BeatFraction.QUARTER)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(440, music.beat(BeatFraction.QUARTER)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(784, music.beat(BeatFraction.HALF)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(587, music.beat(BeatFraction.QUARTER)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(523, music.beat(BeatFraction.QUARTER)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(494, music.beat(BeatFraction.QUARTER)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(523, music.beat(BeatFraction.QUARTER)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(440, music.beat(BeatFraction.HALF)),
            music.PlaybackMode.UNTIL_DONE)
        # Code to play the specified sound
        pass

    def stop_rotation_sound(self):
        """Method to stop rotation sound."""
        # Code to stop the specified sound
        pass

    def play_lesson_complete_sound(self, txt, aChar):
        """Method to play lesson complete sound."""
        # Code to play the specified sound
        pass

    def myrfind(self, txt: str, aChar: str):
        for i in range(len(txt) - 1, -1, -1):
            if txt[i]  == aChar:
                return i
        return -1
    
    def display_question(self, question: str):
        """Method to display the question.

        Args:
        question (str): The question to be displayed.
        """
        # pd = PlanetDetection()
        oldlastindex = 0
        lastindex = 0
        lastcompare = 0
        i = 0
        # display = True
        done = False 
        line = ""
        lines = []
        serial.write_line("Hello.")
        # # # serial.write_line(str(len(question)-1))
        while (lastindex < len(question)-1):
            lastcompare = 16 + lastindex
            # # serial.write_line(str(lastcompare))
            if (len(question) - 1 < lastcompare):
                lastcompare = len(question)-1
                done = True
                # serial.write_line("Done is true.")
            if (question[lastcompare] != " "):
                # x = 1
                # self.myrfind("a", "b")
                lastindex = self.myrfind(question[oldlastindex:lastcompare], " ") + oldlastindex
                # serial.write_line(str(lastindex))
            else:
                lastindex = lastcompare
            
            if (lastcompare >= len(question)-1):
                lastindex = len(question)
            line = question[oldlastindex:lastindex]
            oldlastindex = lastindex
            i += 1
            # serial.write_line(line)
            lines.append(line)
            if (done):
                break
        j = 0
        serial.write_line("Hello again.")
        while(j < len(lines)):
            if (j > 1 and j % 2 == 0):
                basic.pause(3000)
                I2C_LCD1602.clear()
            row = j % 2
            I2C_LCD1602.show_string(lines[j], 0, row)
            j += 1
            # if (j >= len(lines)):
            #     basic.pause(3000)
            #     I2C_LCD1602.clear()
            #     j = 0
    
## ALL MAIN CODE HERE ##
# I2C_LCD1602.lcd_init(39)
# pins.set_pull(DigitalPin.P1, PinPullMode.PULL_UP)
serial.write_line("This is running fr8.")
pd = PlanetDetection()
planet = pd.detect_planet()
serial.write_line(str(planet))
# JoyPiAdvanced.rfid_init()
# id = 0
# while(True):   
#     serial.write_line("HELLO")
#     serial.write_line(str(id))
#     id = JoyPiAdvanced.rfid_read_id()
#     serial.write_line(str(id))


# display.show(Image.NO)

# while True:
#     start_time = utime.ticks_ms()
#     card_id = rfid.wait_card(address, start_time)
#     current_time = utime.ticks_ms()
#     elapsed_time = utime.ticks_diff(current_time, start_time)
#     if elapsed_time >= 500:
#         prev_card_id = None
#         # display.show(Image.YES)
#     if (card_id != prev_card_id):  # Compare with the previous card ID
#         print(card_id)
#         prev_card_id = card_id  # Update the previous card ID
#     sleep(400)
    # display.show(Image.NO)




# lesson = Lesson()
# lesson.next_question() 
# lesson.next_question()
# lesson.next_question()
# lesson.next_question()
# serial.write_line("All done.")
# av = AudioVisual() 
# question = "What planet is closest to the sun my guy huh answer me bruh come on why don't you be cool and stuff????"
# av.display_question(question)
# music.set_built_in_speaker_enabled(True)
# music.set_volume(50)
# # music.ring_tone(Note.C)
# av.play_success_sound()