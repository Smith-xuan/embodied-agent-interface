(define (problem thawing_frozen_food)
    (:domain igibson)
    (:objects agent_n_01_1 - agent date_n_08_1 - date_n_08 electric_refrigerator_n_01_1 - electric_refrigerator_n_01 fish_n_02_1 fish_n_02_2 fish_n_02_4 - fish_n_02 olive_n_04_1 - olive_n_04 sink_n_01_1 - sink_n_01)
    (:init (frozen date_n_08_1) (frozen fish_n_02_1) (frozen fish_n_02_2) (frozen fish_n_02_4) (frozen olive_n_04_1) (inside date_n_08_1 electric_refrigerator_n_01_1) (inside fish_n_02_1 electric_refrigerator_n_01_1) (inside fish_n_02_2 electric_refrigerator_n_01_1) (inside fish_n_02_4 electric_refrigerator_n_01_1) (inside olive_n_04_1 electric_refrigerator_n_01_1) (same_obj date_n_08_1 date_n_08_1) (same_obj electric_refrigerator_n_01_1 electric_refrigerator_n_01_1) (same_obj fish_n_02_1 fish_n_02_1) (same_obj fish_n_02_2 fish_n_02_2) (same_obj fish_n_02_4 fish_n_02_4) (same_obj olive_n_04_1 olive_n_04_1) (same_obj sink_n_01_1 sink_n_01_1))
    (:goal (and (nextto olive_n_04_1 sink_n_01_1) (nextto fish_n_02_2 sink_n_01_1) (nextto fish_n_02_4 sink_n_01_1) (nextto date_n_08_1 fish_n_02_1)))
)