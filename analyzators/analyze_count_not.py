from database.interfaces import DrgnGameInterface

def analyze_count_not():
    drgn_game_interface = DrgnGameInterface()
    count_models = drgn_game_interface.get_count_models()
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
    print(count_not_analyze['by'])
    print(count_now_analyze['by'])
