def permutation(s1: str, s2: str) -> bool:
    
    if len(s1) > len(s2):
        return False
    
    l, r = 0, len(s2) - 1
    
    return True