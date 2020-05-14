def extract_info(hospital_list):

    final_result = []

    for note in hospital_list:
        contents = note.contents

        note_info = {
            '시도' : contents[1].string,
            '시군구' : contents[2].string,
            '선별진료소' : contents[3].text,
            '전화번호' : contents[4].string
        }
        final_result.append(note_info)

    return final_result 

    print(final_result)
