class Lesson {
    static current_question_index: number
    private ___current_question_index_is_set: boolean
    private ___current_question_index: number
    get current_question_index(): number {
        return this.___current_question_index_is_set ? this.___current_question_index : Lesson.current_question_index
    }
    set current_question_index(value: number) {
        this.___current_question_index_is_set = true
        this.___current_question_index = value
    }
    
    static questions: any[]
    private ___questions_is_set: boolean
    private ___questions: any[]
    get questions(): any[] {
        return this.___questions_is_set ? this.___questions : Lesson.questions
    }
    set questions(value: any[]) {
        this.___questions_is_set = true
        this.___questions = value
    }
    
    audio_visual: AudioVisual
    planet_detection: PlanetDetection
    public static __initLesson() {
        Lesson.current_question_index = 0
        Lesson.questions = [ {
            "question" : "Which planet is closest to sun?",
            "answer" : "Mercury",
        }
        , {
            "question" : "Which planet is known as the Red Planet?",
            "answer" : "Mars",
        }
        , {
            "question" : "Which planet is the largest?",
            "answer" : "Jupiter",
        }
        , {
            "question" : "Which planet is the smallest?",
            "answer" : "Saturn",
        }
        , {
            "question" : "Which planet is the furthest from the sun?",
            "answer" : "Venus",
        }
        ]
    }
    
    //  TODO: ...other questions
    constructor() {
        this.audio_visual = new AudioVisual()
        this.planet_detection = new PlanetDetection()
    }
    
    public start_lesson() {
        /** Method to start the lesson. */
        this.next_question()
    }
    
    public next_question() {
        let id: any;
        /** Method to proceed to the next question. */
        this.current_question_index += 1
        if (this.current_question_index < this.questions.length) {
            this.audio_visual.display_question(this.questions[this.current_question_index]["question"])
            id = this.planet_detection.detect_planet()
            I2C_LCD1602.clear()
        } else {
            //  self.check_response(id)
            this.finish_lesson()
        }
        
    }
    
    public check_response(planet: string) {
        /** Method to check the response.

        Args:
        planet (str): The planet name in the response.
        
 */
        let correct_answer = this.questions[this.current_question_index]["answer"]
        if (planet == correct_answer) {
            this.audio_visual.display_success(planet)
        } else {
            //  self.audio_visual.play_success_sound()
            //  wait(1000)
            //  self.audio_visual.play_rotation_sound()
            //  speed = self.get_orbit_speed(planet)
            //  self.planet_motion.rotate_arm(speed)
            this.audio_visual.display_failure(planet)
        }
        
    }
    
    //  self.audio_visual.play_fail_sound()
    public finish_lesson() {
        /** Method to finish the lesson. */
        
    }
    
}

Lesson.__initLesson()

class PlanetDetection {
    constructor() {
        JoyPiAdvanced.rfidInit()
    }
    
    public detect_planet() {
        /** Method to detect a planet.

        Returns:
        str: The detected planet name.
        
 */
        //  Code to detect which planet is placed on the sensor
        let planet_ids = {
            259584497701 : "Mercury",
            809057392480 : "Venus",
        }
        
        let id = 0
        while (id == 0) {
            id = JoyPiAdvanced.rfidReadId()
        }
        while (true) {
            if (pins.digitalReadPin(DigitalPin.P1) == 0) {
                break
            }
            
        }
        if (planet_ids.indexOf(id) >= 0) {
            return planet_ids[id]
        }
        
    }
    
}

class AudioVisual {
    constructor() {
        
    }
    
    public display_success(planet: string) {
        /** Method to display a success message.

        Args:
        planet (str): The planet name in the success message.
        
 */
        //  Code to display success message on LED and play correct sound
        I2C_LCD1602.clear()
        I2C_LCD1602.ShowString(planet, 0, 0)
        I2C_LCD1602.ShowString("is correct!", 1, 0)
    }
    
    public display_failure(planet: string) {
        /** Method to display a failure message.

        Args:
        planet (str): The planet name in the failure message.
        
 */
        //  Code to display failure message on LED
        I2C_LCD1602.ShowString("Incorrect...", 0, 0)
        I2C_LCD1602.ShowString("Try again.", 1, 0)
    }
    
