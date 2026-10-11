# business_rules.py
# Author: Jackson

APPROVAL_LIMIT = 1000


def calculate_total(price: float, quantity: int) -> float:
    """Return total cost including 7% tax."""
    return price * quantity * 1.07


def requires_review(amount: float) -> bool:
    """Return True if amount exceeds the approval limit."""
    return amount > APPROVAL_LIMIT


def get_approval_tier(amount: float) -> str:
    """Return the approval routing tier."""
    if amount <= 500:
        return "auto"
    elif amount <= 2000:
        return "manager"
    else:
        return "director"


def apply_discount(price: float, pct: float) -> float:
    """Return price after discount. pct is 0-100."""
    return price * (1 - pct / 100)


def test_total_includes_tax():
    assert round(calculate_total(100.00, 2), 2) == 214.00


def test_requires_review_over():
    assert requires_review(1500) is True


def test_requires_review_under():
    assert requires_review(500) is False


def test_boundary_at_limit():
    assert requires_review(1000) is False


def test_tier_auto():
    assert get_approval_tier(400) == "auto"


def test_tier_boundary_500():
    assert get_approval_tier(500) == "auto"


def test_tier_manager():
    assert get_approval_tier(1500) == "manager"


def test_discount_ten():
    assert apply_discount(100.00, 10) == 90.0
