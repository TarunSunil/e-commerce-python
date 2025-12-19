import sys
import importlib.metadata
import re

def check_requirements(requirements_file='requirements.txt'):
    print(f"Checking requirements from {requirements_file}...")
    
    try:
        with open(requirements_file, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: {requirements_file} not found.")
        return

    missing = []
    installed = []
    
    # Basic parsing of requirements.txt (handles ==, >=, and simple names)
    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
            
        # Split package name from version constraints
        # This is a simplified parser
        match = re.match(r'^([a-zA-Z0-9_\-\[\]]+)(.*)$', line)
        if not match:
            continue
            
        pkg_name_full = match.group(1)
        constraints = match.group(2)
        
        # Handle extras like uvicorn[standard]
        pkg_name = pkg_name_full.split('[')[0]
        
        try:
            version = importlib.metadata.version(pkg_name)
            installed.append(f"{pkg_name_full} (found {version})")
        except importlib.metadata.PackageNotFoundError:
            missing.append(line)

    print("\n--- Status ---")
    if installed:
        print(f"Installed ({len(installed)}):")
        for p in installed:
            print(f"  - {p}")
    
    if missing:
        print(f"\nMissing ({len(missing)}):")
        for p in missing:
            print(f"  - {p}")
        print("\nTo install missing packages, run:")
        print(f"pip install -r {requirements_file}")
    else:
        print("\nAll requirements are satisfied!")

if __name__ == "__main__":
    check_requirements()
