import os
import json
from uuid import uuid4
filenames = os.listdir("./instruction_following_eval/data/output")
out = []
for filename in filenames:
    with open(f"./instruction_following_eval/data/output/{filename}", "r") as f: 
        acc = 0
        total = 0
        acc_constraints = dict()  
        total_constraints = dict() 
        for line in f:
            line = json.loads(line)
            total += 1
            if line["follow_all_instructions"]:
                acc += 1
            fil = line["follow_instruction_list"]
            for i, constraint in enumerate(line["instruction_id_list"]):
                if constraint not in acc_constraints:
                    acc_constraints[constraint] = 0
                    total_constraints[constraint] = 0
                total_constraints[constraint] += 1
                if fil[i]:
                    acc_constraints[constraint] += 1
        acc = acc / total
        acc_constraints = {k: v / total_constraints[k] for k, v in acc_constraints.items()}
with open(f"./instruction_following_eval/data/output/result_summary-{str(uuid4())[-8:]}.jsonl", "w") as f:
    for o in out:
        f.write(json.dumps(o) + "\n")


        


