from utils import num_digits

done = False
Σ = 0
for n in range(1, 100):
    for b in range(9):
        bn = num_digits((9 - b) ** n)
        if bn == n:
            # print(f"{9 - b}^{n} = {(9 - b) ** n} has {bn} digits")
            Σ += 1
        if b == 0 and bn < n:
            done = True
            break
    if done:
        break

# 9^21 is the last n-digit number that is also an n-th power.
# There is no n > 21, such that b^n has n digits (for any b).
#
# Proof. (Induction)
# We can check that for all b = 1, 2, ..., 9, b^22 has less than 22 digits. (Base Case)
# Also, for any n in N and for all b = 1, 2, ..., 9
# b^n has less than d digits => b^(n+1) = b*b^n has less than d + 1 digits. (Induction Step)
# Thus, for any n > 21, b = 1, 2, ..., 9, there is no b^n with at least n digits
#
# If b > 9, then b^n will always have more than n digits (trivial).
# Therefore, there is no n > 21 such that b^n has n digits (for any b).

print(Σ)
