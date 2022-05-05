def countingValleys(steps, path):
    valleys = 0
    seaLevel = 0
    for pat in path:
        if pat == "D" and seaLevel == 0:
            valleys += 1
        if pat == "U":
            seaLevel += 1
        else:
            seaLevel -= 1
    return valleys

if __name__ == "__main__":
    print(countingValleys(12, "UUDDDDUUDDUU"))

