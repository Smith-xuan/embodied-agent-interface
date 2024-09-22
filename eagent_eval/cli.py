import argparse
import os


def main():
    parser = argparse.ArgumentParser(description="Embodied Evaluation CLI")
    parser.add_argument(
        "--mode",
        choices=["generate_prompts", "evaluate_results"],
        default="generate_prompts",
        help="Mode of operation (default: generate_prompts)",
    )
    parser.add_argument(
        "--eval-type",
        choices=[
            "action_sequence",
            "transition_modeling",
            "goal_interpretation",
            "subgoal_decomposition",
        ],
        default="goal_interpretation",
        help="Type of evaluation (default: goal_interpretation)",
    )
    parser.add_argument(
        "--llm-response-path",
        type=str,
        help="Path to LLM response directory",
    )
    
    parser.add_argument(
        "--output-dir",
        type=str,
        default="./output",
        help="Path to the output directory (default: output/)",
    )
    
    parser.add_argument(
        "--num-workers",
        type=int,
        default=1,
        help="Number of workers for multiprocessing (default: 1)",
    )
    
    parser.add_argument(
        "--dataset",
        choices=["virtualhome", "behavior"],
        default="behavior",
        help="The dataset to use (default: behavior)",
    )

    args = parser.parse_args()
    
    # do argument checking
    # 1. if llm_response_path is None, then mode must be generate_prompts
    # 2. llm_response_path must contain a folder named "eval_type"
    
    if args.mode == "evaluate_results":
        if not os.path.exists(os.path.join(args.llm_response_path, args.eval_type)):
            print(f"Error: {args.llm_response_path} must contain a folder named {args.eval_type} for evaluation")
            exit(1)
        
    
    if args.dataset == "behavior":
        from behavior_eval.agent_eval import agent_evaluation as behavior_agent_evaluation
        behavior_agent_evaluation(
            mode=args.mode,
            eval_type=args.eval_type,
            llm_response_path=args.llm_response_path,
            output_dir=args.output_dir,
        )
    elif args.dataset == "virtualhome":
        from virtualhome_eval.agent_eval import agent_evaluation as virtualhome_agent_evaluation
        virtualhome_agent_evaluation(
            mode=args.mode,
            eval_type=args.eval_type,
            llm_response_path=args.llm_response_path,
            output_dir=args.output_dir,
            dataset=args.dataset,
        )



if __name__ == "__main__":
    main()