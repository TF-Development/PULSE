import random
import time
import sys
from data import questions, outcomes, additional_texts

def get_color_code(color):
    color_map = {
        "reset": "\033[0m",
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        # ... add more as needed
    }
    return color_map.get(color, color_map["reset"])

def print_colored(text, color):
    print(get_color_code(color) + text + get_color_code("reset"))

def typing_effect(text, color="reset", delay=0.1):
    for char in text:
        sys.stdout.write(get_color_code(color) + char + get_color_code("reset"))
        sys.stdout.flush()
        time.sleep(delay)
    print()  # for newline

def time_status_indicator(total_time):
    for _ in range(total_time):
        print(".", end='', flush=True)
        time.sleep(1)
    print_colored("COMPLETE!", "green")

def execute_additional_text(text_entry):
    typing_effect(text_entry["text"], text_entry["color"])
    time_status_indicator(text_entry["time"])

def process_text(name, count=1):
    group = additional_texts[name]
    if group["type"] == "sequence":
        for message in group["messages"]:
            execute_additional_text(message)
    elif group["type"] == "random":
        for _ in range(count):
            message = random.choice(group["messages"])
            execute_additional_text(message)
def get_input():
    while True:
        response = input("Please enter y/yes or n/no: ").lower().strip()
        if response in ["y", "yes"]:
            return "yes"
        elif response in ["n", "no"]:
            return "no"
        else:
            print("Invalid input. Please enter y/yes or n/no.")

def navigate_questions():
    outcome_tags_collected = []
    current_index = 0
    while current_index < len(questions):
        question = questions[current_index]
        typing_effect(question["text"], "blue")

        answer = get_input()

        if answer not in question["answers"]:
            typing_effect("Invalid answer. Please respond with 'yes' or 'no'.", "red")
            continue

        outcome_tags_collected.extend(question["answers"][answer]["outcome_tags"])

        if "next_question" in question["answers"][answer]:
            next_question_id = question["answers"][answer]["next_question"]
            current_index = int(next_question_id) - 1
        else:
            current_index += 1

    return outcome_tags_collected



def execute_outcome(outcome_key):
    outcome = outcomes[outcome_key]
    typing_effect(outcome["text"], outcome["color"])
    time_status_indicator(outcome["time"])

def display_progress(current, total, start_time, interval=5):
    elapsed = time.time() - start_time
    if elapsed >= interval:
        percentage = (current / total) * 100
        typing_effect(f"PROGRESS: {percentage:.2f}%", "yellow")
        return time.time()  # Update the start time
    return start_time

def execute_outcomes_with_interjections(interject_every, text_name, outcome_tags_collected):
    counter = 0
    relevant_outcomes = [k for k, v in outcomes.items() if any(tag in v["tags"] for tag in outcome_tags_collected)]
    total_outcomes = len(relevant_outcomes)
    start_time = time.time()

    for outcome_key in relevant_outcomes:
        execute_outcome(outcome_key)
        counter += 1
        
        start_time = display_progress(counter, total_outcomes, start_time)
        
        if counter % interject_every == 0:
            process_text(text_name, count=1)


def process_flow():
    flow = [
        {"action": "text", "name": "boot"},
        {"action": "questions"},
        {"action": "text", "name": "initiation", "count": 1},
        {"action": "outcomes_with_interjections", "interject_every": 3, "interject_with": "text_element_B"}
        #  {"action": "text", "name": "element_D", "count": 1},
        #  {"action": "text", "name": "shutdown"}
    ]
    outcome_tags_collected = []
    for step in flow:
        action = step["action"]
        if action == "text":
            process_text(step["name"], count=step.get("count", 1))
        elif action == "questions":
            outcome_tags_collected = navigate_questions()
        elif action == "outcomes_with_interjections":
            execute_outcomes_with_interjections(step["interject_every"], step["interject_with"], outcome_tags_collected)


if __name__ == "__main__":
    process_flow()