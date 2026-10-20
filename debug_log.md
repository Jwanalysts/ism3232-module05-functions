# Debug Log
Author: Jackson Williams

## Bug 1
**Error type:** KeyError

**File + line:** week8_buggy.py, line 12

**What the error means:** Python tried to access a dictionary key that did not exist.

**What I told the duck:** The function loops through each record and adds its amount to the total. One record had a misspelled key.

**What I tried:** I added a DEBUG print statement to inspect the records and ran the program again.

**How I fixed it:** I changed 'amout' to 'amount' in the first record and removed the DEBUG statement.

## Bug 2
**Error type:** TypeError

**File + line:** week8_buggy.py, line 16

**What the error means:** Python cannot compare an integer with a string using >.

**How I fixed it:** I removed the quotation marks around '1000' so Python treated it as an integer.

## After Fixing Both Bugs
**Final output:**

Total: $5150.00 across 3 records

True

**Did pytest pass?** Yes, all 13 tests passed.

## AI Literacy Reflection
**Did I use AI?** Yes.

**Exact prompt I used:** "is there a way to type fixerror"

**What AI explained:** AI explained how to read Python errors, identify indentation problems, and use Ruff to check code. It also explained that Ruff cannot automatically repair every syntax error.

**What I changed myself:** I corrected the dictionary key, fixed the integer comparison, and corrected indentation errors in my test file with guidance.

**Can I explain every fixed line?** Yes, after reviewing the code and understanding the errors.

## What I Learned
I learned how to read Python tracebacks from the bottom up and use DEBUG statements to find errors. I also learned that indentation matters in Python and that running pytest helps verify that code works correctly.