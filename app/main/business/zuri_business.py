import re
import os
import openai


class AppBusiness:
    @staticmethod
    def cal_arithmetic(data):
        operation_type = 'Invalid operator type'
        status_code = 400
        print(data)
        if 'operation_type' in data:
            if 'x' in data and 'y' in data and data['operation_type'] == 'addition':
                result = data['x'] + data['y']
                operation_type = 'addition'
                status_code = 200
            elif 'x' in data and 'y' in data and data['operation_type'] == 'subtraction':
                result = data['x'] - data['y']
                operation_type = 'subtraction'
                status_code = 200
            elif 'x' in data and 'y' in data and data['operation_type'] == 'multiplication':
                result = data['x'] * data['y']
                operation_type = 'multiplication'
                status_code = 200
            else:
                operation_type = ''
                num_list = re.findall(r'\d+', data['operation_type'])
                if (len(num_list) > 0):
                    prompt_word = data['operation_type']
                else:
                    if 'x' in data and 'y' in data:
                        prompt_word = str(data['operation_type'])+ ' '+str(data['x']) + ' and '+str(data['y'])
                    else:
                        prompt_word = ''
                        operation_type = 'Invalid operator type'
                if prompt_word != '':
                    openai.api_key = os.getenv("OPENAI_API_KEY")
                    gpt_prompt = "What are the operation type in this question: " + prompt_word
                    response2 = openai.Completion.create(
                        engine="text-davinci-002",
                        prompt=gpt_prompt,
                        temperature=0.5,
                        max_tokens=256,
                        top_p=1.0,
                        frequency_penalty=0.0,
                        presence_penalty=0.0
                    )
                    if 'add' in response2['choices'][0]['text']:
                        operation_type = operation_type + 'addition'
                    if 'multi' in response2['choices'][0]['text']:
                        operation_type = operation_type + ' multiplication'
                    if 'subtract' in response2['choices'][0]['text']:
                        operation_type = operation_type + ' subtraction'

                    print("OPERATOR>>>>"+operation_type)

                    if operation_type.strip() == 'addition' and len(num_list) <= 0:
                        result = data['x'] + data['y']
                        status_code = 200
                    elif operation_type.strip() == 'multiplication' and len(num_list) <= 0:
                        result = data['x'] * data['y']
                        status_code = 200
                    elif operation_type.strip() == 'subtraction' and len(num_list) <= 0:
                        result = data['x'] - data['y']
                        status_code = 200
                    else:
                        gpt_prompt = "I want the answer to this question. "+str(prompt_word)
                        response = openai.Completion.create(
                            engine="text-davinci-002",
                            prompt=gpt_prompt,
                            temperature=0.5,
                            max_tokens=256,
                            top_p=1.0,
                            frequency_penalty=0.0,
                            presence_penalty=0.0
                        )
                        print("knk k k"+response['choices'][0]['text'])

                        answer = re.findall(r'\d+', response['choices'][0]['text'])
                        if (len(answer) > 0):
                            status_code = 200
                            if '=' in response['choices'][0]['text']:
                                result = int(answer[len(answer)-1])
                            elif 'is' in response['choices'][0]['text']:
                                result = int(answer[len(answer) - 1])
                            else:
                                result = int(answer[0])
                            print(response2['choices'][0]['text'])
                        else:
                            result = None
                else:
                    result = None
        else:
            result = None
        response_obj = {
            'slackUsername': 'trustedcoder',
            'result': result,
            'operation_type': operation_type.strip()
        }
        return response_obj, status_code
