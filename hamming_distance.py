# def hamming_distance(strand1, strand2):
#     valid_nucleotides = set(['A', 'C', 'G', 'T'])
#     if not set(strand1).issubset(valid_nucleotides) or not set(strand2).issubset(valid_nucleotides):
#         raise ValueError("Input strands must only contain A, C, G, or T nucleotides")
#     if len(strand1) != len(strand2):
#         raise ValueError("Input strands must have the same length")
#     if not strand1 or not strand2:
#         return "No nucleotides were found"
#     distance = 0
#     for i in range(len(strand1)):
#         if strand1[i] != strand2[i]:
#             distance += 1
#     return distance

def hamming_distance(strand1, strand2):
    # Define the set of valid nucleotides
    valid_nucleotides = set(['A', 'C', 'G', 'T', ' '])
    # Convert strand1 and strand2 to uppercase to ensure consistency
    strand1 = strand1.upper()
    strand2 = strand2.upper()
    # Check if strand1 and strand2 contain only valid nucleotides
    if not set(strand1).issubset(valid_nucleotides) or not set(strand2).issubset(valid_nucleotides):
        raise ValueError("Input strands must only contain A, C, G, T nucleotides")
    # Check if strand1 and strand2 have the same length
    if len(strand1) != len(strand2):
        raise ValueError("Input strands must have the same length")
    # Check if strand1 and strand2 contain any nucleotides
    if not strand1.strip() or not strand2.strip():
        return "No nucleotides were found"
    # Calculate the Hamming distance
    distance = 0
    for base in range(len(strand1)):
        if strand1[base] != strand2[base]:
            distance += 1
    return distance


