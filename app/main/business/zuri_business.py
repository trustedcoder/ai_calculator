import re
import os
import openai


class AppBusiness:
    @staticmethod
    def cal_arithmetic(data):
        operation_type = ''
        if data['operation_type'] == 'addition':
            result = data['x'] + data['y']
            operation_type = 'addition'
        elif data['operation_type'] == 'subtraction':
            result = data['x'] - data['y']
            operation_type = 'subtraction'
        elif data['operation_type'] == 'multiplication':
            result = data['x'] * data['y']
            operation_type = 'multiplication'
        else:
            openai.api_key = os.getenv("OPENAI_API_KEY")
            gpt_prompt = "I want the answer to this question in . "+str(data['operation_type'])
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=gpt_prompt,
                temperature=0.5,
                max_tokens=256,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0
            )
            answer = re.findall(r'\d+', response['choices'][0]['text'])
            print(response['choices'][0]['text'])
            if(len(answer) > 0):
                result = int(answer[0])
            else:
                result = 0

            gpt_prompt = "What are the mathematical operations in this sentence? " + str(data['operation_type'])
            response2 = openai.Completion.create(
                engine="text-davinci-002",
                prompt=gpt_prompt,
                temperature=0.5,
                max_tokens=256,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0
            )
            if 'addition' in response2['choices'][0]['text']:
                operation_type = operation_type + 'addition'
            if 'multiplication' in response2['choices'][0]['text']:
                operation_type = operation_type + ' multiplication'
            if 'subtraction' in response2['choices'][0]['text']:
                operation_type = operation_type + ' subtraction'

        response_obj = {
            'slackUsername': 'trustedcoder',
            'result': result,
            'operation_type': operation_type
        }
        return response_obj, 200
