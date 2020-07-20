# M0_C4 - Peak Volumes
Repository with prompt and code for Module 1, Challenge 4: Peak Volumes.

## Prompt
As an audio engineer, your job is to mix and master music to generate hit songs for a popular artist. One of the things you have to do is see the peak volume of the mix at any second so you can properly balance it.

Volumes can range from -72 to +10 (inclusive) on a mix, measured in decibels (dB).

- Given a list of numbers representing the song's volume at a given second, write a function that returns a list of the current peak value at each second.
- If the volume falls below -72, set the peak value at that second to "-Inf" and then reset the peak.
- If the volume goes above +10, set the peak value at that second to "CLIP" and then reset the peak.

### Assumptions
- The input to the function will always be a list and nothing else.
- The list will only contain integers, so no error handling is necessary.

## Examples
### Example 1
Let's say we have a 10-second song, with the following volumes at each second:

- 0 → -34
- 1 → -27
- 2 → -32
- 3 → -62
- 4 → -71
- 5 → -45
- 6 → -12
- 7 → -53
- 8 → -16
- 9 → -44

This can be modeled as a list, with each index of the list representing the second in the song:

```
# Input
[-34, -27, -32, -62, -71, -45, -12, -53, -16, -44] # List
   0,   1,   2,   3,   4,   5,   6,   7,   8,   9  # Index

# Output
[-34, -27, -27, -27, -27, -27, -12, -12, -12, -12]
```

In the example above, at index 0, this is our first volume of the song so it is the first "peak" value. However, at index 1, we have a higher level of -27, so that's the new peak starting at that index. For the next several indices, the volumes are all lower than -27, so -27 remains the peak value.

Then, at index 6, we have a new "high" peak of -12. For the rest of the song, -12 is the peak value.

### Example 2
```
# Input
[-23, -26, -73, -32, -65, -59, -19,   2,   6,   0] # List
   0    1    2    3    4    5    6    7    8    9  # Index

# Output
[-23, -23, '-Inf', -32, -32, -32, -19, 2, 6, 6]
```

This example demonstrates something trickier. The first volume is a new peak, per usual, but at index 2, we have a volume falling below -72. Per requirements, we set the value here to `'-Inf'` and then we **reset** the peak counter. So the next value after `'-Inf'` is `-32`, which remains the new peak for a few seconds.

### Example 3
```
# Input
[-5, 200,  -8] # List
  0    1    2  # Index

# Output
[-5, 'CLIP', -8]
```

This 3-second song goes above +10 at index 1 and clips, which resets the peak volume for the second after.

## Instructions
1. Fork this repository to your own account.
2. Clone the forked repository to your local computer.
3. Inside `peak_volumes.py`, you should see a function definition with no content. Write your logic there.
4. While you're writing and/or when you're done, you can execute the provided tests to verify your function works by running `python3 test_peak_volumes.py`. Acceptable is at least 4/6 tests passing. All tests are passing if you see `OK` in the output.
