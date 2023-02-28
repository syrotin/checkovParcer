#!/usr/local/bin/python3
import json
import sys

def parceCheckov():
    
    f = open(f'{sys.argv[1]}', "r")
    out = json.load(f)
    data = ""
    base = '{ "issues": ['
    end = ']}'
    try:
        for j in out:
            if 'results' in j:
                for i in j['results']['failed_checks']:
                    ruleId = str(i['check_id']).replace('\n', ':')
                    message = str(i['check_name']).replace('\n', ':')
                    filePath = str(i['file_path']).replace('\n', ':')
                    filePath = filePath[1:]
                    textRange = (i['file_line_range'])
                    result = '{"engineId": "Checkov", "ruleId": "'+ruleId+'", "type": "VULNERABILITY", "severity": "MAJOR", "primaryLocation": {"message": "'+message+'", "filePath": "'+filePath+'", "textRange": {"startLine": "'+str(textRange[0])+'", "endLine": "'+str(textRange[1])+'"}}},'
                    data=data+result
                    print(data)


        js = base + data[0:-1] + end
        file = open(f'checkov.json', 'a')
        file.write(js + '\n')
        file.close
    except (TypeError):
        for i in out['results']['failed_checks']:    
            ruleId = str(i['check_id']).replace('\n', ':')
            message = str(i['check_name']).replace('\n', ':')
            filePath = str(i['file_path']).replace('\n', ':')
            filePath = filePath[1:]
            textRange = (i['file_line_range'])
            result = '{"engineId": "Checkov", "ruleId": "'+ruleId+'", "type": "VULNERABILITY", "severity": "MAJOR", "primaryLocation": {"message": "'+message+'", "filePath": "'+filePath+'", "textRange": {"startLine": "'+str(textRange[0])+'", "endLine": "'+str(textRange[1])+'"}}},'
            data=data+result
            print(data)


        js = base + data[0:-1] + end
        file = open(f'checkov.json', 'a')
        file.write(js + '\n')
        file.close

parceCheckov()