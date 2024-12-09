import sys
from typing import List, Dict

def parse_page_indications(content: str) -> tuple[List[str], List[str]]:
    """
    Parse the input content into rules and update sequences.
    
    Args:
        content (str): The full content of the input file
    
    Returns:
        tuple: A tuple containing rules and update sequences
    """
    rules_text, update_text = content.split('\n\n')
    return rules_text.split('\n'), update_text.split('\n')

def build_page_rules_dict(page_rules: List[str]) -> Dict[int, List[int]]:
    """
    Convert page rules into a dictionary mapping source pages to allowed next pages.
    
    Args:
        page_rules (List[str]): List of page rule strings
    
    Returns:
        Dict[int, List[int]]: Dictionary of page rules
    """
    page_rules_dict = {}
    for page_rule in page_rules:
        if not page_rule.strip():
            continue
        
        page_first, page_after = map(int, page_rule.split('|'))
        page_rules_dict.setdefault(page_first, []).append(page_after)
    
    return page_rules_dict

def validate_page_sequence(page_sequence: List[int], page_rules_dict: Dict[int, List[int]]) -> bool:
    """
    Check if a page sequence follows the given page rules.
    
    Args:
        page_sequence (List[int]): Sequence of pages to validate
        page_rules_dict (Dict[int, List[int]]): Dictionary of allowed page transitions
    
    Returns:
        bool: True if the sequence follows all page rules, False otherwise
    """
    for i in range(len(page_sequence) - 1):
        current_page = page_sequence[i]
        
        # Skip if current page has no defined rules
        if current_page not in page_rules_dict:
            return False
        
        # Check if all subsequent pages are valid according to current page's rules
        allowed_next_pages = page_rules_dict[current_page]
        for j in range(i + 1, len(page_sequence)):
            if page_sequence[j] not in allowed_next_pages:
                return False
    
    return True

def separate_rulless_from_rulefull(page_sequence: List[int], page_rules_dict: Dict[int, List[int]]) -> tuple[List[int], List[int]]:
    """
    Separate the pages into 2 lists, one with the rulless pages and one with the rulefull pages.

    Args:
        page_sequence (List[int]): List of the invalid page order.
        page_rules_dict (Dict[int, List[int]): Dictionary of page rules.
    
    Returns:
        tuple[List[int], List[int]]: rulless elements, rulefull elements
    """
    ruleless = []
    rulefull = []
    for page in page_sequence:
        if page not in page_rules_dict:
            ruleless.append(page)
        else:
            rulefull.append(page)
    return (ruleless, rulefull)

def sort_based_on_rule(rulefull_sequence: List[int], page_rules_dict: Dict[int, List[int]]) -> None:
    """
    Takes in a rulefull unsorted sequence and sorts it based on page_rules_dict.

    Args:
        page_sequence (List[int]): List of the rulefull page sequence.
        page_rules_dict (Dict[int, List[int]): Dictionary of page rules.

    Returns:
        None
    """
    while True:
        swaped = False
        for i in range(len(rulefull_sequence) - 1):
            if rulefull_sequence[i] in page_rules_dict[rulefull_sequence[i + 1]]:
                rulefull_sequence[i], rulefull_sequence[i + 1] = rulefull_sequence[i + 1], rulefull_sequence[i]
                swaped = True
        if swaped == False:
            return

def refactor_into_valid_sequence(page_sequence: List[int], page_rules_dict: Dict[int, List[int]]) -> List[int]:
    """
    Reorder the positions of the invalid page sequences into a valid one and return it.

    Args:
        page_sequence (List[int]): List of the invalid page order.
        page_rules_dict (Dict[int, List[int]): Dictionary of page rules.
    
    Returns:
        List[int]: Reordered into a valid page sequence.
    """
    # Get the elements that don't have a rule
    ruleless_elements, rulefull_elements = separate_rulless_from_rulefull(page_sequence, page_rules_dict)
    
    # Sort the rulefull_elements based on the page rules
    sort_based_on_rule(rulefull_elements, page_rules_dict)

    # Add the ruleless elements at the end as they are last in order that doesn't matter
    rulefull_elements.extend(ruleless_elements)

    # return the valid sequence
    return rulefull_elements

def calculate_middle_pages_sum(page_update_sequences: List[str], page_rules_dict: Dict[int, List[int]]) -> int:
    """
    Calculate the sum of middle pages from invalid page sequences after they are validated.
    
    Args:
        page_update_sequences (List[str]): List of page update sequences
        page_rules_dict (Dict[int, List[int]]): Dictionary of page rules
    
    Returns:
        int: Sum of middle pages from valid sequences
    """
    total_sum = 0
    
    for update_sequence in page_update_sequences:
        if not update_sequence.strip():
            continue
        
        # Convert sequence to integers
        page_sequence = list(map(int, update_sequence.split(',')))
        
        # If sequence is valid, add middle page to sum
        if not validate_page_sequence(page_sequence, page_rules_dict):
            page_sequence = refactor_into_valid_sequence(page_sequence, page_rules_dict)
            middle_index = len(page_sequence) // 2
            total_sum += page_sequence[middle_index]
    
    return total_sum

def main():
    """
    Main function to process page rules and calculate middle pages sum of the invalid pages after refactoring into valid ones.
    """
    # Read input file
    with open(sys.argv[1], 'r') as file:
        content = file.read()
    
    # Parse input
    page_rules, page_update_sequences = parse_page_indications(content)
    
    # Build page rules dictionary
    page_rules_dict = build_page_rules_dict(page_rules)
    
    # Calculate and print sum of middle pages
    result = calculate_middle_pages_sum(page_update_sequences, page_rules_dict)
    print(result)

if __name__ == "__main__":
    main()