import os
import configparser
from pathlib import Path

# --- CONFIGURATION ---
# The name of the file that contains patterns to ignore.
# Behaves like .gitignore.
IGNORE_FILE = ".scraignore"

# The name of the file that defines the output groups.
GROUPS_CONFIG_FILE = "scrape_groups.config"

# The separator to be placed between file contents in the output.
SEPARATOR = "\n---\n\n"
# --- END CONFIGURATION ---


def load_ignore_patterns(root_path):
    """Loads ignore patterns from the .scraignore file."""
    ignore_file_path = Path(root_path) / IGNORE_FILE
    patterns = []
    if ignore_file_path.exists():
        with open(ignore_file_path, "r", encoding="utf-8") as f:
            for line in f:
                stripped_line = line.strip()
                # Ignore comments and empty lines
                if stripped_line and not stripped_line.startswith("#"):
                    patterns.append(stripped_line)
    return patterns


def is_ignored(path_str, ignore_patterns):
    """
    Checks if a given file path should be ignored based on the patterns.
    - Converts backslashes to forward slashes for cross-platform consistency.
    - Matches if the path starts with any of the ignore patterns.
    """
    # Normalize path separators for consistent matching
    normalized_path = path_str.replace("\\", "/")
    for pattern in ignore_patterns:
        if normalized_path.startswith(pattern):
            return True
    return False


def load_group_definitions(root_path):
    """Loads group definitions from the scrape_groups.config file."""
    config_file_path = Path(root_path) / GROUPS_CONFIG_FILE
    if not config_file_path.exists():
        print(f"Error: Configuration file '{GROUPS_CONFIG_FILE}' not found.")
        print("Please create it in your project's root directory.")
        return None

    config = configparser.ConfigParser(allow_no_value=True)
    config.read(config_file_path)

    groups = {}
    for section in config.sections():
        # The keys in each section are the paths to include
        # config.options(section) returns the list of paths
        paths_to_include = [path.replace("\\", "/") for path in config.options(section)]
        groups[section] = paths_to_include

    return groups


def scrape_project():
    """Main function to scrape the project based on configurations."""
    project_root = Path(".").resolve()
    print(f"Starting scrape in directory: {project_root}\n")

    ignore_patterns = load_ignore_patterns(project_root)
    print(f"Loaded {len(ignore_patterns)} ignore patterns from '{IGNORE_FILE}'.")

    groups = load_group_definitions(project_root)
    if not groups:
        return

    print(f"Found {len(groups)} output groups in '{GROUPS_CONFIG_FILE}'.\n")

    # A dictionary to hold all collected file contents for each group
    group_contents = {group_name: [] for group_name in groups.keys()}

    # Walk through the entire project directory
    for root, dirs, files in os.walk(project_root, topdown=True):
        # Create a relative path from the project root for comparison
        relative_root = Path(root).relative_to(project_root)

        # Filter out ignored directories in-place to prevent os.walk from traversing them
        # We need to check the string representation of the path
        dirs[:] = [
            d for d in dirs if not is_ignored(str(relative_root / d), ignore_patterns)
        ]

        for file in files:
            file_path = relative_root / file
            file_path_str = str(file_path).replace("\\", "/")

            # Check if the file itself is ignored
            if is_ignored(file_path_str, ignore_patterns):
                continue

            # Check which group this file belongs to
            for group_name, include_paths in groups.items():
                for include_path in include_paths:
                    if file_path_str.startswith(include_path):
                        try:
                            with open(
                                project_root / file_path, "r", encoding="utf-8"
                            ) as f:
                                content = f.read()

                            formatted_content = (
                                f"File Name: {file_path_str}\n\n{content}"
                            )
                            group_contents[group_name].append(formatted_content)
                            # Once matched and added, break to avoid adding to multiple groups
                            break
                        except Exception as e:
                            print(f"Could not read file {file_path_str}: {e}")

    # Write the collected contents to the output files
    for group_name, contents in group_contents.items():
        if not contents:
            print(
                f"Warning: No files found for group '{group_name}'. The output file will not be created."
            )
            continue

        output_file_path = project_root / group_name
        try:
            with open(output_file_path, "w", encoding="utf-8") as f:
                f.write(SEPARATOR.join(contents))
            print(f"Successfully created '{group_name}' with {len(contents)} files.")
        except Exception as e:
            print(f"Error writing to file {group_name}: {e}")

    print("\nScraping complete.")


if __name__ == "__main__":
    scrape_project()