(define (problem cleaning_windows)
    (:domain igibson)
    (:objects agent_n_01_1 - agent cabinet_n_01_1 - cabinet_n_01 rag_n_01_1 rag_n_01_2 - rag_n_01 sink_n_01_1 - sink_n_01 towel_n_01_1 towel_n_01_2 - towel_n_01 window_n_01_1 window_n_01_2 - window_n_01)
    (:init (dusty window_n_01_1) (dusty window_n_01_2) (inside rag_n_01_1 cabinet_n_01_1) (inside rag_n_01_2 cabinet_n_01_1) (inside towel_n_01_1 cabinet_n_01_1) (inside towel_n_01_2 cabinet_n_01_1) (not (dusty sink_n_01_1)) (not (soaked rag_n_01_1)) (not (soaked rag_n_01_2)) (same_obj cabinet_n_01_1 cabinet_n_01_1) (same_obj rag_n_01_1 rag_n_01_1) (same_obj rag_n_01_2 rag_n_01_2) (same_obj sink_n_01_1 sink_n_01_1) (same_obj towel_n_01_1 towel_n_01_1) (same_obj towel_n_01_2 towel_n_01_2) (same_obj window_n_01_1 window_n_01_1) (same_obj window_n_01_2 window_n_01_2))
    (:goal (and (soaked rag_n_01_1) (soaked rag_n_01_2) (not (dusty window_n_01_2)) (not (dusty window_n_01_1))))
)