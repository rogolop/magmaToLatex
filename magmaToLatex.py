#!/usr/bin/env python3

# Format Magma polynomials as LaTeX
#
# Example usage:
# ./magmaToLatex.py <testIn.txt >testOut.txt; less testOut.txt

import re, sys
theString = sys.stdin.read()

# Remove newlines inside polynomials
theString = re.sub(r"\\\n[ \t]*", "", theString)
theString = re.sub(r"\+[ \t]*\n[ \t]*", "+ ", theString)
theString = re.sub(r"[ \t]*\n[ \t]*\+", " +", theString)
theString = re.sub(r"(?<!\-)\-[ \t]*\n[ \t]*", "- ", theString)
theString = re.sub(r"[ \t]*\n[ \t]*\-(?!\-)", " -", theString)
# Remove product signs
theString = theString.replace("*", " ")
# A_12_34 -> A_{12,34}
theString = re.sub(r"([a-zA-Z])\_(\d+)\_(\d+)[ ]*", r"\1_{\2,\3}", theString)
# t1 -> t_1
theString = re.sub(r"([a-zA-Z])(\d)(?!\d)[ ]*", r"\1_\2", theString)
# t12 -> t_{12}
theString = re.sub(r"([a-zA-Z])(\d\d+)[ ]*", r"\1_{\2}", theString)
# No space before exponentiation"
theString = re.sub(r"[ ]*\^", r"^", theString)
# ^12 -> ^{12}
theString = re.sub(r"\^(\d\d+)", r"^{\1}", theString)
# No space after exponent
theString = re.sub(r"(\^[\{\}\d]+)[ ]*", r"\1", theString)
# Space after number before monomial
theString = re.sub(r"(\d) ([a-zA-Z])", r"\1\,\2", theString)
# space after monomial
theString = re.sub(r"([a-zA-Z0-9\}])([+-]) ", r"\1 \2 ", theString)
# Number fractions
theString = re.sub(r"(\d+)\/(\d+)", r"\\tfrac{\1}{\2}", theString)

print(theString)

