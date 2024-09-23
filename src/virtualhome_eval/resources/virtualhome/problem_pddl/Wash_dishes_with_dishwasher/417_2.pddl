(define (problem Wash_dishes_with_dishwasher)
    (:domain virtualhome)
    (:objects
    character - character
    fork dishwasher dish_soap plate drinking_glass - object
)
    (:init
    (recipient plate)
    (obj_inside dish_soap dishwasher)
    (grabbable drinking_glass)
    (grabbable dish_soap)
    (plugged_out dishwasher)
    (grabbable plate)
    (grabbable fork)
    (movable dish_soap)
    (movable fork)
    (pourable drinking_glass)
    (obj_inside drinking_glass dishwasher)
    (cream dish_soap)
    (surfaces plate)
    (obj_inside fork dishwasher)
    (pourable dish_soap)
    (closed dishwasher)
    (movable drinking_glass)
    (clean dishwasher)
    (can_open dishwasher)
    (off dishwasher)
    (has_switch dishwasher)
    (recipient drinking_glass)
    (movable plate)
    (containers dishwasher)
    (obj_inside plate dishwasher)
)
    (:goal
    (and
        (closed dishwasher)
        (on dishwasher)
        (obj_ontop drinking_glass dishwasher)
        (obj_ontop dish_soap dishwasher)
        (obj_ontop fork dishwasher)
        (obj_ontop plate dishwasher)
    )
)
    )
    