import naver_cafe as cafe

links = cafe.make_board_url(cafe.get_board_info(""))
for l in links:
    print(len(cafe.get_data_from_board(l)))