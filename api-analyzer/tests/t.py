
import logging
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
import os
cwd = os.getcwd()

print("cwd =",cwd)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', encoding='utf-8', level=logging.DEBUG)
logging.info("running logging....")

f = open('./docs/api_doc.txt', 'r')
doc = f.read()
f.close()
f = open('./docs/prompt.txt', 'r')
prompt = f.read()
f.close()
print(doc % prompt)
