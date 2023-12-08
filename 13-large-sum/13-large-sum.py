with open("numbers.txt") as f:
    Σ = 0
    for line in f:
        Σ += int(line.strip())

print(str(Σ)[:10])
