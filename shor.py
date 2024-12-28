from manim import *
import numpy as np

class ShorAlgorithm(Scene):
    def construct(self):
        n_qubits = 8  # Nombre de qubits pour le registre
        N = 21  # Nombre à factoriser (pour la démonstration, on va chercher une période d'une fonction f(x) = a^x mod N)
        a = 2 # Un nombre tel que PGCD(a, N) = 1

        # Fonction oracle simulée (pour simplifier)
        def oracle(x):
           return (a ** x) % N

        self.camera.background_color = WHITE

        # ------------------------- PREPARATION ---------------------------

        # Titre
        title = Text("Algorithme de Shor", font_size=60, color=BLACK).to_edge(UP)
        self.play(Write(title))

        # Registre de qubits
        qubits = VGroup(*[Square(side_length=0.5, color=BLACK, fill_opacity=0.1).shift(DOWN * i) for i in range(n_qubits)]).shift(LEFT * 4)
        labels = VGroup(*[Text(f"|0⟩", color=BLACK).scale(0.6).move_to(q) for q in qubits])
        self.play(Create(qubits), Write(labels))

        # Texte sur la superposition
        superposition_text = Text("1. Création de la superposition", color=BLACK, font_size=30).shift(UP*2).shift(RIGHT*4)
        self.play(Write(superposition_text))

        # ----------------------- PHASE 1: Superposition --------------------------
        # Création de la superposition
        hadamard_gates = VGroup(*[Text("H", color=BLUE).scale(1).move_to(q).shift(RIGHT*0.7) for q in qubits])
        self.play(Write(hadamard_gates))

        new_labels = VGroup(*[Text(f"|+⟩", color=BLACK).scale(0.6).move_to(q) for q in qubits])
        self.play(Transform(labels, new_labels))

        self.wait(2)

        self.play(FadeOut(superposition_text),FadeOut(hadamard_gates))

        # ----------------------- PHASE 2: Oracle --------------------------
        # Texte sur l'oracle
        oracle_text = Text("2. Application de l'Oracle", color=BLACK, font_size=30).shift(UP*2).shift(RIGHT*4)
        self.play(Write(oracle_text))

        # Oracle simulé (simplifié)
        oracle_box = Rectangle(height=2, width=3, color=BLUE, fill_opacity=0.2).shift(RIGHT*4.5)
        oracle_label = Text("Oracle (f(x) = a^x mod N)", color=BLACK, font_size=20).move_to(oracle_box)
        self.play(Create(oracle_box), Write(oracle_label))

        #On passe des |+> à des |f(x)>
        oracle_result_labels = VGroup(*[Text(f"|{oracle(i)} mod {N}⟩", color=BLACK).scale(0.6).move_to(qubits[i]) for i in range(n_qubits) ])
        self.play(Transform(labels, oracle_result_labels))

        self.wait(2)

        self.play(FadeOut(oracle_text),FadeOut(oracle_box),FadeOut(oracle_label))

         # ----------------------- PHASE 3: QFT --------------------------

        qft_text = Text("3. Transformée de Fourier Quantique (QFT)", color=BLACK, font_size=30).shift(UP*2).shift(RIGHT*4)
        self.play(Write(qft_text))

        # Boîte QFT
        qft_box = Rectangle(height=2, width=3, color=GREEN, fill_opacity=0.2).shift(RIGHT*4.5)
        qft_label = Text("QFT", color=BLACK, font_size=25).move_to(qft_box)
        self.play(Create(qft_box), Write(qft_label))

        self.wait(1)

        # Exemple de l'effet de la QFT (en se basant sur la période)
        period = 4 # période
        qft_result_labels = VGroup()
        for i in range(n_qubits) :
            prob = np.abs(np.exp(2*np.pi * 1j * (period-1)* i/pow(2,n_qubits)))/np.sqrt(pow(2,n_qubits))
            qft_result_labels.add(Text(f"|β~{prob:.2f}⟩", color=BLACK).scale(0.6).move_to(qubits[i]) )

        self.play(Transform(labels, qft_result_labels))
        self.wait(2)

        self.play(FadeOut(qft_text),FadeOut(qft_box),FadeOut(qft_label))

        # ----------------------- PHASE 4: Mesure --------------------------

        measure_text = Text("4. Mesure", color=BLACK, font_size=30).shift(UP*2).shift(RIGHT*4)
        self.play(Write(measure_text))

        # Mesure
        measure_arrow = Arrow(start=RIGHT*3.5, end=RIGHT*5.5, color=BLACK)
        measure_label = Text("Mesurer", color=BLACK, font_size=20).move_to(measure_arrow).shift(UP*0.3)
        self.play(Create(measure_arrow), Write(measure_label))

        # Effondrement de l'état et résultat
        measured_value = 1
        measured_label = Text(f"Résultat mesuré: |{measured_value}⟩", color=BLACK, font_size=30).shift(DOWN*3).shift(RIGHT*4)
        self.play(Write(measured_label))

        self.wait(2)

        self.play(FadeOut(measure_text),FadeOut(measure_arrow),FadeOut(measure_label),FadeOut(measured_label))

        # ----------------------- PHASE 5: Périodicité --------------------------

        period_text = Text("5. Détermination de la période", color=BLACK, font_size=30).shift(UP*2).shift(RIGHT*4)
        self.play(Write(period_text))

        period_explanation = Text("Mesures répétées révèlent la période.", color=BLACK, font_size=25).shift(DOWN*0.5).shift(RIGHT*4)
        self.play(Write(period_explanation))

        period_show = Text(f"La période de f(x) est : {period}", color=BLACK, font_size=30).shift(DOWN*2).shift(RIGHT*4)
        self.play(Write(period_show))

        self.wait(3)

        # Nettoyer
        self.play(FadeOut(title,period_text,period_explanation,period_show,qubits,labels,qft_result_labels))
        # self.play(FadeOut(VGroup(*self.mobjects))) # Clean the scene completely
        # self.play(FadeOut(VGroup(*self.mobjects)))