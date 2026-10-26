# K-5 Cyber Adventures: Teacher Guide

## Welcome to the K-5 Cyber Range 🎯

This guide helps educators implement engaging cybersecurity education for elementary students.

## Getting Started

1. **Create Your K-5 Track**
   - In Admin Panel → Exercises → Tracks & Levels
   - Create a new track called "K-5 Cyber Adventures"
   - Add levels (1, 2, 3, etc.) for progressive learning

2. **Assign Scenarios**
   - Each exercise should be assigned to appropriate K-5 level
   - Ensure exercises are enabled and visible

## Age-Appropriate Learning Objectives

### For Grades K-2:
- Basic network discovery using ping
- Simple file access and retrieval
- Understanding that computers can communicate

### For Grades 3-5:
- Port scanning with nmap (basic)
- File system navigation
- Flag identification and submission

## Engagement Strategies

### Visual Learning
- Use colorful interfaces and clear instructions
- Include simple diagrams in README.md files
- Provide visual feedback when challenges are completed

### Gamification Elements
- Achievement badges for completing missions
- Point systems to encourage continued learning
- Progress tracking displays

## Sample K-5 Scenario Structure

### Exercise 1: Treasure Hunt Adventure
- Objective: Find a hidden treasure map using basic network commands
- Tools Used: ping, nmap, curl
- Difficulty: Beginner

### Exercise 2: Digital Detective Work
- Objective: Identify different services running on computers
- Tools Used: nmap, web browsing
- Difficulty: Intermediate

## Implementation Best Practices

### Student Experience
1. Keep exercises short (15-30 minutes)
2. Provide clear step-by-step instructions
3. Include helpful hints that appear gradually
4. Ensure all commands work in the virtual environment

### Technical Setup
1. Use lightweight Docker containers (256MB memory limit)
2. All environments should be isolated and secure
3. Validate exercises with `validate-lab.py` before deployment
4. Test on student devices to ensure compatibility

## Troubleshooting Common Issues

### Students Getting Stuck
- Check that hints are properly configured
- Ensure exercises are enabled and visible
- Verify network connectivity in labs

### Technical Problems
- Confirm Docker containers build correctly
- Validate lab.yaml syntax
- Check resource limits on student machines

## Assessment and Progress Tracking

### How to Monitor Students
- Use the Course scoreboard in Admin Panel
- Review student progress through assigned exercises
- Generate PDF reports for individual students or classes

### Success Indicators
- Completion rates of K-5 exercises
- Time spent per exercise
- Achievement badge collection

## Resources and Support

### Teacher Training
- Review the instructor documentation in Manual-Lite
- Check sample exercises in platform/labs/
- Join community forums for additional support

### Student Resources
- K-5 Student Guide (this document)
- Help system built into each exercise
- Teacher support documentation

---

*OpenCyberRange - Educational Cybersecurity Platform*

For questions or support, contact your platform administrator. 📧