def nextGreater(A):
    a_len = len(A)
    output = []
    for ind, number in enumerate(A):
        j = ind+1
        found_greater_val = False
        while j < a_len:
            if A[j] > number:
                output.append(A[j])
                found_greater_val = True
                break
            j += 1
        if not found_greater_val:
            output.append(-1)

    #output.append(-1)
    return output

print nextGreater([3, 2, 1])
