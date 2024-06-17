import json
import sys

import copy
import sys
import os
import os.path as osp
import copy
import math
from collections import defaultdict

import simulation.evolving_graph.utils as utils
from simulation.evolving_graph.eval_utils import *
from simulation.evolving_graph.pddlgym_planners.fd import FD
from simulation.evolving_graph.logic_score import *


def tm_input_preparation(args):
    helm_prompt_list = []
    dataset = args.dataset
    scenegraph_id = args.scene_id
    scene_id = f"scene_{scenegraph_id}"

    resource_root = osp.join(args.resource_dir, dataset)


    pddl_root = osp.join(resource_root, "pddl_files")
    pddl_problem_dir = osp.join(resource_root, "problem_pddl")
    os.makedirs(pddl_root, exist_ok=True)
    os.makedirs(pddl_problem_dir, exist_ok=True)

    success_dict_path = osp.join(resource_root, "success_task.json")
    id2action_path = osp.join(resource_root, "id2action.json")
    gold_action_path = osp.join(resource_root, "gold_action.json")

    task_dict_dir = osp.join(resource_root, "task_state_LTL_formula_accurate.json")
    prompt_path = osp.join(args.prompt_dir, "operator_prompt_complete.txt")
    helm_prompt_path = osp.join(
        args.helm_dir, f"helm_prompt/transition_modeling_vh_helm.json"
    )
    # task_dict_dir = "/viscam/u/shiyuz/svl_project/AgentEval/virtualhome/resources/task_state_updated.json"
    # prompt_path = (
    #     "/viscam/u/shiyuz/svl_project/AgentEval/virtualhome/prompts/operator_prompt_complete.txt"
    # )
    # helm_prompt_path = "/viscam/u/shiyuz/svl_project/AgentEval/virtualhome/helm/helm_prompt/operator_evaluation_vh_final_complete.json"
    # pddl_problem_dir = '/viscam/u/shiyuz/svl_project/AgentEval/virtualhome/resources/pddl_files/virtualhome'

    task_dict = json.load(open(task_dict_dir, "r"))
    success_file_id = json.load(open(success_dict_path, "r"))
    id2action = json.load(open(id2action_path, "r"))
    gold_action_dict = json.load(open(gold_action_path, "r"))

    task_dict = task_dict[scene_id]

    for task_name, task_dicts in task_dict.items():
        if task_name in ["Wash dishes by hand", "Write an email", "Wash hands"]:
            continue
        print(f"task name is {task_name}")
        task_name = "_".join(task_name.split())
        task_problem_dir = os.path.join(pddl_problem_dir, task_name)

        for file_id, _ in task_dicts.items():
            if os.path.exists(success_dict_path):
                if file_id not in success_file_id:
                    continue
            
            problem_path = os.path.join(task_problem_dir, f"{file_id}.pddl")
            problem_file = open(problem_path, "r").read()

            gold_actions_name = id2action[file_id]
            action_handlers = ""
            for action_name in gold_actions_name:
                action_param = gold_action_dict[action_name]["action_parameters"]
                action_handlers += f"(:action {action_name}\n  :parameters {action_param}\n  :precondition ()\n  :effect ()\n)\n"

            prompt = open(prompt_path, "r").read()
            prompt = prompt.replace("<problem_file>", problem_file)
            prompt = prompt.replace("<action_handlers", action_handlers)
            helm_prompt_list.append(
                {"identifier": f"{file_id}", "llm_prompt": f"{prompt}"}
            )

    # save helm prompt
    json.dump(helm_prompt_list, open(helm_prompt_path, "w"), indent=4)

