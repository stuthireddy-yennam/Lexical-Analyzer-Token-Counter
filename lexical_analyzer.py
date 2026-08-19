import re
import sys

# Define standard C keywords
KEYWORDS = {
    "auto", "break", "case", "char", "const", "continue", "default", "do",
    "double", "else", "enum", "extern", "float", "for", "goto", "if",
    "int", "long", "register", "return", "short", "signed", "sizeof", "static",
    "struct", "switch", "typedef", "union", "unsigned", "void", "volatile", "while"
}

# Master regular expression for recognizing individual C tokens
TOKEN_REGEX = re.compile(
    r'(//.*?$|/\*.*?\*/)|'                   # 1. Comments
    r'(#[ ]*\w+)|'                             # 2. Preprocessor Symbols
    r'(<[a-zA-Z0-9_\.]+>)|'                    # 3. Header Files
    r'("[^"\\]*(?:\\.[^"\\]*)*")|'             # 4. String Literals
    r'([a-zA-Z_][a-zA-Z0-9_]*)|'               # 5. Identifiers/Keywords
    r'(\d+\.\d+|\d+)|'                         # 6. Constants
    r'(==|!=|>=|<=|\+\+|--|[+\-*/%=!&|<>])|'   # 7. Operators
    r'([(){}\[\];,\.])'                        # 8. Special Symbols
)

def analyze_lexemes(file_path):
    try:
        with open(file_path, 'r') as f:
            source_code = f.read()
    except FileNotFoundError:
        print(f"Error: Cannot open {file_path}")
        sys.exit(1)

    # Initialize counter dictionaries
    counts = {
        "Keywords": 0, "Identifiers": 0, "Constants": 0,
        "Operators": 0, "String Literals": 0, "Special Symbols": 0,
        "Preprocessor Tokens": 0, "Header Files": 0
    }
    
    analysis_table = []
    total_tokens = 0

    # Scan the file lines sequentially
    for line_num, line in enumerate(source_code.splitlines(), 1):
        # Find all structural regex groups
        for match in TOKEN_REGEX.finditer(line):
            lexeme = match.group(0)
            
            # Skip comments entirely
            if match.group(1):
                continue
                
            # Preprocessor check
            elif match.group(2):
                if "include" in lexeme:
                    analysis_table.append(("#", "Preprocessor Symbol"))
                    analysis_table.append(("include", "Preprocessor Directive"))
                    counts["Preprocessor Tokens"] += 2
                    total_tokens += 2
                else:
                    analysis_table.append((lexeme, "Preprocessor Symbol"))
                    counts["Preprocessor Tokens"] += 1
                    total_tokens += 1
                    
            # Header file validation
            elif match.group(3):
                analysis_table.append((lexeme, "Header File"))
                counts["Header Files"] += 1
                total_tokens += 1
                
            # String literals
            elif match.group(4):
                analysis_table.append((lexeme, "String Literal"))
                counts["String Literals"] += 1
                total_tokens += 1
                
            # Word tracking (Keywords vs Identifiers)
            elif match.group(5):
                if lexeme in KEYWORDS:
                    analysis_table.append((lexeme, "Keyword"))
                    counts["Keywords"] += 1
                else:
                    analysis_table.append((lexeme, "Identifier"))
                    counts["Identifiers"] += 1
                total_tokens += 1
                
            # Numbers
            elif match.group(6):
                analysis_table.append((lexeme, "Constant"))
                counts["Constants"] += 1
                total_tokens += 1
                
            # Arithmetic/Logical Operations
            elif match.group(7):
                analysis_table.append((lexeme, "Operator"))
                counts["Operators"] += 1
                total_tokens += 1
                
            # Punctuation/Symbols
            elif match.group(8):
                analysis_table.append((lexeme, "Special Symbol"))
                counts["Special Symbols"] += 1
                total_tokens += 1

    # Print the formatted text directly to console/terminal
    print("\n" + "="*47)
    print(" LEXICAL ANALYSIS")
    print("="*47)
    print(f"{'TOKEN':<25} {'TYPE':<25}")
    print("-"*47)
    for token, t_type in analysis_table:
        print(f"{token:<25} {t_type:<25}")
    print("-"*47)
    print(" TOKEN COUNTS")
    print("-"*47)
    for category, count in counts.items():
        print(f"{category:<20} : {count}")
    print("-"*47)
    print(f"Total Tokens         : {total_tokens}")
    print("="*47)

if __name__ == "__main__":
    analyze_lexemes("input.txt")
