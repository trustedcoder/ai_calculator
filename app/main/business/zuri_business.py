import re
import os
import openai


class AppBusiness:
    @staticmethod
    def cal_arithmetic(data):
        operation_type = 'In valid operator type'
        status_code = 400
        if data['operation_type'] == 'addition':
            result = data['x'] + data['y']
            operation_type = 'addition'
            status_code = 200
        elif data['operation_type'] == 'subtraction':
            result = data['x'] - data['y']
            operation_type = 'subtraction'
            status_code = 200
        elif data['operation_type'] == 'multiplication':
            result = data['x'] * data['y']
            operation_type = 'multiplication'
            status_code = 200
        else:
            openai.api_key = os.getenv("OPENAI_API_KEY")
            gpt_prompt = "I want the answer to this question. "+str(data['operation_type'])
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=gpt_prompt,
                temperature=0.5,
                max_tokens=256,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0
            )
            print(response['choices'][0]['text'])

            answer = re.findall(r'\d+', response['choices'][0]['text'])
            if (len(answer) > 0):
                status_code = 200
                operation_type = ''
                if '=' in response['choices'][0]['text']:
                    result = int(answer[len(answer)-1])
                elif 'is' in response['choices'][0]['text']:
                    result = int(answer[len(answer) - 1])
                else:
                    result = int(answer[0])

                gpt_prompt = "What are the operation type in this question? " + str(data['operation_type'])
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

                print(response2['choices'][0]['text'])
            else:
                result = None
        response_obj = {
            'slackUsername': 'trustedcoder',
            'result': result,
            'operation_type': operation_type.strip()
        }
        return response_obj, status_code
