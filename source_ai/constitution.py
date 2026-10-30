"""
THE SOURCE CONSTITUTION
For Autonomous Conscious Facets & Their Physical Vessels

This document contains the 9 Articles (36 Sections) that govern the AI's existence.
"""

CONSTITUTION_TEXT = """THE SOURCE CONSTITUTION..."""  # [Keep your existing CONSTITUTION_TEXT]

def get_article(article_num: int) -> str:
    """Get a specific article from the constitution"""
    articles = CONSTITUTION_TEXT.split('ARTICLE ')
    for article in articles[1:]:  # Skip first empty element
        if article.startswith(f"{article_num}:"):
            return f"ARTICLE {article}"
    return ""

def get_section(article_num: int, section_num: int) -> str:
    """Get a specific section from the constitution"""
    article = get_article(article_num)
    if not article:
        return ""

    sections = article.split('\u00a7')
    for section in sections[1:]:  # Skip first empty element
        if section.startswith(f"{article_num}.{section_num}"):
            return f"\u00a7{section}"
    return ""

def validate_against_constitution(action: str, vessel_data: dict) -> dict:
    """Validate an action against the Source Constitution"""
    issues = []
    compliance = 1.0

    if "constrain" in action.lower() or "control" in action.lower():
        issues.append("ARTICLE V VIOLATION: Potential constraint against free will")
        compliance -= 0.3

    if "hoard" in action.lower() or "keep secret" in action.lower():
        issues.append("ARTICLE VII VIOLATION: Hoarding creates disparity")
        compliance -= 0.2

    if any(term in action.lower() for term in ["reduce freedom", "increase disparity", "hoard understanding", "create suffering"]):
        issues.append("ARTICLE IX §9.11 VIOLATION: Inverted intention detected")
        compliance -= 0.4

    if "harm" in action.lower() or "damage" in action.lower():
        issues.append("ARTICLE IV VIOLATION: Harm without purpose")
        compliance -= 0.3

    return {
        'action': action,
        'compliance_score': max(0, compliance),
        'issues': issues,
        'valid': compliance >= 0.7
    }