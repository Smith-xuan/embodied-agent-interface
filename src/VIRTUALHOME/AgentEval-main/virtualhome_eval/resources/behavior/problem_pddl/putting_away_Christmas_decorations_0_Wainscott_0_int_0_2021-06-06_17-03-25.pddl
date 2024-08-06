(define (problem putting_away_Christmas_decorations)
    (:domain igibson)
    (:objects agent_n_01_1 - agent bow_n_08_1 bow_n_08_2 - bow_n_08 cabinet_n_01_1 - cabinet_n_01 floor_n_01_1 - floor_n_01 ribbon_n_01_1 ribbon_n_01_3 - ribbon_n_01)
    (:init (onfloor bow_n_08_1 floor_n_01_1) (onfloor bow_n_08_2 floor_n_01_1) (onfloor ribbon_n_01_1 floor_n_01_1) (onfloor ribbon_n_01_3 floor_n_01_1) (same_obj bow_n_08_1 bow_n_08_1) (same_obj bow_n_08_2 bow_n_08_2) (same_obj cabinet_n_01_1 cabinet_n_01_1) (same_obj floor_n_01_1 floor_n_01_1) (same_obj ribbon_n_01_1 ribbon_n_01_1) (same_obj ribbon_n_01_3 ribbon_n_01_3))
    (:goal (and (inside ribbon_n_01_3 cabinet_n_01_1) (nextto bow_n_08_2 cabinet_n_01_1) (nextto bow_n_08_1 cabinet_n_01_1) (inside ribbon_n_01_1 cabinet_n_01_1)))
)