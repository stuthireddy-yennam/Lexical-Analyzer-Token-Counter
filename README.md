# Lexical Analyzer and Token Counter

## 1. Title
Implementation of an Automated Source-Code Lexical Analyzer and Token Counter.

## 2. Objective
To design and build a utility program that parses structural source file data to isolate, sequence, and classify fundamental programming primitives into specific structural classes.

## 3. Problem Statement
Write a script that reads an input file filled with target program statements to dynamically log and count:
- Keywords
- Identifiers
- Operators
- Constants
- Special Symbols
- Preprocessor Elements

## 4. Algorithm
1. Read the input character payload stream from `input.txt`.
2. Apply regex block sequences matching target C primitives sequentially line-by-line.
3. For each valid match, check against internal dictionary lookups to check if the value is a specific reserved syntax word.
4. Categorize valid elements, append them to a global token tracker log, and increment class counters.
5. Print out structured matrix profiles onto standard execution logs.

## 5. Source Code
*(Refer to `lexical_analyzer.py` inside the root repository framework)*

## 6. Sample Input
*(Refer to local system validation file `input.txt`)*

## 7. Sample Output
*(Refer to local system execution receipt log `output.txt`)*

## 8. Token Classification
Categorized boundaries follow rigid ANSI C validation requirements targeting keywords, symbol elements, mathematical punctuation operators, literal bounds, and text constants.

## 9. Test Cases
The system reads a raw standard C entry code block defining variable allocations, inline mathematics, and simple standard library stream text calls.

## 10. Conclusion
This environment effectively breaks down string text streams into standard component syntax fragments, establishing clear tracking over overall program structural compositions.
