(define (problem Work)
    (:domain virtualhome)
    (:objects
    character - character
    home_office desk walllamp mouse keyboard light powersocket cpuscreen doorjamb bedroom chair mousepad computer wall floor - object
)
    (:init
    (clean mouse)
    (obj_inside powersocket home_office)
    (obj_next_to cpuscreen mousepad)
    (obj_next_to wall powersocket)
    (surfaces chair)
    (has_plug light)
    (movable mousepad)
    (obj_next_to cpuscreen floor)
    (inside_room light bedroom)
    (obj_next_to keyboard computer)
    (obj_next_to doorjamb walllamp)
    (plugged_out computer)
    (obj_next_to computer cpuscreen)
    (has_plug keyboard)
    (obj_next_to mouse powersocket)
    (obj_next_to mousepad doorjamb)
    (sittable chair)
    (obj_next_to floor computer)
    (obj_next_to mousepad wall)
    (obj_next_to computer doorjamb)
    (obj_next_to light chair)
    (obj_next_to floor light)
    (obj_next_to walllamp floor)
    (obj_next_to light wall)
    (obj_ontop mousepad desk)
    (clean light)
    (inside_room chair bedroom)
    (facing floor computer)
    (obj_next_to wall light)
    (obj_inside wall home_office)
    (obj_next_to mouse chair)
    (obj_next_to doorjamb light)
    (obj_next_to floor powersocket)
    (obj_next_to light floor)
    (inside_room mouse bedroom)
    (obj_next_to computer floor)
    (obj_ontop mouse desk)
    (obj_next_to computer wall)
    (obj_next_to light doorjamb)
    (movable mouse)
    (obj_next_to wall mousepad)
    (obj_next_to light mouse)
    (obj_ontop cpuscreen desk)
    (obj_next_to keyboard mousepad)
    (movable keyboard)
    (obj_next_to chair computer)
    (obj_next_to light cpuscreen)
    (obj_next_to chair mouse)
    (obj_next_to wall cpuscreen)
    (surfaces floor)
    (obj_next_to chair keyboard)
    (obj_next_to mousepad mouse)
    (obj_next_to wall mouse)
    (surfaces mousepad)
    (obj_next_to desk keyboard)
    (obj_next_to light computer)
    (inside_room mousepad bedroom)
    (obj_ontop doorjamb floor)
    (obj_next_to mouse mousepad)
    (obj_ontop keyboard desk)
    (obj_next_to light light)
    (obj_next_to cpuscreen mouse)
    (obj_next_to doorjamb wall)
    (obj_next_to wall doorjamb)
    (obj_next_to chair walllamp)
    (obj_next_to floor mouse)
    (obj_next_to mousepad keyboard)
    (obj_inside walllamp home_office)
    (obj_next_to desk doorjamb)
    (obj_inside floor home_office)
    (obj_next_to light desk)
    (obj_next_to cpuscreen desk)
    (obj_next_to walllamp keyboard)
    (obj_inside doorjamb home_office)
    (obj_next_to mousepad powersocket)
    (obj_next_to chair light)
    (facing wall computer)
    (inside_room doorjamb bedroom)
    (obj_next_to floor mousepad)
    (obj_next_to cpuscreen light)
    (obj_next_to desk light)
    (lookable computer)
    (obj_next_to cpuscreen computer)
    (obj_next_to mousepad cpuscreen)
    (obj_next_to wall keyboard)
    (obj_next_to desk computer)
    (obj_inside desk home_office)
    (obj_next_to desk walllamp)
    (obj_next_to computer desk)
    (inside character bedroom)
    (obj_next_to desk wall)
    (obj_next_to computer mousepad)
    (obj_inside chair home_office)
    (facing walllamp computer)
    (obj_next_to desk mousepad)
    (plugged_out mouse)
    (clean desk)
    (obj_next_to mousepad floor)
    (obj_next_to computer light)
    (obj_next_to mousepad desk)
    (inside_room wall bedroom)
    (obj_next_to keyboard floor)
    (plugged_out keyboard)
    (obj_next_to walllamp chair)
    (grabbable mouse)
    (obj_next_to doorjamb computer)
    (obj_next_to mouse wall)
    (plugged_in light)
    (obj_next_to computer chair)
    (obj_next_to mouse desk)
    (obj_next_to desk floor)
    (obj_next_to keyboard mouse)
    (obj_inside keyboard home_office)
    (obj_inside mousepad home_office)
    (obj_next_to powersocket light)
    (obj_next_to walllamp desk)
    (obj_next_to chair floor)
    (obj_next_to light mousepad)
    (inside_room floor bedroom)
    (obj_next_to mouse floor)
    (clean keyboard)
    (grabbable chair)
    (obj_next_to cpuscreen chair)
    (obj_next_to powersocket wall)
    (obj_next_to floor floor)
    (obj_next_to doorjamb mousepad)
    (obj_next_to walllamp wall)
    (obj_next_to wall walllamp)
    (obj_next_to doorjamb desk)
    (obj_next_to computer mouse)
    (obj_next_to floor keyboard)
    (obj_next_to keyboard light)
    (obj_next_to desk powersocket)
    (obj_next_to wall floor)
    (obj_inside computer home_office)
    (off light)
    (movable desk)
    (obj_next_to cpuscreen keyboard)
    (obj_next_to wall chair)
    (obj_next_to light powersocket)
    (inside_room desk bedroom)
    (obj_next_to mousepad chair)
    (obj_next_to keyboard cpuscreen)
    (obj_next_to chair mousepad)
    (obj_next_to powersocket doorjamb)
    (has_switch light)
    (obj_next_to floor wall)
    (obj_inside mouse home_office)
    (obj_next_to mousepad computer)
    (obj_next_to powersocket mousepad)
    (obj_next_to wall computer)
    (obj_next_to powersocket floor)
    (obj_next_to mouse doorjamb)
    (obj_inside mouse desk)
    (surfaces desk)
    (obj_next_to computer keyboard)
    (facing chair computer)
    (obj_next_to floor walllamp)
    (movable chair)
    (obj_next_to desk mouse)
    (obj_next_to wall wall)
    (obj_next_to floor desk)
    (obj_next_to walllamp doorjamb)
    (obj_next_to desk chair)
    (has_switch computer)
    (obj_next_to chair cpuscreen)
    (obj_next_to keyboard chair)
    (obj_next_to powersocket desk)
    (obj_next_to powersocket mouse)
    (grabbable keyboard)
    (inside_room cpuscreen bedroom)
    (obj_next_to desk cpuscreen)
    (obj_next_to doorjamb powersocket)
    (obj_next_to chair desk)
    (obj_next_to mouse computer)
    (obj_ontop desk floor)
    (closed desk)
    (obj_next_to doorjamb floor)
    (obj_next_to computer powersocket)
    (obj_next_to floor doorjamb)
    (obj_next_to wall desk)
    (obj_next_to mouse keyboard)
    (has_plug mouse)
    (obj_next_to cpuscreen wall)
    (obj_next_to mouse light)
    (obj_next_to chair wall)
    (obj_inside cpuscreen home_office)
    (obj_next_to doorjamb mouse)
    (obj_next_to powersocket computer)
    (obj_next_to keyboard wall)
    (clean computer)
    (obj_next_to mouse cpuscreen)
    (off computer)
    (obj_next_to mousepad light)
    (obj_next_to floor cpuscreen)
    (inside_room keyboard bedroom)
    (facing doorjamb computer)
    (obj_next_to floor chair)
    (obj_next_to light keyboard)
    (obj_next_to keyboard walllamp)
    (inside_room computer bedroom)
    (obj_next_to keyboard desk)
    (obj_ontop mouse mousepad)
    (obj_inside light home_office)
)
    (:goal
    (and
        (on computer)
    )
)
    )
    