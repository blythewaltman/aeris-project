import os
import csv
import math

def find_concentration_index(lst):
    try:
        index = lst.index('concentration')
        return index
    except ValueError:
        return -1  # 'concentration' is not found in the list


def get_mean(filename):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    csv_file_path = os.path.join(current_directory, filename)

    try:
        with open(csv_file_path, 'r') as file:
            csv_reader = csv.reader(file)

            # ignore ['z', 'y', 'x', 'concentration'] row
            header = next(csv_reader)
            concentrationIndex = find_concentration_index(header)

            # variables for sum and count
            sum_concentration = 0
            count = 0

            # iterate through the rows and calculate the sum and count
            for row in csv_reader:
                concentration = float(row[concentrationIndex])
                sum_concentration += concentration
                count += 1

        # calculate the mean
        mean_concentration = sum_concentration / float(count)
        return mean_concentration

    except FileNotFoundError:
        return "File not found"

    except (ValueError, IndexError):
        return "Invalid data format in the CSV file"

    except Exception as e:
        return f"An error occurred: {str(e)}"
    

def get_std_deviation_pop(filename):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    csv_file_path = os.path.join(current_directory, filename)

    try:
        with open(csv_file_path, 'r') as file:
            csv_reader = csv.reader(file)

            # ignore ['z', 'y', 'x', 'concentration'] row
            header = next(csv_reader)
            concentrationIndex = find_concentration_index(header)

            # variables for mean and standard deviation
            mean_concentration = 0
            std_concentration = 0
            count = 0


            # iterate through the rows and calculate the standard concentration and count
            for row in csv_reader:
                concentration = float(row[concentrationIndex])
                mean_concentration += concentration
                std_concentration += concentration ** 2
                count += 1

        # calculate the mean
        mean_concentration /= float(count)

        # calculate the standard deviation
        std_concentration = math.sqrt((std_concentration / count) - mean_concentration ** 2)
        return std_concentration
    
    except FileNotFoundError:
        return "File not found"

    except (ValueError, IndexError):
        return "Invalid data format in the CSV file"

    except Exception as e:
        return f"An error occurred: {str(e)}"
    
def get_std_deviation_sample(filename):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    csv_file_path = os.path.join(current_directory, filename)

    try:
        with open(csv_file_path, 'r') as file:
            csv_reader = csv.reader(file)

            # ignore ['z', 'y', 'x', 'concentration'] row
            header = next(csv_reader)
            concentrationIndex = find_concentration_index(header)

            # initialize variables for mean and standard deviation
            mean_concentration = 0
            std_concentration = 0
            count = 0

            # Iterate through the rows and calculate mean and standard deviation
            for row in csv_reader:
                concentration = float(row[concentrationIndex])
                mean_concentration += concentration
                std_concentration += concentration ** 2
                count += 1

        # calculate the mean
        mean_concentration /= float(count)

        # calculate the standard deviation for a sample
        std_concentration = math.sqrt((std_concentration / count - (mean_concentration ** 2)) * count / (count - 1))
        return std_concentration
    
    except FileNotFoundError:
        return "File not found"

    except (ValueError, IndexError):
        return "Invalid data format in the CSV file"

    except Exception as e:
        return f"An error occurred: {str(e)}"
    
def get_sum(filename):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    csv_file_path = os.path.join(current_directory, filename)

    try:
        with open(csv_file_path, 'r') as file:
            csv_reader = csv.reader(file)
            
            # ignore ['z', 'y', 'x', 'concentration'] row
            header = next(csv_reader)
            concentrationIndex = find_concentration_index(header)

            # variables for sum
            sum_concentration = 0

            # Iterate through the rows and calculate sum
            for row in csv_reader:
                sum_concentration += float(row[concentrationIndex])
        return sum_concentration
    
    except FileNotFoundError:
        return "File not found"

    except (ValueError, IndexError):
        return "Invalid data format in the CSV file"

    except Exception as e:
        return f"An error occurred: {str(e)}"