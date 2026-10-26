# K-5 Scenario Template for OpenCyberRange

## Scenario Overview

**Name:** [Insert Name Here]
**Track:** K-5 Cyber Adventures
**Level:** [1-9]
**Difficulty:** Beginner/Intermediate/Advanced

### Learning Objectives

- [ ] Objective 1
- [ ] Objective 2
- [ ] Objective 3

### Scenario Description

[Describe the adventure in simple terms that young learners can understand. Use storytelling elements and clear, age-appropriate language.]

### Flag Format

```
OCR{your_flag_here}
```

## Exercise Structure

### lab.yaml

```yaml
name: "[Scenario Name]"
description: "[Brief description suitable for students]"
difficulty: beginner
category: general
duration_minutes: 20
scenario: |
  [Detailed scenario narrative in simple language]

flag: "OCR{your_flag_here}"

objectives:
  - [Learning objective 1]
  - [Learning objective 2]
  - [Learning objective 3]

hints:
  - text: |
      [Hint 1 - immediately available]
    unlock_after_minutes: 0
  - text: |
      [Hint 2 - available after 5 minutes]
    unlock_after_minutes: 5
  - text: |
      [Hint 3 - available after 10 minutes]
    unlock_after_minutes: 10

test:
  steps:
    - name: "[Test step 1]"
      command: "[Command to verify student action]"
      expect: "[Expected result]"
    - name: "[Test step 2]"
      command: "[Another verification command]"
      expect: "[Expected result]"

workbook: "wiki/range/k5/CH01_[Scenario_Name]/"
```

### docker-compose.yml

```yaml
services:
  target:
    mem_limit: 256m
    cpus: 0.3
    build:
      context: ./containers/target
      dockerfile: Dockerfile
    hostname: [target-name]
    labels:
      ip_offset: "10"
    restart: unless-stopped
```

### containers/target/Dockerfile

```dockerfile
FROM alpine:latest

# Install required tools
RUN apk add --no-cache nginx curl

# Create scenario content
RUN mkdir -p /var/www/html/scenario \
    && echo "OCR{your_flag_here}" > /var/www/html/scenario/flag.txt

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```

### README.md

```markdown
# [Scenario Name]

## Learning Objectives

[Clear list of what students will learn]

## Adventure Story

[Engaging narrative that frames the learning challenge]

## Solution Walkthrough

### Step 1: [Action]

[Simple, clear instruction]

### Step 2: [Action]

[Simple, clear instruction]

## What You Learned

[Brief summary of concepts learned]

## Success!

[Encouraging message for student completion]
```

## Implementation Checklist

- [ ] Scenario name and description created
- [ ] Lab.yaml file completed with proper flag format
- [ ] Dockerfile created with appropriate container configuration
- [ ] README.md written with clear instructions
- [ ] Test steps defined to validate student actions
- [ ] Hints provided for different time intervals
- [ ] Exercise assigned to K-5 track and level
- [ ] Validated with `validate-lab.py`
- [ ] Enabled and made visible to students

## Engagement Tips

1. **Storytelling**: Frame each exercise as an adventure or mystery
2. **Visual Elements**: Include clear screenshots in README.md when possible
3. **Progression**: Build complexity gradually through levels
4. **Feedback**: Provide immediate success confirmation
5. **Relevance**: Connect concepts to real-world digital experiences students encounter

## Sample Flag Formats for K-5

- OCR{treasure_map}
- OCR{secret_code}
- OCR{digital_key}
- OCR{explorer_name}
- OCR{safe_combination}

---

*Template created for OpenCyberRange K-5 Cyber Adventures*