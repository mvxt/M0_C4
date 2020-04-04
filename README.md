# M0_C4 - Max Volume
Repository with prompt and code for Module 1, Challenge 4: Max Volume.

## Prompt
As an audio engineer, your job is to mix and master music to generate hit songs for a popular artist. One of the things you have to do is find the maximum volume of the mix so you can properly balance it.

Volumes can range from -72 to +10 (inclusive) on a mix, measured in decibels (dB). Anything outside of that range is invalid.

- Given a list of numbers representing the song's volume at a given second, write a function that returns the loudest second in the song.
- But if the volume ever falls outside of [-72, +10] at any point, return "Invalid" as the output.
- If there are multiple "loudest" places in the song, return the earliest one.

### Assumptions
- The input to the function will always be a list and nothing else.
- Aside from invalid values, the list will always contain integers and nothing else.

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

**Input:**
```
List:  [-34, -27, -32, -62, -71, -45, -12, -53, -16, -44]
#Index:   0,   1,   2,   3,   4,   5,   6,   7,   8,   9
```

As you can see, the song above reaches a maximum volume of -12 dB, and this occurs at index 6, or the 6th second. Therefore, your function would return `6` as the output for this scenario.

**Output:**
```
6
```

### Example 2
**Input:**
```
List:  [-23, -26, -73, -32, -65, -59, -19, 2, 6, 0]
```

As you can see, the song above reaches a maximum volume of 6 dB. But, on index 2, we have a volume of -73 dB. Since this falls outside the acceptable range, this song is invalid. Return "Invalid".

**Output:**
```
Invalid
```

### Example 3
**Input:**
```
List:  [-5, -5, -5]
```

This 3-second song stays the same volume throughout. Therefore we return the earliest second, 0.

**Output:**
```
0
```

## Instructions
1. Fork this repository to your own account.
2. Clone the forked repository to your local computer.
3. Inside `loudest_second.py`, you should see a function definition with no content. Write your logic there.
4. While you're writing and/or when you're done, you can execute the provided tests to verify your function works by running `python3 test_loudest_second.py`. Acceptable is at least 4/6 tests passing. All tests are passing if you see `OK` in the output.
