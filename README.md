
```markdown
# University Progression Prediction Program

This Python program predicts progression outcomes for students based on the University regulations. The program allows users to input credits at pass, defer, and fail levels and displays the corresponding progression outcome.

## Part 1 - Main Version

### Outcomes

1. The program prompts for credit inputs and displays the progression outcome.
2. Validation:
   - Handles incorrect data types.
   - Validates credit inputs within the specified range.
   - Checks for the correct total of pass, defer, and fail credits.

### Example Usage

```python
Please enter your credits at pass: p
Integer required 
Please enter your credits at pass: 140
Out of range.
Please enter your credits at pass: 100
Please enter your credit at defer: 40
Please enter your credit at fail: 20
Total incorrect.
Please enter your credits at pass: 100
Please enter your credit at defer: 20
Please enter your credit at fail: 0
Progress (module trailer)
```

3. Multiple Outcomes & Histogram:
   - Allows staff members to predict outcomes for multiple students.
   - Displays a histogram of progression outcomes.

### Staff Version with Histogram

```python
Enter your total PASS credits: 120
Enter your total DEFER credits: 0
Enter your total FAIL credits: 0
Progress
Would you like to enter another set of data?
Enter 'y' for yes or 'q' to quit and view results: y
...
```

## Part 2 - Vertical Histogram (Extension)

The program is extended to include a vertical histogram, displaying stars downwards for each category.

## Part 3 - List/Tuple/Directory (Extension)

The program uses Python to save input progression data to a list, tuple, or directory. It then accesses and prints the stored data.

### Example Output

```python
Progress - 120, 0, 0
Progress (module trailer) - 100, 0, 20
Module retriever - 80, 20, 20
Module retriever - 60, 0, 60
Exclude – 40, 0, 80
```

## Part 4 - Text File

The program saves input progression data to a text file and later accesses and prints the data.

### Example Output (with data from text file)

```python
Progress - 120, 0, 0
Progress (module trailer) - 100, 0, 20
Module retriever - 80, 20, 20
Module retriever - 60, 0, 60
Exclude – 40, 0, 80
```

