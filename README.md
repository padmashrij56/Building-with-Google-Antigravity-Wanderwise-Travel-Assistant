Building with Google Antigravity | Wanderwise Travel Assistant
This repository documents how I used Google Antigravity to set up and run a Python application with an AI coding agent. Wanderwise is one example from a series of projects I’ve built with agents. It gives me an end-to-end workflow to try, from installing dependencies to running and testing a voice interface in a browser.
My Antigravity workflow
Open the project as a workspace. I opened the local project folder in Antigravity so the agent could work with the project files and see the dependency configuration.
Give the agent a concrete goal. I asked it to set up the Poetry environment, install the dependencies, and run the Gradio app.
Review the proposed commands. I used the review-driven workflow to check the agent’s plan and approve terminal commands as it worked through the setup.
Check the result in the browser preview. I used the Gradio interface to try a travel request, inspect the text response, and check browser audio playback.
The prompt I used
> Use the current workspace. Create a Python virtual environment using Poetry, install the project dependencies, and run the Gradio application. Follow the instructions in the README.
Technology
Technology	Role in the project
Google Antigravity	Agent-assisted development workspace for planning, executing, and reviewing setup and launch steps.
Python and Poetry	Application code, dependency installation, and virtual environment management.
Gradio	Browser interface for microphone input, editable requests, text responses, and audio playback.
Whisper	Speech-to-text transcription for recorded requests.
OpenAI API	Generates travel responses using guidance from `data/travel_bot_context.txt`.
gTTS	Text-to-speech library covered in the project walkthrough.
What Wanderwise does
Speak or type a trip request, edit it before submitting, and read or listen to the response. When the request is broad, Wanderwise asks about details such as dates, budget, interests, and travel companions.
Local setup
You’ll need Python, Poetry, an OpenAI API key, and an internet connection. Use the Python version declared in the project’s `pyproject.toml`.
From the project root, install dependencies.
```bash
   poetry install
   ```
Copy `.env.example` to `.env` and fill in `OPENAI_API_KEY`. Keep `.env` local.
```bash
   cp .env.example .env
   ```
On PowerShell, use `Copy-Item .env.example .env`.
Start the Gradio application using the launch command for your checkout. If you’re working in Google Antigravity, open the project folder and ask the agent to locate the Gradio entry point and launch it in the Poetry environment.
Open the local URL printed by Gradio. The demo used `http://127.0.0.1:7860`. Allow microphone access if you want to record a request.
Try it
Type or say “Plan a two-day trip to Goa with beach activities. I’m traveling with a friend and prefer a moderate budget.” Edit the request as needed, select Submit, then read the response or press play under Voice Response (Browser Playback).
