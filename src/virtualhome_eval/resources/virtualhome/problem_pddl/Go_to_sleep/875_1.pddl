(define (problem Go_to_sleep)
    (:domain virtualhome)
    (:objects
    character - character
    bed nightstand mat dining_room pillow window bedroom drawing tablelamp wall curtain floor - object
)
    (:init
    (obj_next_to mat wall)
    (obj_next_to floor pillow)
    (facing wall drawing)
    (obj_next_to mat curtain)
    (obj_next_to pillow floor)
    (facing window drawing)
    (inside_room nightstand bedroom)
    (obj_next_to curtain mat)
    (obj_next_to window floor)
    (obj_next_to floor mat)
    (obj_next_to window nightstand)
    (obj_next_to bed window)
    (surfaces mat)
    (obj_next_to floor bed)
    (has_switch tablelamp)
    (obj_next_to nightstand curtain)
    (obj_next_to bed nightstand)
    (obj_next_to curtain pillow)
    (obj_next_to window bed)
    (obj_ontop nightstand mat)
    (facing drawing drawing)
    (obj_ontop pillow floor)
    (obj_next_to pillow drawing)
    (obj_next_to floor drawing)
    (obj_next_to mat tablelamp)
    (cuttable drawing)
    (obj_next_to window wall)
    (obj_next_to tablelamp mat)
    (obj_next_to mat drawing)
    (inside_room mat bedroom)
    (obj_next_to nightstand tablelamp)
    (obj_next_to bed mat)
    (obj_next_to pillow pillow)
    (obj_next_to wall mat)
    (inside_room floor dining_room)
    (obj_next_to tablelamp window)
    (obj_ontop tablelamp nightstand)
    (obj_next_to curtain tablelamp)
    (obj_next_to curtain wall)
    (obj_next_to nightstand pillow)
    (surfaces floor)
    (obj_next_to drawing drawing)
    (obj_next_to curtain curtain)
    (obj_inside curtain curtain)
    (inside_room wall dining_room)
    (inside_room pillow bedroom)
    (sittable mat)
    (lookable drawing)
    (obj_next_to mat window)
    (obj_next_to bed wall)
    (obj_ontop drawing wall)
    (grabbable mat)
    (surfaces nightstand)
    (obj_next_to wall curtain)
    (obj_next_to wall pillow)
    (obj_next_to drawing pillow)
    (obj_next_to pillow nightstand)
    (obj_ontop nightstand floor)
    (obj_next_to floor curtain)
    (obj_next_to mat floor)
    (cover_object curtain)
    (obj_next_to drawing wall)
    (obj_next_to mat mat)
    (obj_next_to bed floor)
    (movable pillow)
    (inside_room window bedroom)
    (obj_next_to curtain window)
    (obj_next_to wall window)
    (inside_room wall bedroom)
    (obj_next_to mat nightstand)
    (obj_next_to drawing floor)
    (movable mat)
    (obj_next_to tablelamp curtain)
    (obj_next_to mat pillow)
    (obj_next_to bed tablelamp)
    (obj_next_to tablelamp floor)
    (movable curtain)
    (surfaces bed)
    (lieable mat)
    (obj_next_to floor nightstand)
    (containers nightstand)
    (obj_next_to wall tablelamp)
    (inside_room floor bedroom)
    (obj_next_to pillow tablelamp)
    (obj_next_to floor tablelamp)
    (obj_next_to nightstand mat)
    (obj_next_to nightstand floor)
    (obj_next_to window tablelamp)
    (obj_next_to floor floor)
    (facing tablelamp drawing)
    (facing mat drawing)
    (obj_next_to pillow curtain)
    (obj_next_to tablelamp pillow)
    (obj_next_to tablelamp wall)
    (obj_next_to wall drawing)
    (obj_next_to drawing mat)
    (obj_next_to wall floor)
    (obj_next_to bed curtain)
    (inside_room drawing bedroom)
    (obj_next_to pillow window)
    (movable drawing)
    (obj_next_to wall bed)
    (obj_next_to window pillow)
    (obj_next_to nightstand bed)
    (has_paper drawing)
    (obj_next_to curtain floor)
    (obj_next_to floor wall)
    (sittable bed)
    (obj_ontop bed mat)
    (facing floor drawing)
    (obj_next_to wall wall)
    (inside_room curtain bedroom)
    (lieable bed)
    (obj_next_to tablelamp nightstand)
    (obj_next_to curtain nightstand)
    (obj_next_to pillow mat)
    (inside_room mat dining_room)
    (obj_next_to wall nightstand)
    (obj_next_to curtain bed)
    (grabbable drawing)
    (obj_next_to window mat)
    (facing pillow drawing)
    (obj_next_to window curtain)
    (obj_next_to floor window)
    (inside_room bed bedroom)
    (obj_ontop bed floor)
    (inside_room tablelamp bedroom)
    (inside character dining_room)
    (facing nightstand drawing)
    (obj_next_to nightstand wall)
    (obj_next_to tablelamp bed)
    (grabbable pillow)
    (facing curtain drawing)
    (obj_next_to mat bed)
    (obj_next_to nightstand window)
    (inside_room drawing dining_room)
    (facing bed drawing)
    (can_open curtain)
    (can_open nightstand)
    (obj_next_to pillow wall)
)
    (:goal
    (and
        (lying character)
        (ontop character bed)
    )
)
    )
    