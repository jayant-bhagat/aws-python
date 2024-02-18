
def search_error(file_path, error_log):
    try:
        with open(file_path, 'r') as file:
            line_number = 0
            for line in file:
                line_number += 1
                if error_log in line:
                    print(f"Error found in line {line_number}: {line.strip()}")

    except FileNotFoundError:
        print(f" file in {file_path} not  found.")

    except Exception as e:
        print(f"An error occured: {e}")                    

if __name__ == "__main__":

    error_file_path = "/var/log/journal/b78457f26b564739bc4e28cbc29abf4b/system.journal"
    error_text = "error"

    search_error(error_file_path, error_text)