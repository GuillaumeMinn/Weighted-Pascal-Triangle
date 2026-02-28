Weighted Pascal Triangle
------------------------

This code is a variation of Pascal’s triangle using a simple adjustable weight factor.

The program asks the user for two values:
• The number of rows to generate
• A weight factor

It then builds a triangle where each number is formed from the two numbers above it, but with a twist - one of those values is multiplied by the chosen weight.

After generating the triangle, the program:
• Prints the full structure
• Calculates the sum of each row
• Verifies a pattern that emerges from the construction

The interesting part is that the total of the final row always follows a predictable rule based on the weight factor and the number of rows. When the weight is set to 1, the triangle behaves exactly like the classical Pascal triangle. Changing the weight produces a new structured pattern that still follows a consistent growth rule.

This makes the program a compact demonstration of how small rule changes can generate structured mathematical behaviour.

What it demonstrates:
• Algorithmic construction of structured number systems
• Pattern emergence from simple recurrence rules

How to run:
1. Open the file in any Python environment.
2. Run the script.
3. Enter the number of rows and the weight factor when prompted.
No external libraries are required.

License
-------

Distributed under the GNU General Public License v3.0.
See LICENSE.txt for details.