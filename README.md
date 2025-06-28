Context-Packer 🧰✨
Stop re-explaining your project to your AI. Start getting better code.

Context-Packer is a lightweight utility script that bundles your project's source code into clean, organized text files. It's the ultimate solution for providing complete and coherent context to AI/LLM assistants like GPT-4, Gemini, and Claude.


The Pain Point: AI Context Amnesia
Large Language Models are powerful coding partners, but they suffer from a critical flaw: a limited memory. When you're deep in a complex project, you're forced to:

Manually copy-paste code from dozens of different files.
Constantly remind the AI of your project's structure and conventions.
Waste precious time re-explaining the context with every new chat session.
Receive generic, out-of-context answers from an AI that doesn't have the full picture.
This breaks your workflow and reduces the quality of the AI's assistance.

The Solution: Perfect Context, Every Time
Context-Packer solves this problem elegantly. It acts as a "context bundler" for your project. By reading a simple configuration, it traverses your source tree and intelligently packages all your relevant code into logical, consolidated .txt files (e.g., backend.txt, frontend.txt).

Now, you can start any AI session by providing a complete, perfectly formatted snapshot of your entire codebase with a single copy-paste.

Features
🧠 Intelligent Grouping: Define custom bundles like backend, frontend, database, etc., to group related parts of your project.
🚫 Configurable Ignoring: Uses a .scraignore file (with a familiar .gitignore syntax) to exclude dependencies (node_modules/, vendor/), logs, and other noise.
📄 Clean & Clear Output: Each file's content is prepended with its full path (File Name: app/Http/Controllers/UserController.php), making the context easy for both you and the AI to understand.
🌐 Framework Agnostic: While born from a Laravel/Vue.js project, it works perfectly with any framework (React, Django, Rails, etc.) or even vanilla projects.
🚀 Lightweight & Fast: Built with standard Python libraries. No external dependencies to install.
The Tutorial: Getting Started in 2 Minutes
Follow these simple steps to integrate Context-Packer into your workflow.

Prerequisites
Python (Version 3.6 or newer) installed on your system.
Step 1: Add the Files to Your Project
Download or create the following three files in the root directory of your project:

project_scraper.py (The core script)
.scraignore (To define files/folders to ignore)
scrape_groups.config (To define your output files and their contents)
Step 2: Configure Files to Ignore
Open the .scraignore file. Add the names of any directories or files you want the script to skip. This is crucial for keeping your context files clean and focused on your source code.

Example .scraignore:

# Dependencies
node_modules/
vendor/

# Storage, Cache, and Logs
storage/
bootstrap/cache/

# Compiled Assets & Public Dirs
public/build/
public/hot

# Environment & Secrets
.env
.env.*
*.log

# Git & System Files
.git/
.idea/
.vscode/
.DS_Store

# Context-Packer's own files
project_scraper.py
.scraignore
scrape_groups.config
*.txt
Step 3: Define Your Context Groups
Open scrape_groups.config. This is where you define your output files.

Each group starts with a filename in brackets, like [backend.txt].
Underneath the group name, list the directories or specific files you want to include in that bundle.
Example scrape_groups.config for a Laravel/Vue Project:

[backend.txt]
# The section name [backend.txt] will be the output file.
# Add all backend-related paths below.
app/
routes/
database/migrations/
database/seeders/
config/
bootstrap/app.php
composer.json
artisan

[frontend.txt]
# This will create a separate frontend.txt file.
resources/js/
resources/css/
resources/views/
tailwind.config.js
vite.config.js
postcss.config.js
package.json
Step 4: Run the Script
Open your terminal, navigate to your project's root directory, and run the script:

Bash

python project_scraper.py
Note: If you use python3 primarily, you may need to run python3 project_scraper.py.

Step 5: Use Your Context!
The script will generate backend.txt and frontend.txt (or whatever you named them) in your root directory.

Now, simply:

Open the relevant file (e.g., backend.txt).
Select all and copy the entire content.
Paste it into your AI chat prompt as the very first message.
Your AI now has a perfect, comprehensive memory of your project.

Example Use Case
Imagine you need to add a new API endpoint in Laravel that fetches data and displays it in a Vue component.

Old Way: Copy your api.php routes file. Copy your UserController.php. Copy your User.php model. Copy your UserResource.php. Copy your api-service.js. Copy your MyVueComponent.vue. Forget a file and get an error.
With Context-Packer: Start a new chat. Copy the contents of backend.txt and frontend.txt. Then, simply ask: "Add a new API endpoint at /api/users/{id} that returns a user's details, and show me how to call it from a Vue component."
The AI will provide a complete, accurate, and context-aware solution because it understands your entire application structure.

Contributing
This is a tool by a developer, for developers. Contributions are highly welcome! Feel free to fork the repository, suggest features, open issues, and submit pull requests.

License
This project is licensed under the MIT License. See the LICENSE file for details.