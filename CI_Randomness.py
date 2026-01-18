import argparse
from tabulate import tabulate
from FrequencyTest import FrequencyTest
from RunTest import RunTest
from Matrix import Matrix
from Spectral import SpectralTest
from TemplateMatching import TemplateMatching
from Universal import Universal
from Complexity import ComplexityTest
from Serial import Serial
from ApproximateEntropy import ApproximateEntropy
from CumulativeSum import CumulativeSums
from RandomExcursions import RandomExcursions


def hex_to_binary(hex_data):
    return bin(int(hex_data, 16))[2:].zfill(len(hex_data) * 4)


def main(data_path):
    # Open Data File and read the hex data with UTF-8 encoding
    with open(data_path, 'r', encoding='utf-8') as file:
        hex_lines = file.readlines()

    # Convert hex data to binary data
    binary_data = ''.join(hex_to_binary(line.strip().replace(' ', '')) for line in hex_lines)

    print('The statistical test of the Binary Expansion of e')
    results = [
        ['2.01. Frequency Test', FrequencyTest.monobit_test(binary_data[:1000000])],
        ['2.02. Block Frequency Test', FrequencyTest.block_frequency(binary_data[:1000000])],
        ['2.03. Run Test', RunTest.run_test(binary_data[:1000000])],
        ['2.04. Run Test (Longest Run of Ones)', RunTest.longest_one_block_test(binary_data[:1000000])],
        ['2.05. Binary Matrix Rank Test', Matrix.binary_matrix_rank_text(binary_data[:1000000])],
        ['2.06. Discrete Fourier Transform (Spectral) Test', SpectralTest.spectral_test(binary_data[:1000000])],
        ['2.07. Non-overlapping Template Matching Test',
         TemplateMatching.non_overlapping_test(binary_data[:1000000], '000000001')],
        ['2.08. Overlapping Template Matching Test', TemplateMatching.overlapping_patterns(binary_data[:1000000])],
        ['2.09. Universal Statistical Test', Universal.statistical_test(binary_data[:1000000])],
        ['2.10. Linear Complexity Test', ComplexityTest.linear_complexity_test(binary_data[:1000000])],
        ['2.11. Serial Test', Serial.serial_test(binary_data[:1000000])],
        ['2.12. Approximate Entropy Test', ApproximateEntropy.approximate_entropy_test(binary_data[:1000000])],
        ['2.13. Cumulative Sums (Forward)', CumulativeSums.cumulative_sums_test(binary_data[:1000000], 0)],
        ['2.13. Cumulative Sums (Backward)', CumulativeSums.cumulative_sums_test(binary_data[:1000000], 1)]
    ]

    print(tabulate(results, headers=['Test', 'Result'], tablefmt='grid'))

    # Random Excursion Tests
    result = RandomExcursions.random_excursions_test(binary_data[:1000000])
    print('2.14. Random Excursion Test:')
    excursion_results = [['STATE', 'xObs', 'P-Value', 'Conclusion']]
    for item in result:
        excursion_results.append([item[0], item[2], item[3], item[4] >= 0.01])
    print(tabulate(excursion_results, headers='firstrow', tablefmt='grid'))

    result = RandomExcursions.variant_test(binary_data[:1000000])
    print('2.15. Random Excursion Variant Test:')
    variant_results = [['STATE', 'COUNTS', 'P-Value', 'Conclusion']]
    for item in result:
        variant_results.append([item[0], item[2], item[3], item[4] >= 0.01])
    print(tabulate(variant_results, headers='firstrow', tablefmt='grid'))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Statistical tests on the binary expansion of e.')
    parser.add_argument('data_path', type=str, help='Path to the hex data file')
    args = parser.parse_args()
    main(args.data_path)