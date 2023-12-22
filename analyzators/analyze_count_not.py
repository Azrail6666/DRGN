from database.interfaces import DrgnGameInterface

def analyze_count_not():
    drgn_game_interface = DrgnGameInterface()
    count_models = drgn_game_interface.get_count_models()
    print(f"ANALYZE {count_models} GAMES")
    count_pages = count_models // 100 + 1
    requred_colors = ["b", "y", "r", "by", "br", "yr"]
    count_not_now = {}
    count_now = {}
    count_not_analyze = {}
    count_now_analyze = {}
    for requred_color in requred_colors:
        count_not_now.update({requred_color: 0})
        count_now.update({requred_color: 0})
        count_not_analyze.update({requred_color: {}})
        count_now_analyze.update({requred_color: {}})
    for page in range(count_pages):
        drgn_models = drgn_game_interface.get_data_by_page(page, 100)
        for drgn_model in drgn_models:
            for color in count_not_now:
                if drgn_model.win_type in color:
                    count_now[color] += 1
                    if count_not_now[color] in count_not_analyze[color]:
                        count_not_analyze[color][count_not_now[color]] += 1
                    else:
                        count_not_analyze[color][count_not_now[color]] = 1
                    count_not_now[color] = 0
                else:
                    count_not_now[color] += 1
                    if count_now[color] in count_now_analyze[color]:
                        count_now_analyze[color][count_now[color]] += 1
                    else:
                        count_now_analyze[color][count_now[color]] = 1
                    count_now[color] = 0
    for color in count_not_analyze:
        count_not_analyze_color_data = count_not_analyze[color]
        count_not_analyze_color_data = dict(sorted(count_not_analyze_color_data.items()))
        keys = list(count_not_analyze_color_data.keys())
        print(keys)
        for counter in keys:
            counter_sum = sum([count_not_analyze_color_data[key]] for key in count_not_analyze_color_data.keys()])