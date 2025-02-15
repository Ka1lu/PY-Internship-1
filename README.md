# Username Generator

This Python program generates random usernames based on user-defined constraints. It uses an external CSV file (`words.csv`) containing adjectives and nouns, allowing users to modify word lists without altering the code.

## Features
- Uses an external CSV file for easy customization.
- Allows users to specify username length constraints.
- Supports six different username structures.
- Saves generated usernames to `usernames.txt`.

## Requirements
- Python 3
- `pandas` library

## Installation
1. Install Python if not already installed.
2. Install the required library:
   ```sh
   pip install pandas
   ```
3. Ensure `words.csv` exists with the following structure:
   ```csv
   adjective,noun
   Cool,Tiger
   Fast,Car
   Brave,Warrior
   ```

## Usage
Run the script and follow the prompts:
```sh
python Main.py
```
1. Enter the maximum and minimum character limit for usernames.
2. Input a custom special character sequence.
3. Choose a username structure:
   - 1: NOUN + ADJECTIVE + SPECIAL CHARACTER
   - 2: NOUN + SPECIAL CHARACTER + ADJECTIVE
   - 3: ADJECTIVE + NOUN + SPECIAL CHARACTER
   - 4: ADJECTIVE + SPECIAL CHARACTER + NOUN
   - 5: SPECIAL CHARACTER + NOUN + ADJECTIVE
   - 6: SPECIAL CHARACTER + ADJECTIVE + NOUN
4. Specify how many usernames to generate.
5. Generated usernames are displayed and saved in `usernames.txt`.

## Example Output
```
Generated Username: TigerCool!
Generated Username: CarFast@
Generated Username: WarriorBrave#
```

## License
This project is open-source and available under the MIT License.
