# J-conjugator
A program that conjugates Japanese words into different forms (polite, plain, negative, past).

# Introduction
Japanese verbs and adjectives have multiple forms that vary based on tense, politeness level and context. Conjugation is challenging, essential yet complex skill for learners. To aid in this process, I propose creating a Python-based tool named "J-conjugator", which will serve as an interactive platform to conjugate Japanese verbs and adjectives, creating a practical and useful database that's easy and accessible to use.

# Objective
Develop a program that:
* Conjugates japanese verbs into various forms (polite, plain, negative, past)
* Handles adjectives (i-adjectives and na-adjectives) including their conjugations for tense and negation.
* A simple and user-friendly interface for learners to practice.

The program will:
1. Include a built-in dictionary of common Japanese verbs and adjectives.
2. Allow users to input custom verbs and adjectives.
3. Support conjugation types such as:
   Verbs: polite, plain, negative, past and te-form.
   adjectives: polite, negative, past negative, etc.
4. Output conjugated forms clearly.
5. Feature an interactive GUI for an enhanced user experience.

# Approach
* Use Python to encode the rules for conjugating verbs and adjectives based on their types.
* Data storage: Use a python dictionary to store verbs and adjectives along with their types.
* Enable user expansion of the dictionary by adding new words.
* Text-based input for selection of word selection and conjugation type.
