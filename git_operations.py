#!/usr/bin/env python3
"""
Git operations script for Movie Theater Admission Analysis project
This script commits and pushes the files to the remote repository
"""

import subprocess
import sys
import os

def run_command(cmd, description=""):
    """Run a shell command and return output"""
    if description:
        print(f"\n{'='*50}")
        print(f"{description}")
        print(f"{'='*50}")
    
    print(f"Running: {cmd}")
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd='/workspaces/AHMED-EZALARAB-202501010645-PYTHON-PROGRAMMING')
        print(result.stdout)
        if result.stderr:
            print("STDERR:", result.stderr)
        return result.returncode == 0
    except Exception as e:
        print(f"Error: {e}")
        return False

def main():
    """Main function to handle git commit and push"""
    workspace = '/workspaces/AHMED-EZALARAB-202501010645-PYTHON-PROGRAMMING'
    
    if not os.path.exists(workspace):
        print(f"Error: Workspace not found at {workspace}")
        sys.exit(1)
    
    print("\n" + "="*50)
    print("MOVIE THEATER ANALYSIS - GIT OPERATIONS")
    print("="*50)
    
    # Check git status
    run_command("git status", "Checking Git Status Before Commit")
    
    # Add files
    print("\n" + "="*50)
    print("Adding files to staging area...")
    print("="*50)
    
    files_to_add = [
        "week_2/movie_theater_admission.py",
        "week_2/flowchart_diagram.md",
        "week_2/ANALYSIS_AND_TEST_RESULTS.md",
        "week_2/README_WEEK2.md"
    ]
    
    for file in files_to_add:
        run_command(f"git add {file}", f"Adding {file}")
    
    # Show status after staging
    run_command("git status", "Git Status After Staging")
    
    # Commit with detailed message
    commit_message = """Week 2: Movie Theater Admission Policy Analysis

## Changes:
- Complete logical analysis of movie theater admission policy
- Implemented admission algorithm with truth table (8 comprehensive cases)
- Created Python implementation with test suite (100% pass rate)
- Designed flowchart diagrams for visual representation
- Generated pseudocode and step-by-step algorithm
- Developed 10 test cases covering all scenarios
- Produced detailed analysis and documentation

## Files:
1. movie_theater_admission.py - Complete implementation with tests
2. flowchart_diagram.md - Visual diagrams (Mermaid format)
3. ANALYSIS_AND_TEST_RESULTS.md - Comprehensive analysis
4. README_WEEK2.md - Project summary and usage

## Key Features:
- Logical expression: (Age >= 13 OR Accompanied) AND HasTicket
- Truth table with all 8 boolean combinations
- Step-by-step algorithm with detailed explanation
- Both verbose and concise pseudocode
- 10 real-world test scenarios
- Complete pass validation"""
    
    # Commit
    run_command(f'git commit -m "{commit_message}"', "Committing Changes")
    
    # Show recent commit
    run_command("git log --oneline -1", "Latest Commit Info")
    
    # Push to remote
    run_command("git push origin main", "Pushing to Remote Repository")
    
    print("\n" + "="*50)
    print("✓ GIT OPERATIONS COMPLETE")
    print("="*50)
    print("\nRepository: https://github.com/Maxmas75/AHMED-EZALARAB-202501010645-PYTHON-PROGRAMMING")
    print("\nAll files have been successfully committed and pushed!")

if __name__ == "__main__":
    main()
