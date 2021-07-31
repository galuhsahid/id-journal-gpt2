from tqdm import tqdm
import logging
import os

def erase(file_name: str, write_to: str, start_key: str="first_line", stop_key: str="last_line"):
    try:
        result_lines = []
        # read the file lines
        with open(file_name, 'r') as fr:
            lines = fr.readlines()
            write = False
            for line in lines:
                line = line.lower().strip("\n").strip()
                if line.strip('\n').lower().startswith(start_key):
                        write = True

                if write == True:
                        if (line.lower().strip("\n").strip() != "abstrak") and (not line.lower().strip("\n").startswith("kata kunci")):
                            result_lines.append(line.replace("\n", ""))

                if line.strip('\n').strip().lower().startswith(stop_key):
                        write = False
                        break
            if len(result_lines)>0:
                result = (' '.join(result_lines)) 
                result = "<BOS> " + result + " <EOS>"
                
                with open(write_to, 'a') as f1:
                    f1.write(result + "\n")
        
    except Exception as e:
        logging.error(e)
        logging.error(f"Error {file_name}")

def add_tokens(file_name: str, write_to: str):
    try:
        result_lines = []
        # read the file lines
        with open(file_name, 'r') as fr:
            lines = fr.readlines()
            write = False
            for line in lines:
                result_lines.append(line.replace("\n", ""))

            if len(result_lines)>0:
                result = (' '.join(result_lines)) 
                result = "<BOS> " + result + " <EOS>"
                
                with open(write_to, 'a') as f1:
                    f1.write(result + "\n")
        
    except Exception as e:
        logging.error(e)
        logging.error(f"Error {file_name}")

if __name__ == "__main__":
    # alazhar
    '''for subdir, dirs, files in os.walk("txt/alazhar"):
        for file in tqdm(files):
            filepath = subdir + os.sep + file

            if filepath.endswith(".txt"):
                erase(filepath, write_to="alazhar.txt", start_key="abstrak", stop_key="kata kunci")
    '''

    '''for subdir, dirs, files in os.walk("txt/institut_teknologi_bandung"):
        for file in tqdm(files):
            filepath = subdir + os.sep + file

            if filepath.endswith(".txt"):
                add_tokens(filepath, write_to="institut_teknologi_bandung.txt")'''
    
    '''for subdir, dirs, files in os.walk("txt/student_universitas_negeri_yogyakarta"):
        for file in tqdm(files):
            filepath = subdir + os.sep + file

            if filepath.endswith(".txt"):
                erase(filepath, write_to="student_universitas_negeri_yogyakarta.txt", start_key="abstrak", stop_key="kata kunci")
    '''

    '''for subdir, dirs, files in os.walk("txt/universitas_atmajaya"):
        for file in tqdm(files):
            filepath = subdir + os.sep + file

            if filepath.endswith(".txt"):
                erase(filepath, write_to="universitas_atmajaya.txt", start_key="abstrak", stop_key="kata kunci")'''

    '''for subdir, dirs, files in os.walk("txt/universitas_gadjah_mada"):
        for file in tqdm(files):
            filepath = subdir + os.sep + file

            if filepath.endswith(".txt"):
                add_tokens(filepath, write_to="universitas_gadjah_mada.txt")'''

    for subdir, dirs, files in os.walk("txt/universitas_negeri_yogyakarta"):
        for file in tqdm(files):
            filepath = subdir + os.sep + file

            if filepath.endswith(".txt"):
                add_tokens(filepath, write_to="universitas_negeri_yogyakarta.txt")