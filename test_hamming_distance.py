# example input 1: strand1 = "GAGCCTACTAACGGGAT" 
# strand2 = "CATCGTAATGACGGCCT"	
# expected output 1: 7

# example input 2:strand1 = "GAG" strand2 = "GAG"
# expected output 2: 0
from hamming_distance import hamming_distance
import pytest
def test_different_strands_case():
    # arrange
    strand1 = "GAGCCTACTAACGGGAT"
    strand2 = "CATCGTAATGACGGCCT"
    # act
    distance = hamming_distance(strand1, strand2)
    # assert
    assert distance == 7
def test_same_strands_case():
    # arrange
    strand1 = "GAGCCTACTAACGGGAT"
    strand2 = "GAGCCTACTAACGGGAT"
    # act
    distance = hamming_distance(strand1, strand2)
    # assert
    assert distance == 0

def test_one_empty_strand():
    # Arrange
    strand1 = "GAG"
    strand2 = ""

    # act/assert
    with pytest.raises(ValueError):
        hamming_distance(strand1, strand2)

def test_space_deletion_case():
    # arrange
    strand1 = "GAGCCT CTAACGGGAT"
    strand2 = "GAGCCTACTAACGGGAT"
    # act
    distance = hamming_distance(strand1, strand2)
    # assert
    assert distance == 1

def test_different_length_case():
    # arrange
    strand1 = "GAGCCTACTAACGGGATTTT"
    strand2 = "GAGCCTACTAACGGGAT"
    # act/assert
    with pytest.raises(ValueError):
        hamming_distance(strand1, strand2)

def test_wrong_letter_case():
    # arrange
    strand1 = "ABC"
    strand2 = "GAG"
    # act/assert
    with pytest.raises(ValueError):
        hamming_distance(strand1, strand2)

def test_case_insensitive():
    # arrange
    strand1 = "GAGCCTACTAACGGGAT"
    strand2 = "gagCCTACTAACGGGAT"
    # act
    distance = hamming_distance(strand1, strand2)
    # assert
    assert distance == 0

def test_non_nucleotide_char_case():
    # arrange
    strand1 = "A-+!$%"
    strand2 = "GAGGAG"
    # act/assert
    with pytest.raises(ValueError):
        hamming_distance(strand1, strand2)

def test_same_lengths_strands_case():
    # arrange
    strand1 = "GAG"
    strand2 = "GAG"
    # act
    distance = hamming_distance(strand1, strand2)
    # assert
    assert len(strand1) == 3
    assert len(strand2) == 3

def test_different_strands_case():
    # arrange
    strand1 = "ACGTACGT"
    strand2 = "TGCATGCA"
    # act
    distance = hamming_distance(strand1, strand2)
    # assert
    assert distance == 8