    public display_lesson_complete(message: string) {
        /** Method to display a lesson complete message.

        Args:
        message (str): The message to be displayed.
        
 */
    }
    
    public play_success_sound() {
        /** Method to play success sound. */
        //  Code to play the specified sound
        music.play(music.tonePlayable(784, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
        music.play(music.tonePlayable(784, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
    }
    
    public play_fail_sound() {
        /** Method to play fail sound. */
        //  Code to play the specified sound
        
    }
    
    public play_rotation_sound() {
        /** Method to play rotation sound. */
        //  Star Wars
        music.play(music.tonePlayable(392, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
        music.play(music.tonePlayable(587, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
        music.play(music.tonePlayable(523, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
        music.play(music.tonePlayable(494, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
        music.play(music.tonePlayable(440, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
        music.play(music.tonePlayable(784, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
        music.play(music.tonePlayable(587, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
        music.play(music.tonePlayable(523, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
        music.play(music.tonePlayable(494, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
        music.play(music.tonePlayable(440, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
        music.play(music.tonePlayable(784, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
        music.play(music.tonePlayable(587, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
        music.play(music.tonePlayable(523, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
        music.play(music.tonePlayable(494, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
        music.play(music.tonePlayable(523, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
        music.play(music.tonePlayable(440, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
        //  Code to play the specified sound
        
    }
    
    public stop_rotation_sound() {
        /** Method to stop rotation sound. */
        //  Code to stop the specified sound
        
    }
    
    public play_lesson_complete_sound(txt: any, aChar: any) {
        /** Method to play lesson complete sound. */
        //  Code to play the specified sound
        
    }
    
    public myrfind(txt: string, aChar: string): number {
        for (let i = txt.length - 1; i > -1; i += -1) {
            if (txt[i] == aChar) {
                return i
            }
            
        }
        return -1
    }
    
    public display_question(question: string) {
        let row: number;
        /** Method to display the question.

        Args:
        question (str): The question to be displayed.
        
 */
        //  pd = PlanetDetection()
        let oldlastindex = 0
        let lastindex = 0
        let lastcompare = 0
        let i = 0
        //  display = True
        let done = false
        let line = ""
        let lines = []
        serial.writeLine("Hello.")
        //  # # serial.write_line(str(len(question)-1))
        while (lastindex < question.length - 1) {
            lastcompare = 16 + lastindex
            //  # serial.write_line(str(lastcompare))
            if (question.length - 1 < lastcompare) {
                lastcompare = question.length - 1
                done = true
            }
            
            //  serial.write_line("Done is true.")
            if (question[lastcompare] != " ") {
                //  x = 1
                //  self.myrfind("a", "b")
                lastindex = this.myrfind(question.slice(oldlastindex, lastcompare), " ") + oldlastindex
            } else {
                //  serial.write_line(str(lastindex))
                lastindex = lastcompare
            }
            
            if (lastcompare >= question.length - 1) {
                lastindex = question.length
            }
            
            line = question.slice(oldlastindex, lastindex)
            oldlastindex = lastindex
            i += 1
            //  serial.write_line(line)
            lines.push(line)
            if (done) {
                break
            }
            
        }
        let j = 0
        serial.writeLine("Hello again.")
        while (j < lines.length) {
            if (j > 1 && j % 2 == 0) {
                basic.pause(3000)
                I2C_LCD1602.clear()
            }
            
            row = j % 2
            I2C_LCD1602.ShowString(lines[j], 0, row)
            j += 1
        }
    }
    
}

//  if (j >= len(lines)):
//      basic.pause(3000)
//      I2C_LCD1602.clear()
//      j = 0
// # ALL MAIN CODE HERE ##
//  I2C_LCD1602.lcd_init(39)
//  pins.set_pull(DigitalPin.P1, PinPullMode.PULL_UP)
serial.writeLine("This is running fr8.")
let pd = new PlanetDetection()
let planet = pd.detect_planet()
serial.writeLine("" + planet)
