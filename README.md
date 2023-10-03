# P.U.L.S.E. Board Game Transformation Module
_Programmable Unit for Lust & Sensory Enhancement_

## Overview

P.U.L.S.E. is a transformation system simulator intended for use in roleplay or other fantasy engagements which include a transformation element. Upon running the module, users are faced with a series of questions. Their responses determine the transformation outcome of their character. As the program executes, the user is shown progress updates and various status messages with the intent of immersing them in the narrative of their character's transformation.

## Features

1. **Dynamic Questioning System:** Users are posed with sets of questions that determine the outcome of their character's transformation.
2. **Engaging Transformation Sequence:** Real-time progress indicators and thematic status messages enhance immersion.
3. **Modular Design:** Allows for easy expansion of questions and outcomes as needed.

## Installation & Usage

**Prerequisites:** 
- Ensure you have the latest version of Python installed.

1. **Clone the Repository:**
    \```bash
    git clone https://github.com/TF-Development/PULSE.git
    \```

2. **Navigate to the Directory:**
    \```bash
    cd PULSE
    \```

3. **Run the Application:**
    \```bash
    python transformation_engine.py
    \```

4. Follow the on-screen prompts and answer the questions as they appear.

## Development

### Structure

The core logic for the transformation is located in `transformation_engine.py`. Here, the answers to the questions are processed, and the resulting transformation sequence is determined.

Questions, their possible outcomes, and other text elements are stored in `data.py`.
### Extending the Questionnaire

To add more questions or outcomes:

1. Open `data.py` in your preferred text editor.
2. Follow the existing structure to add more questions or modify existing ones.
3. Ensure any new major sections are properly defined in `transformation_engine.py`.

### Updating the Transformation Sequence

All transformation sequences, progress updates, and status messages are managed between `transformation_engine.py` & `data.py`. Modify the existing functions or add new ones to introduce fresh transformation narratives.

## Contributing

Contributions are welcome and encouraged! If you have ideas or improvements, please fork this repository and create a pull request. Ensure your changes don't break existing functionality.

## License

This project is licensed under the GNU General Public License v3.0 (GPLv3).