mod_space = 12
opt_000 = [0, 0, 0]
opt_001 = [0, 0, 1]
opt_002 = [0, 0, 2]
opt_003 = [0, 0, 3]
opt_004 = [0, 0, 4]
opt_005 = [0, 0, 5]
opt_006 = [0, 0, 6]
opt_011 = [0, 1, 1]
opt_012 = [0, 1, 2]
opt_013 = [0, 1, 3]
opt_014 = [0, 1, 4]
opt_015 = [0, 1, 5]
opt_016 = [0, 1, 6]
opt_022 = [0, 2, 2]
opt_023 = [0, 2, 3]
opt_024 = [0, 2, 4]
opt_025 = [0, 2, 5]
opt_026 = [0, 2, 6]
opt_027 = [0, 2, 7]
opt_033 = [0, 3, 3]
opt_034 = [0, 3, 4]
opt_035 = [0, 3, 5]
opt_036 = [0, 3, 6]
opt_037 = [0, 3, 7]
opt_044 = [0, 4, 4]
opt_045 = [0, 4, 5]
opt_046 = [0, 4, 6]
opt_047 = [0, 4, 7]
opt_048 = [0, 4, 8]
opt_055 = [0, 5, 5]
opt_056 = [0, 5, 6]

repeating_forms = [opt_000, opt_001, opt_002, opt_003, opt_011, opt_022, opt_033]
all_opt_forms = [opt_000, opt_001, opt_002, opt_003, opt_004, opt_005, opt_006, opt_011,
                 opt_012, opt_013, opt_014, opt_015, opt_016, opt_022, opt_023, opt_024,
                 opt_025, opt_026, opt_027, opt_033, opt_034, opt_035, opt_036, opt_037,
                 opt_044, opt_045, opt_046, opt_047, opt_048, opt_055, opt_056]
non_repeating_forms = [opt_012, opt_013, opt_014, opt_023, opt_024]
triads = [opt_037, opt_047, opt_048]
rojavai_forms = [opt_024, opt_014]
victors_forms =  [opt_014, opt_023, opt_013]


def permute(opt_form):
    all = []

    for i in range(0, 3):
        x, y, z = opt_form[i], opt_form[(i + 1) % 3], opt_form[(i + 2) % 3]
        all.append([x, y, z])
    for i in range(0, 3):
        x, y, z = opt_form[i], opt_form[(i - 1) % 3], opt_form[(i - 2) % 3]
        all.append([x, y, z])
    return all


def transpose(permuted_list):
    transposed = []

    for point in permuted_list:
        for i in range(0, mod_space):
            new_triad = []
            for pitch in point:
                new_pitch = (pitch + i) % mod_space
                new_triad.append(new_pitch)
            transposed.append(new_triad)
    #print(f'transposed: {transposed}')
    return transposed


def the_point_of_it_all(raw_form_list):
    all_the_points = []

    for norm_form in raw_form_list:
        current_list = transpose(permute(norm_form))
        all_the_points.append(current_list)
    return all_the_points


