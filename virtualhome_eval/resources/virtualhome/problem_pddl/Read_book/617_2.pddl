(define (problem Read_book)
    (:domain virtualhome)
    (:objects
    character - character
    nightstand novel home_office bedroom drawing tablelamp bed - object
)
    (:init
    (has_paper drawing)
    (obj_next_to drawing drawing)
    (inside_room nightstand bedroom)
    (sittable bed)
    (obj_next_to nightstand novel)
    (readable novel)
    (has_switch tablelamp)
    (obj_next_to bed nightstand)
    (lieable bed)
    (obj_next_to tablelamp nightstand)
    (obj_next_to bed tablelamp)
    (clean nightstand)
    (facing drawing drawing)
    (has_paper novel)
    (grabbable drawing)
    (closed nightstand)
    (lookable drawing)
    (surfaces bed)
    (obj_inside novel nightstand)
    (containers nightstand)
    (movable novel)
    (surfaces nightstand)
    (cuttable novel)
    (obj_next_to novel nightstand)
    (inside_room bed bedroom)
    (inside_room tablelamp bedroom)
    (inside_room novel bedroom)
    (facing nightstand drawing)
    (cuttable drawing)
    (grabbable novel)
    (facing tablelamp drawing)
    (obj_next_to tablelamp bed)
    (can_open novel)
    (facing bed drawing)
    (obj_next_to nightstand tablelamp)
    (can_open nightstand)
    (inside character home_office)
    (inside_room drawing bedroom)
    (movable drawing)
    (obj_ontop tablelamp nightstand)
    (obj_next_to nightstand bed)
    (obj_inside drawing home_office)
)
    (:goal
    (and
        (holds_rh character novel)
    )
)
    )
    