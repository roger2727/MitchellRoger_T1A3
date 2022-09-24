from data import question_data
from data import quest_data, darth_data

# test th length of question
def test_num_of_questions():

    assert len(question_data) == 10


# number of quests
def test_num_of_quests():

    assert (len(quest_data), len(darth_data)) == (5, 5)


# test correct keys
def test_keys():
    assert "question" in question_data[1]
    assert "correct_answer" in question_data[1]


if __name__ == "__main__":

    test_num_of_questions
    test_num_of_quests
    test_keys
