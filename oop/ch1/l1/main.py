def destroy_walls(wall_health):
    new_hp = []
    for w in wall_health:
        if w > 0:
            new_hp.append(w)
    return new_hp