def tm_output_evaluation(args):
    model_name = args.model_name
    dataset = args.dataset
    visualization = False
    save_results = False

    if dataset == 'virtualhome':
        timeout = 100
    elif dataset == 'behavior':
        timeout = 200
    
    resource_root = osp.join(args.resource_dir, dataset)
    helm_output_path = osp.join(args.helm_dir, f"helm_output/transition_modeling_{dataset}/{model_name}_outputs.json")

    # load LLM output
    helm_output = json.load(open(helm_output_path, "r"))

    # indexing path
    id2action_path = osp.join(resource_root, "id2action.json")
    id2category_path = osp.join(resource_root, "id2category_2.json")
    id2task_path = osp.join(resource_root, "id2task.json")
    id2predicate_path = osp.join(resource_root, "id2predicate.json")
    success_dict_path = osp.join(resource_root, "success_task.json")

    # evaluation path
    domain_path = osp.join(resource_root, f"{dataset}.pddl")
    domain_pd_path = osp.join(resource_root, f"{dataset}_pd.pddl")
    gold_action_path = osp.join(resource_root, "gold_action.json")
    pred2category_path = osp.join(resource_root, "predicates_category.json")

    # save path and figure path
    save_root = osp.join(args.output_dir, f"operator_eval_{model_name}")
    if not os.path.exists(save_root):
        os.makedirs(save_root)
    fig_root = os.path.join(save_root, "fig")
    if not os.path.exists(fig_root):
        os.makedirs(fig_root)
    pddl_root = osp.join(resource_root, "pddl_files")
    pddl_problem_dir = osp.join(resource_root, "problem_pddl")
    os.makedirs(pddl_root, exist_ok=True)
    os.makedirs(pddl_problem_dir, exist_ok=True)

    precond_predicate_type_res_dict_path = os.path.join(
        save_root, "precond_predicate_type_res_dict.json"
    )
    precond_action_type_dict_path = os.path.join(save_root, "precond_action_type_dict.json")
    effect_action_type_dict_path = os.path.join(save_root, "effect_action_type_dict.json")
    full_predicate_type_res_dict_path = os.path.join(
        save_root, "full_predicate_type_res_dict.json"
    )
    full_action_type_dict_path = os.path.join(save_root, "full_action_type_dict.json")

    precond_predicate_res_dict_path = os.path.join(save_root, "precond_predicate_res_dict.json")
    effect_predicate_res_dict_path = os.path.join(save_root, "effect_predicate_res_dict.json")
    full_predicate_res_dict_path = os.path.join(save_root, "full_predicate_res_dict.json")
    
    success_by_task_type_dict_path = os.path.join(save_root, "success_by_task_type_dict.json")

    task_variate_control_by_type_path = os.path.join(save_root, "task_variate_control_by_type.json")
    task_variate_control_precond_by_type_path = os.path.join(save_root, "task_variate_control_precond_by_type.json")
    task_variate_control_effect_by_type_path = os.path.join(save_root, "task_variate_control_effect_by_type.json")
    action_variate_control_path = os.path.join(save_root, "action_variate_control.json")
    action_variate_control_precond_path = os.path.join(save_root, "action_variate_control_precond.json")
    action_variate_control_effect_path = os.path.join(save_root, "action_variate_control_effect.json")

    per_task_res_path = os.path.join(save_root, "per_task_res.json")

    # load indexing dict
    id2action = json.load(open(id2action_path, "r"))
    id2category = json.load(open(id2category_path, "r"))
    id2task = json.load(open(id2task_path, "r"))
    id2predicate = json.load(open(id2predicate_path, "r"))
    success_file_id = json.load(open(success_dict_path, "r"))
    pred2category = json.load(open(pred2category_path, "r"))

    categories_set = {
        "object states",
        "object affordance",
        "object orientation",
        "object tools",
        "spatial relations",
        "non-spatial relations",
    }
    action_set = set()
    for action_list in id2action.values():
        action_set.update(action_list)
    predicate_set = set()
    for predicate in pred2category.keys():
        predicate_set.add(predicate)

    # load evaluation dict
    gold_action_dict = json.load(open(gold_action_path, "r"))
    

    # logical score (precison, recall, f1)
    # 1. precond logical score based on type 
    # 2. effect logical score based on type 
    # 3. precond logical score per action (fig)
    # 4. effect logical score per action (fig)
    # potentially record score for each predicate

    precond_predicate_type_res_dict = {}
    effect_predicate_type_res_dict = {}
    full_predicate_type_res_dict = {}
    precond_action_type_dict = {}
    effect_action_type_dict = {}
    full_action_type_dict = {}

    precond_predicate_score_dict = {}
    effect_predicate_score_dict = {}
    full_predicate_score_dict = {}
    
    # 5. success rate by planner on task type
    success_by_task_type_dict = {}

    # sensitivity analysis
    # 6. action success rate by planner on task type (precond, effect) -- change all operators/precond/effect by predicted in task
    task_variate_control_by_type = {} # all
    task_variate_control_precond_by_type = {} # precond
    task_variate_control_effect_by_type = {} # effect
    # 7. action success rate by planner for all action (precond, effect)
    action_variate_control = {} # all
    action_variate_control_precond = {} # precond
    action_variate_control_effect = {} # effect

    for category_type in categories_set:
        # [success(TP), precond false positive fail(FP), missing fail(FN)]
        precond_predicate_type_res_dict[category_type] = [0, 0, 0]
        effect_predicate_type_res_dict[category_type] = [0, 0, 0]
        success_by_task_type_dict[category_type] = [0, 0] # [success, total]
        task_variate_control_by_type[category_type] = {}
        task_variate_control_precond_by_type[category_type] = {}
        task_variate_control_effect_by_type[category_type] = {}

    # micro avg
    for action in action_set:
        # [success(TP), precond false positive fail(FP), missing fail(FN)]
        precond_action_type_dict[action] = [0, 0, 0]
        effect_action_type_dict[action] = [0, 0, 0]
        action_variate_control[action] = [0, 0] # [success, total]
        action_variate_control_precond[action] = [0, 0] # [success, total]
        action_variate_control_effect[action] = [0, 0] # [success, total]

    for pred in predicate_set:
        precond_predicate_score_dict[pred] = [0, 0, 0]
        effect_predicate_score_dict[pred] = [0, 0, 0]

    planner = FD()
    total_num = 0
    format_wrong_num = 0
    hallucination_num = 0
    total_predict_action_num = 0

    print("start evaluation")

    for output_dict in helm_output:
        file_id = output_dict["identifier"]
        if file_id not in success_file_id:
            print(f"{file_id} not in success file id!")
            continue

        total_num += 1

        task_name = id2task[file_id]
        print(f"task name is {task_name}")
        
        task_name = "_".join(task_name.split())
        if dataset == 'virtualhome':
            task_problem_dir = os.path.join(pddl_problem_dir, task_name)
        elif dataset == 'behavior':
            task_problem_dir = pddl_problem_dir
        problem_path = os.path.join(task_problem_dir, f"{file_id}.pddl")
        
        category_name_list = id2category[file_id]
        print(f"category names are {category_name_list}")

        predicted_action = output_dict["llm_output"]
        # if llm output starts with ```json
        if predicted_action.startswith("```json"):
            predicted_action = predicted_action[7:]
            predicted_action = predicted_action.strip("```")
        predicted_action = (
            predicted_action.strip().replace("\n", "")
        )
        predicted_action = predicted_action.replace("'", '"')
        try:
            predicted_action = json.loads(predicted_action)
            predicted_action = predicted_action["output"]
        except Exception as e:
            pass
        # print(predicted_action, flush=True)

        try:
            predicted_action = extract_action_details(content=predicted_action)
        except Exception as e:
            format_wrong_num += 1
            print(f"Error in extracting action details: {e}")
            print(f"format wrong num is {format_wrong_num}")
            continue

        print("GPT predicted action body:", flush=True)
        if predicted_action is None or predicted_action == "":
            continue

        predicted_domain_path = os.path.join(pddl_root, f"predicted_{model_name}")
        gold_domain_path = os.path.join(pddl_root, f"gold_{model_name}")
        os.makedirs(predicted_domain_path, exist_ok=True)
        os.makedirs(gold_domain_path, exist_ok=True)

        gold_actions = {}
        gold_actions_name = id2action[file_id]
        for action_name in gold_actions_name:
            gold_actions[action_name] = gold_action_dict[action_name]

        # start eval
        for action_name, action_dict in predicted_action.items():
            total_predict_action_num += 1
            if action_name not in gold_actions_name:
                hallucination_num += 1
                continue
            
            gold_action = gold_actions[action_name]

            # print predicted action
            pred_str = ""
            pred_str += f":action {action_name}\n"
            pred_str += f'  :parameters {action_dict["action_parameters"]}\n'
            pred_str += f'  :preconditions {action_dict["action_preconditions"]}\n'
            pred_str += f'  :effects {action_dict["action_effects"]}\n'

            gold_str = ""
            gold_str += f":action {action_name}\n"
            gold_str += f'  :parameters {gold_action["action_parameters"]}\n'
            gold_str += f'  :preconditions {gold_action["action_preconditions"]}\n'
            gold_str += f'  :effects {gold_action["action_effects"]}\n'

            print("Gold action:")
            special_print(gold_str)
            print("GPT predicted action")
            special_print(pred_str)

            # logical score
            gold_action = gold_action_dict[action_name]

            # match preconditions and effects
            (
                precond_similarity_score,
                matched_precond,
                unmatched_pred_precond,
                unmatched_gold_precond,
            ) = calculate_logic_score(
                action_dict["action_preconditions"],
                gold_action["action_preconditions"],
            )
            (
                effect_similarity_score,
                matched_effect,
                unmatched_pred_effect,
                unmatched_gold_effect,
            ) = calculate_logic_score(
                action_dict["action_effects"], gold_action["action_effects"]
            )


            # record precondition
            for pred in matched_precond:
                if pred == "()":
                    continue
                precond_predicate_type_res_dict[pred2category[pred]][0] += 1
                precond_action_type_dict[action_name][0] += 1
                precond_predicate_score_dict[pred][0] += 1
            print(f"{unmatched_pred_precond=}")
            for pred in unmatched_pred_precond:
                if pred == "()":
                    continue
                if pred not in pred2category.keys():
                    continue
                precond_predicate_type_res_dict[pred2category[pred]][1] += 1
                precond_action_type_dict[action_name][1] += 1
                precond_predicate_score_dict[pred][1] += 1
            for pred in unmatched_gold_precond:
                if pred == "()":
                    continue
                precond_predicate_type_res_dict[pred2category[pred]][2] += 1
                precond_action_type_dict[action_name][2] += 1
                precond_predicate_score_dict[pred][2] += 1
            
            # record effect
            for pred in matched_effect:
                if pred == "()":
                    continue
                effect_predicate_type_res_dict[pred2category[pred]][0] += 1
                effect_action_type_dict[action_name][0] += 1
                effect_predicate_score_dict[pred][0] += 1
            for pred in unmatched_pred_effect:
                if pred == "()":
                    continue
                if pred not in pred2category.keys():
                    continue
                effect_predicate_type_res_dict[pred2category[pred]][1] += 1
                effect_action_type_dict[action_name][1] += 1
                effect_predicate_score_dict[pred][1] += 1
            for pred in unmatched_gold_effect:
                if pred == "()":
                    continue
                effect_predicate_type_res_dict[pred2category[pred]][2] += 1
                effect_action_type_dict[action_name][2] += 1
                effect_predicate_score_dict[pred][2] += 1


        predicted_action_copy = copy.deepcopy(predicted_action)
        # success rate by planner & sensitivity analysis
        # partial operator trials
        # category_name_list = id2category[file_id]

        # increase tot number for success rate
        for category_name in category_name_list:
            success_by_task_type_dict[category_name][1] += 1
            # increase tot number for sensitivity analysis
            for action in gold_actions_name:
                if action not in task_variate_control_by_type[category_name].keys():
                    task_variate_control_by_type[category_name][action] = [0, 1]
                else:
                    task_variate_control_by_type[category_name][action][1] += 1
                if action not in task_variate_control_precond_by_type[category_name]:
                    task_variate_control_precond_by_type[category_name][action] = [0, 1]
                else:
                    task_variate_control_precond_by_type[category_name][action][1] += 1
                if action not in task_variate_control_effect_by_type[category_name]:
                    task_variate_control_effect_by_type[category_name][action] = [0, 1]
                else:
                    task_variate_control_effect_by_type[category_name][action][1] += 1

        for action in gold_actions_name:      
            action_variate_control[action][1] += 1
            action_variate_control_precond[action][1] += 1
            action_variate_control_effect[action][1] += 1
            
        # gold action trial
        for action_name in predicted_action.keys():
            assert predicted_action_copy == predicted_action
            if action_name not in gold_actions_name:
                print(f"{action_name} not in gold! Hallucination!")
                continue
            single_variate_action = {}
            gold_action_dict_copy = copy.deepcopy(gold_action_dict)
            for gd_action_name in gold_actions_name:
                single_variate_action[gd_action_name] = copy.deepcopy(
                    gold_action_dict_copy[gd_action_name]
                )
            domain_file_path = complete_pddl_domain(
                single_variate_action,
                gold_action_dict,
                domain_pd_path,
                file_id,
                predicted_domain_path,
                action_name_key='gold',
            )
            try:
                pddl_plan = planner.plan_from_pddl(domain_file_path, problem_path, timeout=timeout)
                print(f"Gold test: task {file_id}'s {action_name} succeeded")
            except Exception as e:
                print(f"Gold test: task {file_id}'s {action_name} failed")
                raise e

        # per action trial
        for action_name in predicted_action.keys():
            assert predicted_action_copy == predicted_action
            if action_name not in gold_actions_name:
                print(f"{action_name} not in gold! Hallucination!")
                continue
            single_variate_action = {}
            gold_action_dict_copy = copy.deepcopy(gold_action_dict)
            for gd_action_name in gold_actions_name:
                single_variate_action[gd_action_name] = copy.deepcopy(gold_action_dict_copy[gd_action_name])
            single_variate_action[action_name] = copy.deepcopy(predicted_action_copy[action_name])
            # print(f"{single_variate_action=}")
            domain_file_path = complete_pddl_domain(
                single_variate_action,
                gold_action_dict,
                domain_pd_path,
                file_id,
                predicted_domain_path,
                action_name_key=action_name,
            )
            try:
                pddl_plan = planner.plan_from_pddl(
                    domain_file_path, problem_path, timeout=timeout
                )
                for category_name in category_name_list:
                    task_variate_control_by_type[category_name][action_name][0] += 1
                action_variate_control[action_name][0] += 1
                print(f"Action test: task {file_id}'s {action_name} succeeded")
            except Exception as e:
                print(f"Action test: task {file_id}'s {action_name} failed")

        # precondition / effect trial
        for action_name in predicted_action.keys():
            assert predicted_action_copy == predicted_action
            if action_name not in gold_actions_name:
                print(f"{action_name} not in gold! Hallucination!")
                continue
            single_variate_action = {}
            gold_action_dict_copy = copy.deepcopy(gold_action_dict)
            for gd_action_name in gold_actions_name:
                single_variate_action[gd_action_name] = copy.deepcopy(gold_action_dict_copy[
                    gd_action_name
                ])
            single_variate_action[action_name]["action_preconditions"] = copy.deepcopy(
                predicted_action_copy[action_name]["action_preconditions"]
            )
            domain_file_path = complete_pddl_domain(
                single_variate_action,
                gold_action_dict,
                domain_pd_path,
                file_id,
                predicted_domain_path,
                action_name_key=action_name + "_precond",
            )
            try:
                pddl_plan = planner.plan_from_pddl(
                    domain_file_path, problem_path, timeout=timeout
                )
                for category_name in category_name_list:
                    task_variate_control_precond_by_type[category_name][action_name][0] += 1
                action_variate_control_precond[action_name][0] += 1
                print(f"Precondition test: task {file_id}'s {action_name} succeeded")
            except Exception as e:
                print(f"Precondition test: task {file_id}'s {action_name} failed")

        for action_name in predicted_action.keys():
            assert predicted_action_copy == predicted_action
            if action_name not in gold_actions_name:
                print(f"{action_name} not in gold! Hallucination!")
                continue
            single_variate_action = {}
            gold_action_dict_copy = copy.deepcopy(gold_action_dict)
            for gd_action_name in gold_actions_name:
                single_variate_action[gd_action_name] = (
                    copy.deepcopy(gold_action_dict_copy[gd_action_name]
                ))
            single_variate_action[action_name]["action_effects"] = copy.deepcopy(
                predicted_action_copy[action_name]["action_effects"]
            )
            domain_file_path = complete_pddl_domain(
                single_variate_action,
                gold_action_dict,
                domain_pd_path,
                file_id,
                predicted_domain_path,
                action_name_key=action_name + "_effect",
            )
            try:
                pddl_plan = planner.plan_from_pddl(
                    domain_file_path, problem_path, timeout=timeout
                )
                for category_name in category_name_list:
                    task_variate_control_effect_by_type[category_name][action_name][0] += 1
                action_variate_control_effect[action_name][0] += 1
                print(f"Effect test: task {file_id}'s {action_name} succeeded")
            except Exception as e:
                print(f"Effect test: task {file_id}'s {action_name} failed")

        # all action trial
        domain_file_path = complete_pddl_domain(
            predicted_action,
            gold_action_dict,
            domain_pd_path,
            file_id,
            predicted_domain_path,
        )
        try:
            pddl_plan = planner.plan_from_pddl(
                domain_file_path, problem_path, timeout=timeout
            )
            for category_name in category_name_list:
                success_by_task_type_dict[category_name][0] += 1
            print(f"Holistic test: task {file_id} succeeded")
        except Exception as e:
            print(f"Holistic test: task {file_id} failed")

        # single action ablation
        # ablation_action = "walk_towards"
        # if ablation_action not in task_ablation_dict.keys():
        #     task_ablation_dict[ablation_action] = {}
        # if task_name not in task_ablation_dict[ablation_action].keys():
        #     task_ablation_dict[ablation_action][task_name] = [0, 1]
        # else:
        #     task_ablation_dict[ablation_action][task_name][1] += 1
        # print(f"Ablation on {ablation_action}!")
        # walk_ablation = predicted_action_copy
        # walk_ablation[ablation_action] = gold_action_dict[ablation_action]
        # domain_file_path = complete_pddl_domain(
        #     walk_ablation,
        #     gold_action_dict,
        #     domain_pd_path,
        #     file_id,
        #     predicted_domain_path,
        #     action_name_key=ablation_action + "_ablation",
        # )
        # try:
        #     pddl_plan = planner.plan_from_pddl(domain_file_path, problem_path)
        #     task_ablation_dict[ablation_action][task_name][0] += 1
        #     print(f"Ablation test: task {file_id} succeeded")
        # except:
        #     print(f"Ablation test: task {file_id} failed")

        sys.stdout.flush()


    # results post-processing logical scores

    # full is the sum of precond and effect
    for category_type in categories_set:
        full_predicate_type_res_dict[category_type] = [
            precond_predicate_type_res_dict[category_type][0]
            + effect_predicate_type_res_dict[category_type][0],
            precond_predicate_type_res_dict[category_type][1]
            + effect_predicate_type_res_dict[category_type][1],
            precond_predicate_type_res_dict[category_type][2]
            + effect_predicate_type_res_dict[category_type][2],
        ]
    
    # full is the sum of precond and effect
    for action in action_set:
        full_action_type_dict[action] = [
            precond_action_type_dict[action][0] + effect_action_type_dict[action][0],
            precond_action_type_dict[action][1] + effect_action_type_dict[action][1],
            precond_action_type_dict[action][2] + effect_action_type_dict[action][2],
        ]
    
    # full is the sum of precond and effect
    for pred in predicate_set:
        full_predicate_score_dict[pred] = [
            precond_predicate_score_dict[pred][0] + effect_predicate_score_dict[pred][0],
            precond_predicate_score_dict[pred][1] + effect_predicate_score_dict[pred][1],
            precond_predicate_score_dict[pred][2] + effect_predicate_score_dict[pred][2],
        ]

    # precond logical score based on type
    precond_predicate_type_res_dict = calculate_precision_recall_f1(
        precond_predicate_type_res_dict
    )

    # effect logical score based on type
    effect_predicate_type_res_dict = calculate_precision_recall_f1(
        effect_predicate_type_res_dict
    )

    full_predicate_type_res_dict = calculate_precision_recall_f1(full_predicate_type_res_dict)

    # precond logical score per action
    precond_action_type_dict = calculate_precision_recall_f1(precond_action_type_dict)

    # effect logical score per action
    effect_action_type_dict = calculate_precision_recall_f1(effect_action_type_dict)

    full_action_type_dict = calculate_precision_recall_f1(full_action_type_dict)
    
    # precondition predicate score per predicate
    precond_predicate_score_dict = calculate_precision_recall_f1(precond_predicate_score_dict)

    # effect predicate score per predicate
    effect_predicate_score_dict = calculate_precision_recall_f1(effect_predicate_score_dict)

    # full predicate score per predicate
    full_predicate_score_dict = calculate_precision_recall_f1(full_predicate_score_dict)

    print(f'Format wrong num is {format_wrong_num}!!!')

    

    # print out precision recall f1 
    print("Precondition predicate type res dict:")
    print_precision_recall_f1(precond_predicate_type_res_dict)
    print("Effect predicate type res dict:")
    print_precision_recall_f1(effect_predicate_type_res_dict)
    
    print("Precondition action type dict:")
    print_precision_recall_f1(precond_action_type_dict)
    print("Effect action type dict:")
    print_precision_recall_f1(effect_action_type_dict)
    print("Full action type dict:")
    print_precision_recall_f1(full_action_type_dict)
    print("Precondition predicate score dict:")
    print_precision_recall_f1(precond_predicate_score_dict)
    print("Effect predicate score dict:")
    print_precision_recall_f1(effect_predicate_score_dict)
    print("Full predicate score dict:")
    print_precision_recall_f1(full_predicate_score_dict)


    # post-process sensitivity analysis
    task_variate_control_by_type = calculate_success_rate_by_category(task_variate_control_by_type)
    task_variate_control_precond_by_type = calculate_success_rate_by_category(
        task_variate_control_precond_by_type
    )
    task_variate_control_effect_by_type = calculate_success_rate_by_category(
        task_variate_control_effect_by_type
    )

    print("Task variate control by type:")
    print_success_rate_by_category(task_variate_control_by_type)
    print("Task variate control precond by type:")
    print_success_rate_by_category(task_variate_control_precond_by_type)
    print("Task variate control effect by type:")
    print_success_rate_by_category(task_variate_control_effect_by_type)
    print("Action variate control:")
    print(action_variate_control)
    print("Action variate control precond:")
    print(action_variate_control_precond)
    print("Action variate control effect:")
    print(action_variate_control_effect)


    # post-process success rate by planner on task type
    print('\n')
    print(f'{total_num=}')
    print(f'{format_wrong_num=}, rate={100.*format_wrong_num/total_num:.2f}')
    print(
        f"{hallucination_num=}, rate={100.*hallucination_num/total_predict_action_num:.2f}"
    )
    success_by_task_type_dict = calculate_success_rate(success_by_task_type_dict)
    print("MODEL NAME!!! ", model_name)
    print("\n")
    print("Success by task type dict:")
    print_success_rate(success_by_task_type_dict)
    print("\n")
    print("Full predicate type res dict:")
    print_precision_recall_f1(full_predicate_type_res_dict)
    # output = [full_predicate_type_res_dict, success_by_task_type_dict, 100.*format_wrong_num/total_num, 100.*hallucination_num/total_predict_action_num]
    output = [task_variate_control_by_type, task_variate_control_precond_by_type, task_variate_control_effect_by_type, action_variate_control, action_variate_control_precond, action_variate_control_effect]

    # save results
    if save_results:
        json.dump(precond_predicate_type_res_dict, open(precond_predicate_type_res_dict_path, "w"), indent=4)
        json.dump(effect_predicate_type_res_dict, open(effect_predicate_type_res_dict_path, "w"), indent=4)
        json.dump(full_predicate_type_res_dict, open(full_predicate_type_res_dict_path, "w"), indent=4)
        json.dump(precond_action_type_dict, open(precond_action_type_dict_path, "w"), indent=4)
        json.dump(effect_action_type_dict, open(effect_action_type_dict_path, "w"), indent=4)
        json.dump(full_action_type_dict, open(full_action_type_dict_path, "w"), indent=4)
        json.dump(precond_predicate_score_dict, open(precond_predicate_res_dict_path, "w"), indent=4)
        json.dump(effect_predicate_score_dict, open(effect_predicate_res_dict_path, "w"), indent=4)
        json.dump(full_predicate_score_dict, open(full_predicate_res_dict_path, "w"), indent=4)
        json.dump(
            success_by_task_type_dict, open(success_by_task_type_dict_path, "w"), indent=4
        )
        json.dump(task_variate_control_by_type, open(task_variate_control_by_type_path, "w"), indent=4)
        json.dump(task_variate_control_precond_by_type, open(task_variate_control_precond_by_type_path, "w"), indent=4)
        json.dump(task_variate_control_effect_by_type, open(task_variate_control_effect_by_type_path, "w"), indent=4)
        json.dump(action_variate_control, open(action_variate_control_path, "w"), indent=4)
        json.dump(action_variate_control_precond, open(action_variate_control_precond_path, "w"), indent=4)
        json.dump(action_variate_control_effect, open(action_variate_control_effect_path, "w"), indent=4)
    
    return output

