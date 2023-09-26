from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import pandas as pd
import re

# creating a Flask app
app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"origins": "*"}})

## Filter 
def filter_data(text_data, language):
  
  # # For Hindi language codes
  if language == "hindi":
    ignored_str = [',', '|', '(', ')', '[', ']', '{', '}','।', '?', ': ', ' :', '- ', ' -', '? '] 
  elif language == 'marathi':
    ignored_str = [',', '|', '(', ')', '[', ']', '{', '}','।', '?', ': ', ' :', '- ', ' -', '? ']
  else:
    ignored_str = []
  for ig in ignored_str:
    text_data = text_data.replace(ig, ' ') 
  return text_data
  

# generated file name
output_file_name = 'output' # without extension

@cross_origin()
@app.route('/word_count', methods = ['GET', 'POST'])
def word_count_text():
    if(request.method == 'GET'):
        try:
            input_data = request.args.get('input_data')
            selected_language = request.args.get('language')
            # selected_language = 'hindi'
            print("Selected language: " + selected_language)
            
            ## get word count from input data
            # split data with white space
            filtered_input_data = filter_data(input_data, selected_language)
            list_word = filtered_input_data.split()
            print(len(list_word))

            # create dictionary of words with count
            
            email_regex = re.compile(r'^[\w]+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$')
            counts = dict()
            for word in list_word:
              ## ignore numeric values, email and URL
              if not word.isdigit():
                if re.fullmatch(email_regex, word) is None:
                  if word in counts:
                      counts[word] += 1
                  else:
                      counts[word] = 1
            
            ## conert into excel          
            KeysList = list(counts.keys())
            ValuesList = list(counts.values())
            df = pd.DataFrame({'List of Words': KeysList, 'words Count': ValuesList,})
            
            # df.to_csv('file.csv', index=False)
            df.to_excel('../output_files/'+ output_file_name +'.xlsx', index=False)

    
            return jsonify({'status': "success", 'data': "Done"})
        except PermissionError:
          return jsonify({'status': "error", 'data': "Output file is open. First close it and try again"})
        except:
            return jsonify({'status': "error", 'data': "Something went wrong"})
  

@cross_origin()
@app.route('/word_count_file', methods = ['POST'])
def word_count_file():
    if(request.method == 'POST'):
        # try:
            uploaded_file = request.files.get('uplodedFile')
            selected_language = request.form.get('language')
            
            print("Selected language: " , selected_language)
            print("Uploaded File: " , uploaded_file)
            file_type= uploaded_file.filename.split('.')[-1]

            if(file_type == 'txt'):
              pass
            else:
              return jsonify({'status': "error", 'data': "Invalid file format. Allowed files with extension [ txt ]"})
            
            uploaded_file.save("./uploded_file/" + uploaded_file.filename)
            
            # get data from text file
            with open("./uploded_file/" + uploaded_file.filename, encoding="utf-8") as f:
              input_data = f.read()
            print("data from text file : ", input_data)
            
            ## get word count from input data
            # split data with white space
            filtered_input_data = filter_data(input_data, selected_language)
            list_word = filtered_input_data.split()
            print(len(list_word))

            # create dictionary of words with count
            
            email_regex = re.compile(r'^[\w]+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$')
            counts = dict()
            for word in list_word:
              ## ignore numeric values, email and URL
              if not word.isdigit():
                if re.fullmatch(email_regex, word) is None:
                  if word in counts:
                      counts[word] += 1
                  else:
                      counts[word] = 1
            
            ## conert into excel          
            KeysList = list(counts.keys())
            ValuesList = list(counts.values())
            df = pd.DataFrame({'List of Words': KeysList, 'words Count': ValuesList,})
            
            # df.to_csv('file.csv', index=False)
            df.to_excel('../output_files/'+ output_file_name +'.xlsx', index=False)

    
            return jsonify({'status': "success", 'data': "Done"})
        # except PermissionError:
        #   return jsonify({'status': "error", 'data': "Output file is open. First close it and try again"})
        # except:
        #     return jsonify({'status': "error", 'data': "Something went wrong"})
  
# driver function
if __name__ == '__main__':
    app.run(debug = True, port=5001)