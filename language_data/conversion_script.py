import json

def get_lang_tydiqa(data_path, output_name, language):
  with open(data_path) as f:
    data = json.load(f)
  data = data['data']
  qa_data = []
  # langs = set()
  for d in data:
    # pprint(d)
    paragraphs = d['paragraphs']
    for para in paragraphs:
    #   context = para['context']
      qas = para['qas']
      for qa in qas:
        # pprint(qa)
        # answer = qa['answers']
        id = qa['id']
        # question = qa['question']
        lang = id.split('-')[0]
        # print(lang)
        # langs.add(lang)
        if lang == language:
          qa_data.append(d)
  print(f"Total data in {language} is : {len(qa_data)}")
  qa_data_dict = {'data': qa_data}
  with open(output_name, 'w') as f:
    json.dump(qa_data_dict, f, ensure_ascii=False)

if __name__=="__main__":
  data_path = "./tydiqa-goldp-v1.1-train.json"
  languages = ['korean', 'arabic', 'telugu', 'indonesian', 'bengali', 'finnish', 'english', 'swahili', 'russian']
  for language in languages:
    output_name = f"tydiqa-data/{language}_tydiqa_train.json"
    get_lang_tydiqa(data_path, output_name, language)