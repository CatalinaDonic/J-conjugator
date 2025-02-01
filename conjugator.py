import tkinter as tk
import random

class JapaneseConjugator:
    def __init__(self):
        # Full verb dictionary with types (ru-verbs, u-verbs, irregular verbs)
        self.verbs = {
            "あく": "u",  # aku (open)
            "あるく": "u",  # aruku (walk)
            "いく": "u",  # iku (go)
            "おく": "u",  # oku (put)
            "かく": "u",  # kaku (write)
            "きく": "u",  # kiku (listen)
            "さく": "u",  # saku (bloom)
            "つく": "u",  # tsuku (arrive)
            "なく": "u",  # naku (sing)
            "はく": "u",  # haku (put on)
            "はたらく": "u",  # hataraku (work)
            "ひく": "u",  # hiku (pull)
            "ふく": "u",  # fuku (breathe)
            "みがく": "u",  # migaku (polish)
            "およぐ": "u",  # oyogu (swim)
            "ぬぐ": "u",  # nugu (undress)
            "おす": "u",  # osu (push)
            "かえす": "u",  # kaesu (return)
            "かす": "u",  # kasu (lend)
            "けす": "u",  # kesu (turn off)
            "さす": "u",  # sasu (put up an umbrella)
            "だす": "u",  # dasu (post)
            "なくす": "u",  # nakusu (lose)
            "はなす": "u",  # hanasu (speak)
            "わたす": "u",  # watasu (hand over)
            "しぬ": "u",  # shinu (die)
            "あそぶ": "u",  # asobu (play)
            "よぶ": "u",  # yobu (call)
            "すむ": "u",  # sumu (live)
            "たのむ": "u",  # tanomu (ask)
            "のむ": "u",  # nomu (drink)
            "やすむ": "u",  # yasumu (rest)
            "よむ": "u",  # yomu (read)
            "あう": "u",  # au (meet)
            "あらう": "u",  # arau (wash)
            "いう": "u",  # iu (say)
            "うたう": "u",  # utau (sing)
            "かう": "u",  # kau (buy)
            "すう": "u",  # suu (smoke)
            "ちがう": "u",  # chigau (differ)
            "つかう": "u",  # tsukau (use)
            "ならう": "u",  # narau (learn)
            "たつ": "u",  # tatsu (stand up)
            "まつ": "u",  # matsu (wait)
            "もつ": "u",  # motsu (hold)
            "うる": "u",  # uru (sell)
            "おわる": "u",  # owaru (finish)
            "かえる": "u",  # kaeru (return)
            "かかる": "u",  # kakaru (take time)
            "かぶる": "u",  # kaburu (wear a hat)
            "きる": "u",  # kiru (cut)
            "こまる": "u",  # komaru (be in trouble)
            "しまる": "u",  # shimaru (close)
            "しる": "u",  # shiru (know)
            "すわる": "u",  # suwaru (sit)
            "つくる": "u",  # tsukuru (make)
            "とまる": "u",  # tomaru (stop)
            "とる": "u",  # toru (take)
            "なる": "u",  # naru (become)
            "のぼる": "u",  # noboru (climb)
            "のる": "u",  # noru (ride)
            "はいる": "u",  # hairu (enter)
            "はしる": "u",  # hashiru (run)
            "はじまる": "u",  # hajimaru (start)
            "はる": "u",  # haru (stick)
            "ふる": "u",  # furu (fall rain)
            "まがる": "u",  # magaru (turn)
            "やる": "u",  # yaru (do)
            "わかる": "u",  # wakaru (understand)
            "わたる": "u",  # wataru (cross)
            "あける": "ru",  # akeru (open something)
            "あげる": "ru",  # ageru (give)
            "いれる": "ru",  # ireru (put in)
            "うまれる": "ru",  # umareru (be born)
            "おしえる": "ru",  # oshieru (teach)
            "おぼえる": "ru",  # oboeru (memorize)
            "かける": "u",  # kakeru (make a call)
            "きえる": "ru",  # kieru (disappear)
            "しめる": "u",  # shimeru (close)
            "たべる": "ru",  # taberu (eat)
            "つかれる": "ru",  # tsukareru (get tired)
            "でる": "ru",  # deru (leave)
            "はれる": "ru",  # hareru (clear up)
            "みせる": "ru",  # miseru (show)
            "わすれる": "ru",  # wasureru (forget)
            "あびる": "ru",  # abiru (bathe)
            "いる": "ru",  # iru (exist, living)
            "おきる": "ru",  # okiru (get up)
            "おりる": "ru",  # oriru (get off)
            "かりる": "ru",  # kariru (borrow)
            "きる": "u",  # kiru (wear)
            "できる": "ru",  # dekiru (can do)
            "みる": "ru",  # miru (see)
            "する": "irregular",  # suru (do)
            "くる": "irregular"   # kuru (come)
        }
        self.score = 0  # Initialize score

    # function to conjugate 'u'-type verbs, separated into different groups according to word ending
    def conjugate_verb_u(self, verb, form):
        if verb.endswith("う"):
            stem = verb[:-1]
            return stem + ("います" if form == "polite" else "わない" if form == "negative" else "った")
        elif verb.endswith("つ") or verb.endswith("る"):
            stem = verb[:-1]
            return stem + ("ります" if form == "polite" else "らない" if form == "negative" else "った")
        elif verb.endswith("む") or verb.endswith("ぶ") or verb.endswith("ぬ"):
            stem = verb[:-1]
            return stem + ("みます" if form == "polite" else "まない" if form == "negative" else "んだ")
        elif verb.endswith("く"):
            stem = verb[:-1]
            return stem + ("きます" if form == "polite" else "かない" if form == "negative" else "いた")
        elif verb.endswith("ぐ"):
            stem = verb[:-1]
            return stem + ("ぎます" if form == "polite" else "がない" if form == "negative" else "いだ")
        elif verb.endswith("す"):
            stem = verb[:-1]
            return stem + ("します" if form == "polite" else "さない" if form == "negative" else "した")
        else:
            return verb
        
    # function to conjugate 'ru'-type verbs
    def conjugate_verb_ru(self, verb, form):
        stem = verb[:-1]
        if form == "polite":
            return stem + "ます"
        elif form == "negative":
            return stem + "ません"
        elif form == "past":
            return stem + "ました"

    # function to conjugate 'irregular' type verbs
    def conjugate_irregular(self, verb, form):
        if verb == "する":
            if form == "polite":
                return "します"
            elif form == "negative":
                return "しません"
            elif form == "past":
                return "しました"
        elif verb == "くる":
            if form == "polite":
                return "きます"
            elif form == "negative":
                return "きません"
            elif form == "past":
                return "きました"
        else:
            return verb

    # Function that classifies the verb to the correct conjugation function, according to the verb dictionary
    def conjugate_verb(self, verb, form):
        verb_type = self.verbs.get(verb, None)
        if verb_type == "u":
            return self.conjugate_verb_u(verb, form)
        elif verb_type == "ru":
            return self.conjugate_verb_ru(verb, form)
        elif verb_type == "irregular":
            return self.conjugate_irregular(verb, form)
        else:
            return "Unknown verb"

    # Quiz interface
    def run_quiz(self):
        def show_intro():
            # Hide quiz widgets during intro
            for widget in quiz_widgets:
                widget.pack_forget()

            # Display intro screen
            intro_label.pack(pady=10)
            instructions_label.pack(pady=10)
            start_button.pack(pady=10)

        def start_quiz():
            # Hide intro widgets
            intro_label.pack_forget()
            instructions_label.pack_forget()
            start_button.pack_forget()

            # Show quiz widgets
            for widget in quiz_widgets:
                widget.pack(pady=5)

            next_question()

        def generate_question():
            verb, verb_type = random.choice(list(self.verbs.items()))
            form = random.choice(["polite", "negative", "past"])
            correct_answer = self.conjugate_verb(verb, form)

            # Generate 3 random incorrect answers
            all_answers = [correct_answer]
            while len(all_answers) < 4:
                random_verb = random.choice(list(self.verbs.keys()))
                random_form = random.choice(["polite", "negative", "past"])
                random_conjugation = self.conjugate_verb(random_verb, random_form)
                if random_conjugation != correct_answer and random_conjugation not in all_answers:
                    all_answers.append(random_conjugation)

            random.shuffle(all_answers)
            question_label.config(text=f"What is the {form} form of '{verb}'?")
            for i, answer in enumerate(all_answers):
                buttons[i].config(text=answer, command=lambda a=answer: check_answer(a, correct_answer))

        # Make sure the message displayed to the user includes the actual correct answer and add 1 point per correct answer
        def check_answer(selected_answer, correct_answer):
            nonlocal score_label
            if selected_answer == correct_answer:
                self.score += 1
                result_label.config(text="Correct!", fg="green")
            else:
                result_label.config(text=f"Incorrect! Correct answer: {correct_answer}", fg="red")

            score_label.config(text=f"Score: {self.score}")
            next_button.config(state="normal")  # Enable the Next button

        def next_question():
            result_label.config(text="")  # Clear previous result message
            next_button.config(state="disabled")  # Disable the Next button again
            generate_question()

        root = tk.Tk()
        root.title("Japanese Conjugation Quiz")

        # Intro screen widgets
        intro_label = tk.Label(root, text="Welcome to the Japanese Conjugation Quiz!", font=("Arial", 16))
        instructions_label = tk.Label(root, text="Test your knowledge of Japanese verb conjugations.\n"
                                                 "Choose the correct conjugated form from the options provided.", font=("Arial", 12))
        start_button = tk.Button(root, text="Start Quiz", font=("Arial", 12), command=start_quiz)

        # Quiz screen widgets
        question_label = tk.Label(root, text="", font=("Arial", 14))
        buttons = [tk.Button(root, text="", font=("Arial", 12), width=20) for _ in range(4)]
        result_label = tk.Label(root, text="", font=("Arial", 12))
        score_label = tk.Label(root, text=f"Score: {self.score}", font=("Arial", 12))
        next_button = tk.Button(root, text="Next", font=("Arial", 12), state="disabled", command=next_question)

        # Group quiz widgets for easy show/hide
        quiz_widgets = [question_label, score_label] + buttons + [result_label, next_button]

        # Show intro screen on startup
        show_intro()

        root.mainloop()

if __name__ == "__main__":
    conjugator = JapaneseConjugator()
    conjugator.run_quiz()
