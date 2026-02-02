# from tasks.t_1.prompt_injection import main
# from tasks.t_2.input_llm_based_validation import main
# from tasks.t_3.output_llm_based_validation import main
from tasks.t_3.streaming_pii_guardrail import main

if __name__ == "__main__":
    # main()
    # main(soft_response=False)
    main(presidio=False)


# python starter.py
