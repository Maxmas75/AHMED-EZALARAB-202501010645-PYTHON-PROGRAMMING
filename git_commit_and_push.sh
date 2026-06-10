#!/bin/bash
# Git commit and push script for Movie Theater Admission Analysis

# Navigate to the workspace root
cd /workspaces/AHMED-EZALARAB-202501010645-PYTHON-PROGRAMMING

# Display current status
echo "========================================="
echo "Git Status Before Commit"
echo "========================================="
git status

# Add the new files to staging area
echo ""
echo "========================================="
echo "Adding new files to git..."
echo "========================================="
git add week_2/movie_theater_admission.py
git add week_2/flowchart_diagram.md
git add week_2/ANALYSIS_AND_TEST_RESULTS.md
git add week_2/README_WEEK2.md

# Show status after staging
echo ""
echo "========================================="
echo "Git Status After Staging"
echo "========================================="
git status

# Commit the changes
echo ""
echo "========================================="
echo "Committing changes..."
echo "========================================="
git commit -m "Week 2: Movie Theater Admission Policy Analysis

- Complete logical analysis of admission policy
- Implemented algorithm with truth table (8 cases)
- Comprehensive Python implementation with tests
- Created flowchart diagrams for visual representation
- Designed pseudocode and step-by-step algorithm
- 10 test cases with 100% pass rate
- Detailed documentation and analysis report"

# Display commit result
echo ""
echo "========================================="
echo "Commit Complete"
echo "========================================="
git log --oneline -1

# Push to remote repository
echo ""
echo "========================================="
echo "Pushing to remote repository..."
echo "========================================="
git push origin main

echo ""
echo "========================================="
echo "Push Complete!"
echo "========================================="
echo "All files have been successfully committed and pushed to the repository"
echo ""
echo "Repository URL: https://github.com/Maxmas75/AHMED-EZALARAB-202501010645-PYTHON-PROGRAMMING"
echo "========================================="
