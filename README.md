# CIT Contest Solutions

Python solutions and problem statements for the **CIT's CONTEST** on HackerRank.
The story: in 2026 THE CRASH hit the CIT Network, and you play an Operator who must
restore THE CORE by solving a series of problems.

## Repository Structure

Each problem has its own folder with two files:

```
CIT's CONTEST/
|-- Problem A - Telemetry Noise Filter/
|   |-- description.txt
|   |-- solution.py
|-- Problem B - Gateway Handshake/
|   |-- description.txt
|   |-- solution.py
|-- ...
```

- `description.txt`: the full problem statement (input, output, samples).
- `solution.py`: the Python 3 solution, ready to paste into HackerRank.

## Problems

| # | Problem | Main idea | Complexity |
|---|---------|-----------|------------|
| A | Telemetry Noise Filter | Keep only values >= 0, same order | O(n) |
| B | Gateway Handshake | Find the pair i < j with a[i] + a[j] = T (smallest i, then smallest j) using a dictionary of positions | O(n) |
| C | Datawyin's Ramadan League Exploit | Count the "AC" tokens and check that no "AC" touches an error token | O(m) |
| D | Firewall Packet Reordering | Sliding window with at most k negative numbers | O(n) |
| E | Reversing the Crash Logs | A reversed log contains "citlogin" originally if it contains "nigoltic" | O(total length) |
| F | Core Reactor Power Balance | Binary search on the answer + greedy check of the number of groups | O(n log(sum)) |
| G | Mirror Status Protocol | Count fragments in a dictionary, pair each word with its reverse, then choose the status code by priority | O(total length) |

## Short Explanations

**A - Telemetry Noise Filter**
Loop over the list and keep the numbers that are not negative. Print the count, then the numbers.

**B - Gateway Handshake**
For each index i, look for the value T - a[i] at a later index j. The first i that works,
with its smallest j, is the answer. Print -1 -1 if there is none.

**C - Datawyin's Ramadan League Exploit**
The log is FRAUDULENT if there are more "AC" than n, or if an "AC" is directly next to
"WA", "TLE" or "RTE". Otherwise it is GENUINE.

**D - Firewall Packet Reordering**
Keep a window [left, right] and count the negative numbers inside it. If the count goes
above k, move left forward. The answer is the biggest window seen.

**E - Reversing the Crash Logs**
No need to reverse every string. Reversing "citlogin" gives "nigoltic", so we only count
the strings that contain "nigoltic".

**F - Core Reactor Power Balance**
The answer is between max(numbers) and sum(numbers). For a guess "limit", fill groups
greedily. If we need at most k groups, the guess is big enough, so we try smaller.
Otherwise we try bigger.

**G - Mirror Status Protocol**
A mirror pair is two fragments where one is the reverse of the other. A palindrome can
only pair with an identical one. The status code is chosen in this order:
500 (malformed input), 412 (an unpaired palindrome), 404 (no pairs),
200 (everything paired), 202 (some fragments unpaired).