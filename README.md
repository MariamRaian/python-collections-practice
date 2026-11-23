# Python Collections Practice

Small, runnable Python exercises exploring how lists, nested lists, and dictionaries work. Developed as club assignments and organized here as a single foundations project, rather than presenting each exercise as a complete application.

## What the examples cover

| File | Focus |
| --- | --- |
| `list_operations.py` | Indexing, negative indexing, length, replacement, removal, append, insert, extend, sorting, slicing, and nested-list access |
| `dictionary_operations.py` | Dictionary lookup, updates, adding and removing keys, items/keys/values views, sorted items, clearing, and further list operations |

The examples use fruit, food, contact placeholders, accessory prices, and numbers. They print labeled results so each change can be followed in a terminal.

## Run locally

Requires Python 3. No third-party packages are needed.

```bash
python list_operations.py
python dictionary_operations.py
```

On systems where Python 3 is named `python3`, use that command instead.

## Example results

The list example starts with four fruits and finishes by editing a nested list. The dictionary example demonstrates how a contact dictionary changes, then clears it. Its final number list is:

```text
[1, 2, 3, 'three', 5, 7, 8, 9, 10, 11]
```

## Skills demonstrated

- Choosing between ordered lists and key-value dictionaries
- Reading and updating mutable collections
- Working with zero-based indexes and slices
- Inspecting dictionary keys, values, and items
- Organizing simple exercises into readable, runnable scripts

## Scope and preparation

These are beginner learning exercises, not a contact manager or inventory system. There is no user interface, persistence, or input validation.

The original club work was kept to the same operations. Preparation for this repository fixed formatting and a stray indentation error, translated the Arabic output label, added English explanations and terminal output for notebook expressions, and placed execution behind a `__main__` guard. Contact values were replaced with deliberately non-dialable `PHONE_...` placeholders for privacy. Accessory key capitalization was normalized for readability.
